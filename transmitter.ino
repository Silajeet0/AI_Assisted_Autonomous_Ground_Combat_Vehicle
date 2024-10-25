#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
//const int joystickXPin = A0;
const int joystickXPin = 0;

const char* ssid = "Wifi name";
const char* password = "Password";
IPAddress receiverIP(192, 168, 0, 136); // Change this to the IP address of the receiver ESP8266
unsigned int receiverPort = 1234; // Change this to the port number of the receiver

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  delay(10);

  
  Serial.println();
  Serial.println("Connecting to WiFi");
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  udp.begin(1234); // Start UDP communication on port 1234
}

void loop() {
  // Read data from joystick X-axis
  //int joystickXValue = analogRead(joystickXPin);
  int joystickXValue = digitalRead(joystickXPin);
  
  // Send data
  udp.beginPacket(receiverIP, receiverPort);
  udp.print(joystickXValue);
  udp.endPacket();

  delay(10); // Wait for a short time before sending data again
}
