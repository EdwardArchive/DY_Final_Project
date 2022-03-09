from PathInfo import PathInfo
pathinfo = PathInfo()
class Convert :
    
    def __init__(self,codelist):
        self.codelist = codelist
        self.codebase = """
void setup() {{
         pinMode(LED_BUILTIN, OUTPUT);
{code_setup}
         Serial.begin(9600);
}}
void loop() {{
{code_text}
}}
"""
        self.codedict = {
            "LED_ON":"digitalWrite(LED_BUILTIN, HIGH);",
            "LED_OFF":"digitalWrite(LED_BUILTIN, LOW);",
            "Sleep":"delay({option});",
            "Digital_PIN_ON":"digitalWrite({option}, HIGH);",
            "Digital_PIN_OFF":"digitalWrite({option}, LOW);",
            "loop-start":"for(int i=0; i<{option}; i++){{",
            "loop-end":"}",
            "if":"if({option}){{",
            "if-end":"}",
            "break":"break;",
            "UltrasoundSensor":"""
    long duration, distance;
    digitalWrite(9, LOW);
    delayMicroseconds(2);
    digitalWrite(9, HIGH);
    delayMicroseconds(10);
    digitalWrite(9, LOW);
    duration = pulseIn (8, HIGH); 
    distance = duration * 17 / 1000; 
    Serial.println(duration ); 
    Serial.println("DIstance : ");
    Serial.print(distance); 
    Serial.println(" Cm");
    delay({option}); 

            """,
            "Analog_PIN_wt":"analogWrite({PIN_NUM},{Value});",
            "Analog_PIN_rd":"{Var} = analogRead({PIN_NUM});"
        }
        self.code_setup_dict={
            "UltrasoundSensor":"""
        pinMode(9, OUTPUT);
        pinMode(8, INPUT);
            """,
            "Analog_PIN_wt" : "pinMode({PIN_NUM},OUTPUT);",
            "Analog_PIN_rd" : "pinMode({PIN_NUM},INPUT);"
        }
        self.option_list=['Sleep','Digital_PIN_ON','Digital_PIN_OFF','UltrasoundSensor','loop-start','if','Analog_PIN_wt','Analog_PIN_rd']
    
    def Converter(self):
        code_text = ""
        code_setup = ""
        indent_count = 1
        save_pin=[]
        for command in self.codelist :
            if command.split('|')[0] in self.option_list:
                if command.split('|')[0] == 'UltrasoundSensor':
                    code_setup+="\t"+self.code_setup_dict[command.split('|')[0]]+"\n"
                    code_text += "\t"*indent_count+self.codedict[command.split('|')[0]].format(option=command.split('|')[1])+"\n"

                elif command.split('|')[0] == 'Analog_PIN_wt':
                    if command.split('|')[1] not in save_pin:
                        code_setup+="\t"+self.code_setup_dict[command.split('|')[0]].format(PIN_NUM=command.split('|')[1])+"\n"
                    code_text += "\t"*indent_count+self.codedict[command.split('|')[0]].format(PIN_NUM=command.split('|')[1] , Value=command.split('|')[2])+"\n"
                    save_pin.append(command.split('|')[1])

                elif command.split('|')[0] == 'Analog_PIN_rd':
                    if command.split('|')[2] not in save_pin:
                        code_setup+="\t"+self.code_setup_dict[command.split('|')[0]].format(PIN_NUM=command.split('|')[2])+"\n"
                    code_text += "\t"*indent_count+self.codedict[command.split('|')[0]].format(Var=command.split('|')[1], PIN_NUM=command.split('|')[2])+"\n"
                    save_pin.append(command.split('|')[2])

                else : 
                    code_text += "\t"*indent_count+self.codedict[command.split('|')[0]].format(option=command.split('|')[1])+"\n"
            else:
                code_text += "\t"*indent_count+self.codedict[command]+"\n"

            if command.split('|')[0] in ['loop-start','if']:
                indent_count += 1
            
            elif command.split('|')[0] in ['loop-end','if-end']:
                indent_count -= 1


        code_done = self.codebase.format(code_setup=code_setup,code_text=code_text)
        with open(pathinfo.ino_path, 'w') as f:
            f.write(code_done)
        return code_done

    

        