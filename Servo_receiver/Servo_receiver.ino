
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
int arr[2];    
    while( 1 <= Wire.available() ){ // loop through all bytes but the last
      char c = Wire.read();
      Serial.println(c);
      message += c;
      
      //updateServo(c);
    }
    Serial.println(message);
    unpackMessage(message, arr);
    message = "";
  }

void updateServo1(int position){
    servo.write(position);
  }

void updateServo2(int position){
  
  }

void unpackMessage(String MSG, int arr[2]){
  //Split the incoming message up to the ',' comma delimiter, 
  //omitting the opening bracket
  // the toInt() function at the end stores this cropped string as an integer
  arr[0] = MSG.substring(1, MSG.indexOf(",") ).toInt();

  // Split the incoming message from the ',' comma delimiter UP to 
  // and omitting the closing bracket. 
  // the toInt() function at the end stores this cropped string as an integer
  arr[1] = MSG.substring(MSG.indexOf(",")+2, MSG.indexOf(")")).toInt();

Serial.print("index0:");
Serial.print(arr[0]+1);
Serial.print(" index1:");
Serial.println(arr[1]+1);
  }
