# Plant Pot Pi
A smart plant pot computer system for analysing, tracking, and reacting to abiotic stress factors affecting house plants.

The project began as the coursework element of my OCR Computer Science A-level which I completed in 2019. I was awarded an A for my combined efforts in coursework as well as exams. I have published the project in the exact state it was submitted as for the non-examined assessment (NEA) within [this folder](nea). I've done this to give current CompSci A-level students some inspiration for their projects, the written documentation accompanying the project will be released soon.

## Getting started
### Prerequisites
Below is the hardware used to develop the project, other hardware could probably be used with some slight adjustments to the project.
+ Raspberry Pi 3 (RPi)
+ Arduino MKR1000
+ Micro-USB cable (capable of data/charging)
+ AM2320 temperature & humidity sensor
+ SparkFun soil moisture sensor
+ Mini breadboard
### Deployment
WIP.
### Built With
#### Python libaries
+ **pySerial:** serial communication via micro-USB between the RPi and Arduino
+ **csv:** environmental data is stored as CSV
+ **smtplib:** to send automatic emails using MIME format
#### Arduino (C++) libaries
+ **Adafruit_Sensor:** unified driver for Adafruit sensors (possibly not needed)
+ **Adafruit_AM2320:** driver specifically for the AM2320 sensor used
#### JavaScript
+ **Chart.js:** used to plot graphs on local website
+ **jQuery:** used to read/update environmental data from the CSV file
#### Others
+ **Apache:** used to run the local webserver on the RPi
