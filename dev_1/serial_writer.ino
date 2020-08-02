/*Write simple integer to Serial*/

int a = 0
/*Instantiate variable as 0*/

void setup() {
/*One-time called function*/
  Serial.begin(9600);
/*Set baud to 9600, which is the normal*/
}

void loop() {
/*Looped main function*/
  a++;
/*Increment variable on every loop*/
  Serial.println(a);
/*Output variable to Serial*/
  delay(1000);
/*Wait 1 second before looping*/
}
