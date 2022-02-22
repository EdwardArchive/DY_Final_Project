
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    	pinMode(5,OUTPUT);
	pinMode(6,OUTPUT);
	pinMode(7,OUTPUT);
	pinMode(5,OUTPUT);
	pinMode(6,OUTPUT);
	pinMode(7,OUTPUT);

    Serial.begin(9600);
}
void loop() {
	analogWrite(5,0);
	analogWrite(6,0);
	analogWrite(7,0);
	delay(500);
	analogWrite(5,255);
	analogWrite(6,255);
	analogWrite(7,255);
	delay(500);

}
