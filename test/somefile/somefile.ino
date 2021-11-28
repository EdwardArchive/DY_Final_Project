
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    
    Serial.begin(9600);
}
void loop() {
	for(int i=0; i<5; i++){
		digitalWrite(LED_BUILTIN, HIGH);
		delay(250);
		digitalWrite(LED_BUILTIN, LOW);
		delay(250);
		}
	digitalWrite(2, HIGH);
	delay(1000);
	digitalWrite(2, LOW);
	delay(1000);

}
