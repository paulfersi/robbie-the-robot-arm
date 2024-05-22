#include <Servo.h>

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;
Servo wristServo;

const int basePin = 4;
const int shoulderPin = 5;
const int elbowPin = 6;
const int wristPin = 7;

// Initial angles for each joint
int baseAngle = 80;
int shoulderAngle = 100;
int elbowAngle = 180;
int wristAngle = 90;

// Button pins
const int baseForwardButtonPin = 34;
const int baseBackwardButtonPin = 32;
const int shoulderUpButtonPin = 30;
const int shoulderDownButtonPin = 28;
const int elbowUpButtonPin = 26;
const int elbowDownButtonPin = 24;

void moveBase(int angle)
{
  baseServo.write(angle);
  baseAngle = angle;
  delay(20);
}

void moveShoulder(int angle)
{
  shoulderServo.write(angle);
  shoulderAngle = angle;
  delay(40);
}

void moveElbow(int angle)
{
  elbowServo.write(angle);
  elbowAngle = angle;
  delay(20);
}

void moveWrist(int angle)
{
  wristServo.write(angle);
  wristAngle = angle;
  delay(30);
}

void setup()
{
  baseServo.attach(basePin);
  elbowServo.attach(elbowPin);
  shoulderServo.attach(shoulderPin);

  pinMode(baseForwardButtonPin, INPUT_PULLUP);
  pinMode(baseBackwardButtonPin, INPUT_PULLUP);
  pinMode(shoulderUpButtonPin, INPUT_PULLUP);
  pinMode(shoulderDownButtonPin, INPUT_PULLUP);
  pinMode(elbowUpButtonPin, INPUT_PULLUP);
  pinMode(elbowDownButtonPin, INPUT_PULLUP);

  moveBase(baseAngle);
  moveElbow(elbowAngle);
  moveShoulder(shoulderAngle);
}

void loop()
{
  bool baseForwardButtonState = digitalRead(baseForwardButtonPin) == LOW;
  bool baseBackwardButtonState = digitalRead(baseBackwardButtonPin) == LOW;
  bool shoulderUpButtonState = digitalRead(shoulderUpButtonPin) == LOW;
  bool shoulderDownButtonState = digitalRead(shoulderDownButtonPin) == LOW;
  bool elbowUpButtonState = digitalRead(elbowUpButtonPin) == LOW;
  bool elbowDownButtonState = digitalRead(elbowDownButtonPin) == LOW;

  // Move base
  if (baseForwardButtonState && !baseBackwardButtonState)
  {
    baseAngle += 5;
    if (baseAngle > 180)
      baseAngle = 180;
    moveBase(baseAngle);
  }
  else if (!baseForwardButtonState && baseBackwardButtonState)
  {
    baseAngle -= 5;
    if (baseAngle < 0)
      baseAngle = 0;
    moveBase(baseAngle);
  }

  // Move shoulder
  if (shoulderUpButtonState && !shoulderDownButtonState)
  {
    shoulderAngle += 5;
    if (shoulderAngle > 180)
      shoulderAngle = 180;
    moveShoulder(shoulderAngle);
  }
  else if (!shoulderUpButtonState && shoulderDownButtonState)
  {
    shoulderAngle -= 5;
    if (shoulderAngle < 0)
      shoulderAngle = 0;
    moveShoulder(shoulderAngle);
  }

  // Move elbow
  if (elbowUpButtonState && !elbowDownButtonState)
  {
    elbowAngle += 5;
    if (elbowAngle > 180)
      elbowAngle = 180;
    moveElbow(elbowAngle);
  }
  else if (!elbowUpButtonState && elbowDownButtonState)
  {
    elbowAngle -= 5;
    if (elbowAngle < 0)
      elbowAngle = 0;
    moveElbow(elbowAngle);
  }
}
