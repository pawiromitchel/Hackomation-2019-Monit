String command;

void setup() {
  Serial.begin(9600);
}

void loop() {
    command = Serial.readString();
    if(command == "boom") {
      Serial.println("Drone vliegt");
    }
}
