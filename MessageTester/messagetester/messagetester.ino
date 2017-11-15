#include <SoftwareSerial.h>
SoftwareSerial BTSerial = SoftwareSerial(10, 11); // RX | TX

char data[20];

  
void setup() {
  Serial.begin(115200);  //initial the Serial with 115200 speed

}

void emptyData(){
  for (int x=0;x<20;x++){
    data[x] = '\0';
  }
}

void retrieveDataRx() {
  emptyData();
  if(Serial.available()) {
    Serial.readBytes(data,20);  // retrieve the 20 characters max received
    Serial.println(data);
    
  }
}

/**
 * Compare the data with the expected value
 */
bool compareDataRx(const char * value){
  if (strcmp(data, value) == 0){
    Serial.println(value);
    return true;
  }
  return false;
}
  
void loop() {
  data[0]='h';
  data[1]='e';
  data[2]='l';
  data[3]='l';
  Serial.write(data);
}



