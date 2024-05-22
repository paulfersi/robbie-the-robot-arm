#include <WiFiS3.h> //library for the Arduino R4 Wifi
#include <WebServer.h>
#include <Servo.h>
#include "WiFiCredentials.h" 

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;
Servo wristServo;

const int basePin = 4;
const int shoulderPin = 5;
const int elbowPin = 6;
const int wristPin = 7;

WebServer server(80);

void setup()
{
    
    Serial.begin(115200);

    // Attach servos to pins
    baseServo.attach(basePin);
    shoulderServo.attach(shoulderPin);
    elbowServo.attach(elbowPin);
    wristServo.attach(wristPin);

    // Connect to WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("WiFi connected");
    Serial.println(WiFi.localIP());

    // Define routes
    server.on("/move", handleMove);
    server.begin();
    Serial.println("HTTP server started");
}

void handleMove()
{
    String joint = server.arg("joint");
    int angle = server.arg("angle").toInt();

    if (joint == "base")
    {
        baseServo.write(angle);
    }
    else if (joint == "shoulder")
    {
        shoulderServo.write(angle);
    }
    else if (joint == "elbow")
    {
        elbowServo.write(angle);
    }
    else if (joint == "wrist")
    {
        wristServo.write(angle);
    }
    server.send(200, "text/plain", "OK");
}

void loop()
{
    server.handleClient();
}
