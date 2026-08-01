/*
Class: EE 2501
Section: 07
Term: Spring 2026
Instructor: Matthew Abrams
Name: Christine Marie Lirazan
Final Project: Dual-Mode Soil Moisture-Based Irrigation Controller
*/

#define MANUAL_BUTTON 2 // Manual control button (user input)
#define MODE_BUTTON 3   // Mode toggle button (manual/auto selection)
#define RELAY_PIN 4     // Pump control output (actuator)

#define MANUAL_ACTION_LED 9 // Pump active indicator (manual mode action)
#define MANUAL_LED 10       // Manual mode indicator
#define AUTO_LED 11         // Auto mode indicator
#define GREEN_LED 12        // Wet soil indicator
#define RED_LED 13          // Dry soil indicator

#define SENSOR_PIN A0 // Resistance-based soil moisture sensor (analog input)

int threshold = 600; // Dry/wet decision point

bool manualMode = true;

// DEBOUNCE
// Requirement: Pass input through logic
// (removes button bounce)

bool buttonState = HIGH;
bool lastButtonReading = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

void setup() {

  // Requirement: Receive input from the outside world
  pinMode(MANUAL_BUTTON, INPUT_PULLUP);
  pinMode(MODE_BUTTON, INPUT_PULLUP);

  // Requirement: Produce output that depends on input
  pinMode(RELAY_PIN, OUTPUT);

  pinMode(MANUAL_ACTION_LED, OUTPUT);
  pinMode(MANUAL_LED, OUTPUT);
  pinMode(AUTO_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  // Requirement: Receive input from the outside world
  bool A = manualMode;
  bool B = (digitalRead(MANUAL_BUTTON) == LOW);
  bool M = (analogRead(SENSOR_PIN) >= threshold); // 1 = dry soil

  bool reading = digitalRead(MODE_BUTTON);

  // MODE CONTROL
  // Requirement: Pass input through logic

  if (reading != lastButtonReading) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {

    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == LOW) {
        manualMode = !manualMode;
        Serial.println(manualMode ? "MANUAL" : "AUTO");
      }
    }
  }

  lastButtonReading = reading;

  // BOOLEAN LOGIC
  // Requirement: Pass input through a system of at least four logic gates

  // Boolean variables:
  // A = manualMode
  // B = manual button (pressed = 1)
  // M = moisture sensor (1 = dry soil)

  // Boolean equation:
  // P = (A · B) + (A' · M)

  bool P = (A && B) || (!A && M);

  bool green = !M;
  bool red = M;

  bool manualLED = A;
  bool autoLED = !A;

  // OUTPUTS
  // Requirement: Produce output that depends on processed input

  digitalWrite(RELAY_PIN, !P);

  digitalWrite(MANUAL_ACTION_LED, B && A);

  digitalWrite(GREEN_LED, green);
  digitalWrite(RED_LED, red);

  digitalWrite(MANUAL_LED, manualLED);
  digitalWrite(AUTO_LED, autoLED);
}