/*Reads temperature, humidity, and soil moisture*/
#include "Adafruit_Sensor.h"
/*Unified Adafruit sensor library, for the temperature and humidity sensor*/
#include "Adafruit_AM2320.h"
/*Specific library for the temperature and humidity sensor*/
Adafruit_AM2320 am2320 = Adafruit_AM2320();
/*Shortens the AM2320 sensor function call*/
void setup() {
  Serial.begin(9600);
/*Sets standard baud rate for reading from Serial*/
  while (!Serial) {
    delay(1000);
/*While not transmitting over Serial impose a 1 second delay*/
  }
  Serial.println("Welcome to PlantPotPi");
  pinMode(0, OUTPUT);
/*Sets pin 0 as an output, for soil moisture sensor*/
  digitalWrite(0, LOW);
/*Sets pin 0 to off, prevents powering the moisture sensor*/
  am2320.begin();
/*Calls temperature and humidity sensor to connect via I2C*/
}
void loop() {
  Serial.println(temperature());
  Serial.println(humidity());
  Serial.println(moisture());
/*Output returned values from functions to Serial*/
  delay(10000);
/*Imposes 10 second delay*/
}
int temperature() {
  int current_temperature = am2320.readTemperature();
/*Save temperature gathered from sensor as variable*/
  return current_temperature;
/*Return saved temperature variable to main loop*/
}
int humidity() {
  int relative_humidity = am2320.readHumidity();
/*Save humidity gathered from sensor as variable*/
  return relative_humidity;
/*Return saved humidity variable to main loop*/
}
int moisture() {
  digitalWrite(0, HIGH);
/*Turns sensor on by providing power to pin*/
  delay(10);
/*Allow 0.1 seconds for sensor to power on*/
  int soil_moisture = analogRead(A0);
/*Reads value from A0 pin which is humidity data*/
  digitalWrite(0, LOW);
/*Turns off moisture sensor*/
  int relative_moisture = map(soil_moisture,750,180,0,100);
/*Converts recieved value into actual percentage*/
  return relative_moisture;
}
