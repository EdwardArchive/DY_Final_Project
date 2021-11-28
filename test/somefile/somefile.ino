
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    	
    pinMode(9, OUTPUT);
    pinMode(8, INPUT);
            

    Serial.begin(9600);
}
void loop() {
	
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
    delay(500); 

            
	if(distance<20){
		digitalWrite(LED_BUILTIN, HIGH);
		digitalWrite(2, LOW);
		}
	if(distance>20){
		digitalWrite(LED_BUILTIN, LOW);
		digitalWrite(2, HIGH);
		}

}
