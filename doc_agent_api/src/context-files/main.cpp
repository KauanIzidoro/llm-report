#include <DHTesp.h>
#include <WiFi.h>

#define WIFI_NAME "WIFI_ADM_CFP402"
#define WIFI_PASS "ac4ce0ss2"
#define pinOut 15


DHTesp dhtSensor;

void ConnectWifi()
{
  Serial.println("Connecting to Wifi...")
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attemps < 20)
  {
    WiFi.begin(WIFI_NAME, WIFI_PASS, 6);
    delay(500);
    Serial.print(".");
    attempts++;
  }
  if (WiFi.status() != WL_CONNECTED)
  {
    Serial.println("\nFailed to connect to WiFi.");
  } else
  {
    Serial.println("\nConnect to WiFi");
  }
}

void setup()
{
  Serial.begin(115200);
  Serial.println("ESP32 and DHT Sensor");
  dhtSensor.setup(pinOut, DHTesp::DHT22);
  ConnectWifi();
}


void loop()
{
  TempAndHumidity data = dhtSensor.getTempAndHumidity();
  float temp = data.temperature;
  int hum = data.humidity;

  Serial.println(temp);
  Serial.println(hum);
  delay(1000);
}