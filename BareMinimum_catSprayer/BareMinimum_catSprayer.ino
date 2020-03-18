int PIRpin = 6;
int MOTORpin = 7;


void setup() {
  // put your setup code here, to run once:
  pinMode(PIRpin, INPUT);
  pinMode(MOTORpin, OUTPUT);
  digitalWrite(MOTORpin, LOW);
  delay(20000);
}

void loop() {
  // put your main code here, to run repeatedly:

  while(digitalRead(PIRpin)){      
      spray();
  }
  noSpray();
}

void spray(){
  digitalWrite(MOTORpin, HIGH);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2500);
  noSpray();
  delay(5000);
  }

void noSpray(){
  digitalWrite(MOTORpin, LOW);
  digitalWrite(LED_BUILTIN, LOW);
  }

  
