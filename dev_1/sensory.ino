/*Temperature & Humidity Reading*/

#include "Adafruit_Sensor.h"
/*Imports unified sensor library for all Adafruit sensors.*/
#include "Adafruit_AM2320.h"
/*Imports specific library for the temperature & humidity sensor*/

am2320 = Adafruit_AM2320();
/*Rebinds call function for the sensor to shorter variable*/

void setup() {
/*Function called on startup and only run once*/
  Serial.begin(9600);
/*Sets baud rate, important for Serial communication and testing*/
  Serial.println("Temperature and humidity control");
/*Outputs title of program to Serial for testing*/
  am2320.begin();
/*Calls the sensor function for use*/
}

void loop() {
/*Main function which is continually repeated*/
  Serial.print("Temperature: "); Serial.println(am2320.readTemperature());Serial.print("°C");
/*Prints label and then prints the return of the function call to read the temperature*/
  Serial.print("Relative humidity: "); Serial.println(am2320.readHumidity());Serial.print("%");
/*Print label and then prints return of the humidity reading function*/

  delay(2000);
/*Waits 2 seconds before looping to the begining of the function*/
}
