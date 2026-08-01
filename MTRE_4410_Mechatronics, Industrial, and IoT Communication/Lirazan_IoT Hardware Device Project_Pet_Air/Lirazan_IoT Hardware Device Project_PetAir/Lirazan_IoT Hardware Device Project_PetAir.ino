#include "arduino_secrets.h"
/*
Class: MTRE 4410
Section: W01
Term: Summer 2026
Instructor: Razvan Voicu
Name: Christine Marie Lirazan
Project: IoT Hardware Device 
*/

#include "thingProperties.h"
#include <DHT.h>
#include <WiFi.h>


// Function: Define sensor inputs and actuator outputs used by the PetAir system.

// Requirement: Device integrates provided sensors (analog light sensor, digital buttons) or additional sensors effectively.
// Requirement: Successfully actuates provided (LED) or additional devices (motors, buzzers, servos, etc.).

#define FLAME_PIN 18
#define DHT_PIN 5

#define BUZZER_PIN 23

#define RED_LED_PIN   0
#define GREEN_LED_PIN 2
#define BLUE_LED_PIN  14

#define MOTOR_IN1 16
#define MOTOR_IN2 17


#define DHT_TYPE DHT11
DHT dht11(DHT_PIN, DHT_TYPE);


// Function: Declare functions used for LED control and fan operation.

void setColor(int red, int green, int blue);
void fanOn();
void fanOff();



void setup() {


  // Function: Initialize serial communication and display device startup information.

  Serial.begin(115200);
  delay(1500);


  Serial.println();
  Serial.println("∘₊✧────── ૮(• ﻌ •)ა ──────✧₊∘");
  Serial.println("          JOJO'S PETAIR");
  Serial.println("       Air Safety Monitor");
  Serial.println("∘₊✧────────────────✧₊∘");
  Serial.println();



  // Function: Start the DHT sensor and configure hardware pins.

  dht11.begin();


  pinMode(FLAME_PIN, INPUT);

  pinMode(BUZZER_PIN, OUTPUT);

  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(BLUE_LED_PIN, OUTPUT);

  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);



  // Function: Set actuators to a safe initial state.

  fanOff();

  digitalWrite(BUZZER_PIN, LOW);



  // Function: Connect the ESP32 device to Arduino IoT Cloud for remote monitoring and control.

  // Requirement: Successfully implements reliable wireless communication (Wi-Fi or similar).

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);


  setDebugMessageLevel(2);

  ArduinoCloud.printDebugInfo();


  Serial.println("Connecting to Arduino IoT Cloud...");



  while (!ArduinoCloud.connected()) {

    ArduinoCloud.update();

    delay(500);

    Serial.print(".");

  }



  Serial.println();

  Serial.println("Arduino IoT Cloud Connected!");

  Serial.println();



  // Function: Set default system operating modes after connection.

  autoMode = true;

  fanControl = false;

  alarmControl = false;

  safetyStatus = false;



  ArduinoCloud.update();



  // Function: Indicate startup status using the RGB LED.

  setColor(0, 0, 255);

  delay(1500);

  setColor(0, 255, 0);



  Serial.println("∘₊✧────── ૮(• ﻌ •)ა ──────✧₊∘");
  Serial.println("       Jojo's PetAir Ready!");
  Serial.println("       Auto Mode : ON");
  Serial.println("       Fan       : OFF");
  Serial.println("       Alarm     : OFF");
  Serial.println("∘₊✧────────────────✧₊∘");
  Serial.println();

}

void loop() {


  // Function: Update Arduino IoT Cloud communication and synchronize device variables.

  ArduinoCloud.update();



  // Function: Read temperature and humidity sensor data.

  // Requirement: Sensor data is accurately captured and effectively utilized in device logic.

  temperature = dht11.readTemperature(true);

  humidity = dht11.readHumidity();



  if (isnan(temperature) || isnan(humidity)) {

    Serial.println("ERROR: Failed to read DHT11!");

    delay(1000);

    return;

  }



  // Function: Read flame sensor input for fire detection.

  int flameState = digitalRead(FLAME_PIN);



  airQuality = 0;

  smokeLevel = 0;



  Serial.println();

  Serial.println("∘₊✧────── ૮(• ﻌ •)ა ──────✧₊∘");
  Serial.println("          JOJO'S PETAIR");
  Serial.println("∘₊✧────────────────✧₊∘");



  Serial.print("Temperature : ");

  Serial.print(temperature);

  Serial.println(" °F");



  Serial.print("Humidity    : ");

  Serial.print(humidity);

  Serial.println(" %");



  Serial.print("Flame       : ");

  Serial.println(flameState == LOW ? "DETECTED" : "SAFE");



  Serial.print("Auto Mode   : ");

  Serial.println(autoMode ? "ON" : "OFF");



  Serial.print("Fan Control : ");

  Serial.println(fanControl ? "ON" : "OFF");



  Serial.println();



  // Function: Detect fire conditions and activate the safety response.

  // Requirement: Demonstrates meaningful and consistent data processing and reaction based on sensed input.

  if (flameState == LOW) {


    safetyStatus = true;

    alarmControl = true;



    setColor(255, 0, 0);

    digitalWrite(BUZZER_PIN, HIGH);


    Serial.println("∘₊✧────── FIRE ALERT ──────✧₊∘");

    Serial.println("STATUS: FIRE DETECTED!");

    Serial.println("Alarm: ON");



  } else {


    safetyStatus = false;


    setColor(0, 255, 0);



    if (!alarmControl) {

      digitalWrite(BUZZER_PIN, LOW);

    }



    Serial.println("∘₊✧────── STATUS ──────✧₊∘");

    Serial.println("STATUS: SAFE");


  }



  Serial.println();



  // Function: Control fan operation using temperature conditions or dashboard commands.

  // Requirement: Actuators respond correctly and reliably to sensed input or remote commands.

  if (autoMode) {


    Serial.println("MODE: AUTOMATIC");



    if (temperature > 75.0) {


      fanOn();



      Serial.println("Fan: ON");

      Serial.println("Reason: Temperature above 75°F");



    } else {


      fanOff();



      Serial.println("Fan: OFF");

      Serial.println("Reason: Temperature below 75°F");


    }



  } else {



    Serial.println("MODE: MANUAL");



    if (fanControl) {


      fanOn();



      Serial.println("Fan: ON");

      Serial.println("Reason: Dashboard switch");



    } else {


      fanOff();



      Serial.println("Fan: OFF");

      Serial.println("Reason: Dashboard switch");


    }

  }



  Serial.println("∘₊✧────────────────✧₊∘");



  delay(1000);

}


// Function: Control RGB LED color output to indicate system status.

// Requirement: Successfully actuates provided (LED) or additional devices (motors, buzzers, servos, etc.).

void setColor(int red, int green, int blue) {

  analogWrite(RED_LED_PIN, red);

  analogWrite(GREEN_LED_PIN, green);

  analogWrite(BLUE_LED_PIN, blue);

}




// Function: Turn the fan motor on.

// Requirement: Successfully actuates provided (LED) or additional devices (motors, buzzers, servos, etc.).

void fanOn() {

  digitalWrite(MOTOR_IN1, HIGH);

  digitalWrite(MOTOR_IN2, LOW);

}




// Function: Turn the fan motor off.

// Requirement: Successfully actuates provided (LED) or additional devices (motors, buzzers, servos, etc.).

void fanOff() {

  digitalWrite(MOTOR_IN1, LOW);

  digitalWrite(MOTOR_IN2, LOW);

}




// Function: Update buzzer operation when alarm control is changed from the dashboard.

// Requirement: Actuators respond correctly and reliably to sensed input or remote commands.

void onAlarmControlChange() {

  Serial.print(">>> Alarm Control changed to: ");

  Serial.println(alarmControl ? "ON" : "OFF");


  digitalWrite(BUZZER_PIN, alarmControl ? HIGH : LOW);

}




// Function: Update manual fan operation when fan control is changed from the dashboard.

// Requirement: Actuators respond correctly and reliably to sensed input or remote commands.

void onFanControlChange() {

  Serial.print(">>> Fan Control changed to: ");

  Serial.println(fanControl ? "ON" : "OFF");



  if (!autoMode) {


    if (fanControl) {


      fanOn();

      Serial.println(">>> Manual Fan: ON");



    } else {


      fanOff();

      Serial.println(">>> Manual Fan: OFF");


    }

  }

}




// Function: Switch between automatic temperature control and manual dashboard control.

void onAutoModeChange() {

  Serial.print(">>> Auto Mode changed to: ");

  Serial.println(autoMode ? "ON" : "OFF");



  if (autoMode) {


    Serial.println(">>> Automatic temperature control enabled");


  } 
  else {


    Serial.println(">>> Manual fan control enabled");


  }

}