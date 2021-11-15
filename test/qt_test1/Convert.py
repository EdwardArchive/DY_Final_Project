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
            "Sleep":"delay(100);"
        }
    
    def Converter(self):
        code_text=""
        code_setup=""
        for command in self.codelist :
            code_text += "\t"+self.codedict[command]+"\n"
        code_done = self.codebase.format(code_setup=code_setup,code_text=code_text)
        with open(pathinfo.ino_path, 'w') as f:
            f.write(code_done)
        return code_done

    

        