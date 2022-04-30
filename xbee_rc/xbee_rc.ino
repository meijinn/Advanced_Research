#include <Servo.h>
Servo servo;
Servo speedcontroller;

int steering=89; //= servoneutral;
int vel=96; //= speedcontrollerneutral;

const int val_size=2;
int values[val_size] = {0,0};
bool isValids[val_size] = {false,false};

void setup() {
  Serial.begin(115200);
  servo.attach(10);
  speedcontroller.attach(6);
}

void loop() {
  if(Serial.available()>=7){
    int head = Serial.read();
    if(head==128){
      bool isValids[val_size] = {false,false};
    }
    for(int i=0;i<val_size;i++){
      if(head==128+i){
        int high = Serial.read();
        int low = Serial.read();
        values[i] = (high<<5)+low;
      }
    }
  }
  steering = values[0];
  vel = values[1];
  servo.write(steering);
  speedcontroller.write(vel);
  Serial.println(values[0]);
  Serial.println(values[1]);
}
