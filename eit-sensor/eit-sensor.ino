#include <ArduinoJson.h>
#include <Udp.h>
#include <TelenorNBIoT.h>
#include <Wire.h>   // I2C library
#include "iAQcore.h"
#include <SoftwareSerial.h>

SoftwareSerial ublox(10, 11);
/*
 * Create an nbiot instance using default settings, which is the Telenor NB-IoT
 * Development Platform's APN (mda.ee) and 0 for both mobile country code and
 * mobile operator code (auto mode).
 * 
 * It's also possible to specify a different APN, mobile country code and
 * mobile network code. This should speed up attaching to the network.
 * 
 * Example:
 * TelenorNBIoT nbiot("mda.ee", 242, 01); // Telenor Norway
 * 
 * See list of codes here: https://www.mcc-mnc.com/
 */
TelenorNBIoT nbiot;

IPAddress remoteIP(172, 16, 15, 14);
int REMOTE_PORT = 1234;

iAQcore iaqcore;

bool sensorWarm = false;
const int ledPin = 3;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  ublox.begin(9600);
  
  Serial.print("Connecting to NB-IoT module...\n");
  bool hasBegun = nbiot.begin(ublox);
  while (!hasBegun) {
    Serial.println("Begin failed. Retrying...");
    hasBegun = nbiot.begin(ublox);
    delay(1000);
  }

  while (!nbiot.createSocket()) {
    Serial.print("Error creating socket. Error code: ");
    Serial.println(nbiot.errorCode(), DEC);
    delay(100);
  }

  // Enable I2C for Arduino pro mini or Nano [VDD to VCC/3V3, GND to GND, SDA to A4, SCL to A5]
  Wire.begin();

  // Enable iAQ-Core
  iaqcore.begin();
}

void loop() {
  if (nbiot.isConnected()) {
    uint16_t eco2;
    uint16_t stat;
    uint32_t resist;
    uint16_t etvoc;
    iaqcore.read(&eco2,&stat,&resist,&etvoc);

    if (stat != 0x00) {
      Serial.print("Status: 0x"); Serial.println(stat, HEX);
      delay(5000);
      return;
    }

    sensorWarm = true;
    digitalWrite(ledPin, LOW);

    const int capacity = JSON_OBJECT_SIZE(2);
    StaticJsonDocument<capacity> doc;
    doc["co2"] = eco2;
    doc["tvoc"] = etvoc;

    String output = "";
    serializeJson(doc, output);

    // Send message to remote server
    Serial.println(output);
    nbiot.sendString(remoteIP, REMOTE_PORT, output);
    /*if (true == nbiot.sendString(remoteIP, REMOTE_PORT, "Hello, this is Arduino calling")) {
      Serial.println("Successfully sent data");
    } else {
      Serial.println("Failed sending data");
    }*/

    delay(60 * 1000);
  } else {
    // Not connected yet. Wait 5 seconds before retrying.
    Serial.println("Connecting...");
    delay(5000);
  }
}


