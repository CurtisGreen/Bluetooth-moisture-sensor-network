#include "LowPower.h"
#include <SoftwareSerial.h>

int sensor_pin = A0; 
int output_value;
int inByte = 0;


void setup() {
  Serial.begin(9600);
  Serial.println("Reading From the Sensor ...");
  delay(2000);
  }

void loop() {
  if (Serial.available()){  
    for(int i = 0; i<15; i++)
    {
    output_value= analogRead(sensor_pin);
    Serial.print("Mositure : ");
    Serial.println(output_value);
    Serial.write(output_value);
    delay(1000);
     for(int j = 0; j<5400; j++)
     {
      LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
     }
    }
  }
}


