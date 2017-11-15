#include <SoftwareSerial.h>
SoftwareSerial BTSerial = SoftwareSerial(10, 11); // RX | TX

char data[20];

void setup() {
    Serial.begin(115200);               //initial the Serial
}

 
void loop(){
  delay(400);
  Serial.write("s003432");    //send what has been received
  Serial.write("s003432");
  Serial.write("s003432");
}
