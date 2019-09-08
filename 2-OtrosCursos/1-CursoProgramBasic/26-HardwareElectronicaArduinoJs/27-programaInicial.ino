int amarillo = 8;
int rojo = 12;
int milisegundos = 100;

void setup() {
  pinMode(amarillo, OUTPUT);
  pinMode(rojo , OUTPUT);
  Serial.begin(9600);  

}

void loop() {
  digitalWrite(amarillo, HIGH);
  delay(milisegundos);
  digitalWrite(amarillo, LOW);
  delay(milisegundos);

  digitalWrite(rojo, HIGH);
  delay(milisegundos);
  digitalWrite(rojo, LOW);
  delay(milisegundos);
}