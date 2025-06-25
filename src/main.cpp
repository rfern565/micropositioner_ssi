#include <Arduino.h>
#include <SPI.h>

const int CS_PIN = 4;

float kp = 0.5, ki = 0.0, kd = 0.0;
float integral = 0;
float lastError = 0;

void setup() {
  Serial.begin(115200);
  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);
  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE1));
}

int readSSI() {
  digitalWrite(CS_PIN, LOW);
  delayMicroseconds(1);
  uint8_t highByte = SPI.transfer(0x00);
  uint8_t lowByte  = SPI.transfer(0x00);
  digitalWrite(CS_PIN, HIGH);
  return ((highByte << 8) | lowByte) & 0x0FFF;
}

float ssiToMicrons(int ssiVal) {
  return (ssiVal / 4095.0) * 2000.0;
}

float computePID(float target, float current) {
  float error = target - current;
  integral += error;
  float derivative = error - lastError;
  lastError = error;
  float output = kp * error + ki * integral + kd * derivative;
  return constrain(output, 0, 4095);
}

void writeToActuator(int value) {
  Serial.print("Control Signal: ");
  Serial.println(value);
}

void controlLoop(float target_um) {
  int raw = readSSI();
  float current = ssiToMicrons(raw);
  float output = computePID(target_um, current);
  writeToActuator((int)output);

  Serial.print("Current Pos (um): ");
  Serial.print(current);
  Serial.print(" | Target: ");
  Serial.print(target_um);
  Serial.print(" | Output: ");
  Serial.println(output);    
}

unsigned long startTime = millis();

void loop() {
  float target_um = 1000.0;  // 1 mm target
  int raw = readSSI();
  float current = ssiToMicrons(raw);
  float output = computePID(target_um, current);

  writeToActuator((int)output);

  float elapsed = (millis() - startTime) / 1000.0;
  Serial.print(elapsed); Serial.print(",");
  Serial.print(current); Serial.print(",");
  Serial.print(target_um); Serial.print(",");
  Serial.println(output);

  delay(10);  // 100 Hz update rate
}

