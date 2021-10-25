void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}
void loop() {
    Serial.println("ON_test");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(300);

    Serial.println("OFF_test");
    digitalWrite(LED_BUILTIN, LOW);
    delay(300);
}




