#include <Servo.h>
#include <Wire.h>
Servo servo;
void setup() {
  // put your setup code here, to run once:
  servo.attach(3);
  Wire.begin(4);
  Wire.onReceive(ServoEvent);
  Serial.begin(9600);
  updateServo(0);
}


void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}

void ServoEvent(int howMany){
    while( 1 <= Wire.available() ){ // loop through all bytes but the last
      int c = Wire.read();
      Serial.println(c);
      updateServo(c);
    }
  
  }

void updateServo(int position){
    servo.write(position);
    
  }
