const int ledPin = 13; 
int incomingByte;      
int random_value;
void setup() {
  
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
 
void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }

  random_value = random(0,100);
  Serial.println(random_value);
}
