/*Reads temperature, humidity, and soil moisture, includes Wi-Fi capabilities*/

#include "Adafruit_Sensor.h" 
/*Unified Adafruit sensor library, for the temperature and humidity sensor*/
#include "Adafruit_AM2320.h"
/*Specific library for the temperature and humidity sensor*/
#include "WiFi101.h" 
/*Library for the built-in WiFi chip and shield, needed for LAN*/

Adafruit_AM2320 am2320 = Adafruit_AM2320(); 
/*Shortens the AM2320 sensor function call*/
int wifi_status = WL_IDLE_STATUS;
/*Assigns variable a tempory status given until the counter below expires*/
int wifi_counter = 0;
/*Instantiates counter for Wi-Fi connection attempts*/

void setup() {
/*One-time called startup function*/
  Serial.begin(9600);
/*Sets standard baud rate for reading from Serial*/
  while (!Serial) {
/*While not transmitting over Serial impose a 1 second delay*/
    delay(1000);
  }
  
  Serial.println("Welcome to PlantPotPi! At the moment there is support for Temperature (°C), Humidity (%), and Soil Moisture.");
 /*Output title and purpose of script to Serial, for testing*/
  Serial.println("Attempting to connect to WPA2 secured Wifi network.");
 /*Informs user attempt to connect to LAN*/
  
  while (wifi_status != WL_CONNECTED) {
 /*Check to see if connected to LAN*/
    if (wifi_counter > 3) {
 /*Prevents continuous connection attempts if it's tried over 3 times*/
      Serial.println("Cannot connect to the Wifi network!");
 /*Informs user the Arduino cannot connect to LAN*/
      break;
 /*Skips attempts to connec to LAN*/
    }
    wifi_status = WiFi.begin("VM9850065", "mbkf8KqPhjjFIVE");
 /*Call WiFi connection function, with arguments of LAN details*/
    Serial.println("Connecting now, waiting 5 seconds for connection...");
 /*Inform user that WiFi connection is being attempt*/
    wifi_counter ++; 
 /*Increment counter after the attempt to connect to LAN*/
    delay(5000);
 /*Wait 5 seconds before attempting to connect again*/
  }
  
  Serial.print("Now connected, your local IP address is: ");Serial.println(WiFi.localIP());
 /*Output local IP to ensure connected on correct LAN, for testing*/
  pinMode(0, OUTPUT); 
 /*Sets 0th pin as an output, for soil moisture sensor*/
  digitalWrite(0, LOW); 
 /*Sets 0th pin to off, prevent powering moisture sensor*/
  am2320.begin();
 /*Call temperature and humidity sensor to connect via I2C*/
}

int temperature() {
/*Function to read temperature from AM2320 sensor and return value*/
  int current_temperature = am2320.readTemperature();
/*Save temperature gathered from sensor as variable*/
  return current_temperature;
/*Return saved temperature variable from wherever it is called*/
}

int humidity() {
/*Function to read humidity from sensor and return value*/
  int relative_humidity = am2320.readHumidity();
/*Define variable as integer for the humidity from AM2320 sensor*/
  return relative_humidity;
/*Return saved humidity variable from wherever it is called*/
}

int moisture() {
  digitalWrite(0, HIGH); 
/*Sets 0th pin on, powering soil moisture sensor*/
  delay(10);
/*Allow 0.1 seconds for sensor to power on*/
  int soil_moisture = analogRead(A0); 
/*Reads value from A0 pin which is humidity data*/
  digitalWrite(0, LOW);
/*Turns 0th pin off, turning off moisture sensor*/
  return soil_moisture;
/*Returned read humdidity integer from wherever it is called*/
}
