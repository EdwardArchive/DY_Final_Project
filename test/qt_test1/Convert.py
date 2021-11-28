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

            """
        }
        self.code_setup_dict={
            "UltrasoundSensor":"""
    pinMode(9, OUTPUT);
    pinMode(8, INPUT);
            """
        }
        self.option_list=['Sleep','Digital_PIN_ON','Digital_PIN_OFF','UltrasoundSensor','loop-start','if']
    
    def Converter(self):
        code_text = ""
        code_setup = ""
        indent_count = 1
        for command in self.codelist :
            if command.split('|')[0] in self.option_list:
                code_text += "\t"*indent_count+self.codedict[command.split('|')[0]].format(option=command.split('|')[1])+"\n"
                if command.split('|')[0] == 'UltrasoundSensor':
                    code_setup+="\t"*indent_count+self.code_setup_dict[command.split('|')[0]]+"\n"
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

    

        