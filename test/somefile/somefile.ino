
void setup() {
         pinMode(LED_BUILTIN, OUTPUT);
	
        pinMode(9, OUTPUT);
        pinMode(8, INPUT);
            
	pinMode(5,OUTPUT);
	pinMode(6,OUTPUT);
	pinMode(7,OUTPUT);

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

            
	if(distance<10){
		analogWrite(7,255);
		analogWrite(6,0);
		analogWrite(5,0);
		delay(100);
		}
	if(distance>10 && distance <30){
		analogWrite(6,255);
		analogWrite(5,0);
		analogWrite(7,0);
		delay(100);
		}
	if(distance>30){
		analogWrite(5,255);
		analogWrite(7,0);
		analogWrite(6,0);
		delay(100);
		}


}
