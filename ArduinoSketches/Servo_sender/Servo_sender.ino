
#include <Wire.h>


void setup() {
  // put your setup code here, to run once:
  Wire.begin();
}
byte send = 0;

void loop() {
  // put your main code here, to run repeatedly:
  updatePosition(0);
  delay(1000);
  updatePosition(90);
  delay(1000);
  updatePosition(180);
  delay(1000);
}

void updatePosition(int position){
    //servo.write(position);
    Wire.beginTransmission(4);
    Wire.write(position);
    Wire.endTransmission();
  }
