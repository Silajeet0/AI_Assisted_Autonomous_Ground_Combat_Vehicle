#include <WiFi.h>
#include <WiFiUdp.h>

char* ssid = "wifi name"; // Change this to your Wi-Fi network name
const char* password = "password"; // Change this to your Wi-Fi password
unsigned int localPort = 1234; // Change this to the port number you want to listen on

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  delay(10);

  Serial.println();
  Serial.println("Connecting to WiFi");

  WiFi.begin((char*)ssid, password); // Typecast ssid to char*

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  udp.begin(localPort); // Start UDP communication on the specified port
}

void loop() {
  // Check if data has been received
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Read received data into a buffer
    char packetBuffer[255]; // Adjust the buffer size according to your data
    udp.read(packetBuffer, packetSize);
    packetBuffer[packetSize] = '\0'; // Null-terminate the string
    
    // Print received data
    Serial.print("Received packet: ");
    Serial.println(packetBuffer);
  }

  delay(10); // Add a small delay to prevent flooding the serial port
}
