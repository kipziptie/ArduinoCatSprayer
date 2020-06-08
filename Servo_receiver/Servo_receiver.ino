
#include <Servo.h>
#include <Wire.h>
Servo servo;
String message;

void setup() {
  // put your setup code here, to run once:
  servo.attach(3);
  servo.attach(4);
  Wire.begin(4);
  Wire.onReceive(ServoEvent);
  Serial.begin(9600);
  updateServo1(0);
  updateServo2(0);
}


void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}

void ServoEvent(int howMany){
    
    while( 1 <= Wire.available() ){ // loop through all bytes but the last
      char c = Wire.read();
      Serial.println(c);
      message += c;
      
      //updateServo(c);
    }
    Serial.println(message);
    message = "";
  }

void updateServo1(int position){
    servo.write(position);
  }

void updateServo2(int position){
  
  }

void unpackMessage(String MSG, int *arr){
  

  }
