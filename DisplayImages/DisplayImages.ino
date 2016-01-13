/*
  DisplayImages.ino
  
  Author:Eduardo
  2016-1-8

  UVC demo.

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include <Wire.h>
#include "rgb_lcd.h"
#include "NewPing.h"
#include "NewTone.h"

// Sketch to upload pictures to Dropbox when motion is detected
#include <Bridge.h>
#include <Process.h>

rgb_lcd lcd;
char message[] = "Put message here";

//#include <stdlib.h>       // calloc
//#include <stdarg.h>       // va_*
//#include <string.h>       // strlen, strcpy

//////////
//BUZZER//
//////////
int speakerPin = 8;                 // Grove Buzzer connect to D3
int length = 15;                    // the number of notes
//char notes[] = "ccggaagffeeddc "; // a space represents a rest
char notes[] = "cdec";              // a space represents a rest
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

///////////////
//Temperature//
///////////////
const int pinTemp = A0;             // pin of temperature sensor
int B=3975;                         // B value of the thermistor
float temperature;
float resistance;

/////////
//Sound//
///////// When sound larger than a certain value, led will on
const int pinSound = A1;            // pin of Sound Sensor
const int pinLedSound   = 7;        // pin of LED
int thresholdValueSound = 800;      // the threshold to turn on or off the LED

/////////
//Light//
/////////
// when the value of light sensor ledd than a certain value
// led will on, you can set this certain value via change thresholdvalue
// such as when you cover light sensor with your hand, you'll find led on
const int pinLight = A2;
const int pinLedLight   = 7;
int thresholdvalue=400;             //the threshold to turn on or off the LED

/////////////////////
//Ultrasonic Sensor//
/////////////////////
#define TRIGGER_PIN  12             // PIN tied to trigger on the ultrasonic sensor.
#define ECHO_PIN     11             // PIN tied to echo on the ultrasonic sensor.
#define MAX_DISTANCE 200            // Maximum distance we want to ping for (cms) Max distance rated at 400-500cm
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

/////////////////
//Camera Device//
///////////////// 
Process picture;
String filenamePhoto;             // Filename
String pathPhoto = "/arduino/";                // Path (Typically /mnt/sda1/ if you have SD Card)


void setup() {
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);

    // Bridge
    Bridge.begin();
  
    // initialize the serial communications:
    Serial.begin(9600);

    // Led to highlight
    pinMode(pinLedLight, OUTPUT);
    
    // Print a message to the LCD.
    //lcd.print(message);//not right now...

    //Grove Buzzer 
    pinMode(speakerPin, OUTPUT); // we want to make some noise
}

void loop() {
    // Turn off the display:
    //lcd.noDisplay();
    //delay(1000);
    // Turn on the display:
    lcd.display();
    //delay(1000);

    //METHODS
    //Print 0 to 9
    //autoScroll();
    //blink
    //blink();
    //cursors
    //cursor();
    //custom chars
    //customChars();

  ///////////////    
  //Temperature//
  ///////////////
  int val = analogRead(pinTemp);                               // get analog value
  resistance=(float)(1023-val)*10000/val;                      // get resistance
  temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;     // calc temperature
  String tempMessage = "Temp: ";
  tempMessage += temperature;
  Serial.print(tempMessage);
  lcd.clear();
  lcd.print(tempMessage);
  delay(1000);
    
  /*///////
  //SOUND//
  /////////
  int sensorSoundValue = analogRead(pinSound);   //read the sensorValue on Analog 0
  if(sensorSoundValue>thresholdValueSound)
  {
    digitalWrite(pinLedSound,HIGH);
    delay(200);
    digitalWrite(pinLedSound,LOW);
    emitBuzzerSound();
    String soundMessage = "Sound: ";
    soundMessage += sensorSoundValue;
    lcd.print(soundMessage);
    delay(3000);
    lcd.clear();
  }
  */
  
  /////////
  //LIGHT//
  /*///////
  int sensorValueLight = analogRead(pinLight);    //the light sensor is attached to analog 0
  if(sensorValueLight < thresholdvalue)
  {
    digitalWrite(pinLedLight, HIGH);
    String lightMessage = "Light: ";
    lightMessage += sensorValueLight;
    lcd.print(lightMessage);
    delay(3000);
    lcd.clear();
  }else{
    digitalWrite(pinLedLight, LOW);
  }
  */

  /////////////////////
  //Ultrasonic Sensor//
  /////////////////////  
  delay(50);  // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  int distance = sonar.ping_cm(); // Send ping, get ping time in microseconds (uS).
  Serial.print("Ping: ");
  Serial.print(distance); // Convert ping time to distance in cm and print result (0 = outside set distance range)
  Serial.println("cm");
  if (distance < 15)
  {
    digitalWrite(7, HIGH);
    delay(distance*10);
    digitalWrite(7, LOW);
    delay(distance*10);
    //emitBuzzerSoundProximity();
    
    String distanceMessage = "Distance: ";
    distanceMessage += distance;
    lcd.clear();
    lcd.print(distanceMessage);
    delay(1500);
    //Camera Device//
    lcd.clear();
    lcd.print("Taking Photograph");
    delay(1500);
    takePicture();
    //emitBuzzerSound();
  }  

}////Loop

//Helper methods for each Sensor/functionality
void playTone(int tone, int duration) {
    for (long i = 0; i < duration * 1000L; i += tone * 2) {
        digitalWrite(speakerPin, HIGH);
        delayMicroseconds(tone);
        digitalWrite(speakerPin, LOW);
        delayMicroseconds(tone);
    }
}

void playNote(char note, int duration) {
    char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
    int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

    // play the tone corresponding to the note name
    for (int i = 0; i < 8; i++) {
        if (names[i] == note) {
            playTone(tones[i], duration);
        }
    }
}

void autoScroll()
{
  
    // set the cursor to (0,0):
    lcd.setCursor(0, 0);
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++)
    {
        lcd.print(thisChar);
        delay(500);
    }

    // set the cursor to (16,1):
    lcd.setCursor(16,1);
    // set the display to automatically scroll:
    lcd.autoscroll();
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++)
    {
        lcd.print(thisChar);
        delay(500);
    }
    // turn off automatic scrolling
    lcd.noAutoscroll();

    // clear screen for the next loop:
    lcd.clear();
}

void blink()
{
    // Turn off the blinking cursor:
    lcd.noBlink();
    delay(3000);
    // Turn on the blinking cursor:
    lcd.blink();
    delay(3000);  
}

void cursor() {
    // Turn off the cursor:
    lcd.noCursor();
    delay(500);
    // Turn on the cursor:
    lcd.cursor();
    delay(500);
}

void customChars() 
{
    // read the potentiometer on A0:
    int sensorReading = analogRead(A0);
    // map the result to 200 - 1000:
    int delayTime = map(sensorReading, 0, 1023, 200, 1000);
    // set the cursor to the bottom row, 5th position:
    lcd.setCursor(4, 1);
    // draw the little man, arms down:
    lcd.write(3);
    delay(delayTime);
    lcd.setCursor(4, 1);
    // draw him arms up:
    lcd.write(4);
    delay(delayTime);
}

void serialDisplay()
{
    // when characters arrive over the serial port...
    if (Serial.available()) 
    {
        // wait a bit for the entire message to arrive
        delay(100);
        // clear the screen
        lcd.clear();
        // read all the available characters
        while (Serial.available() > 0) 
        {
            // display each character to the LCD
            lcd.write(Serial.read());
        }
    }
}

void emitBuzzerSound()
{
  //Buzzer sounds
  for (int i = 0; i < length; i++) 
  {
        if (notes[i] == ' ')
        {
            delay(beats[i] * tempo); // rest
        }
        else
        {
            playNote(notes[i], beats[i] * tempo);
            //Serial.println("Playing Note: ");
            //Serial.println(notes[i]);
        }

        // pause between notes
        delay(tempo / 2);
  }
}

void emitBuzzerSoundProximity(){
  
  // Melody (liberated from the toneMelody Arduino example sketch by Tom Igoe).
  int melody[] = { 262, 196, 196, 220, 196, 0, 247, 262 };
  int noteDurations[] = { 4, 8, 8, 4, 4, 4, 4, 4 };

  for (unsigned long freq = 125; freq <= 15000; freq += 10) {  
    NewTone(speakerPin, freq); // Play the frequency (125 Hz to 15 kHz sweep in 10 Hz steps).
    delay(1); // Wait 1 ms so you can hear it.
  }
  noNewTone(speakerPin); // Turn off the tone.

  delay(500); // Wait a second.

  for (int thisNote = 0; thisNote < 8; thisNote++) { // Loop through the notes in the array.
    int noteDuration = 5000/noteDurations[thisNote];
    NewTone(speakerPin, melody[thisNote], noteDuration); // Play thisNote for noteDuration.
    delay(noteDuration * 4 / 3); // Wait while the tone plays in the background, plus another 33% delay between notes.
  }

  while(1); // Stop (so it doesn't repeat forever driving you crazy--you're welcome).  
}

void takePicture()
{
    // Generate filename with timestamp
    filenamePhoto = "image_";
    picture.runShellCommand("date");
    while(picture.running());

    while (picture.available()>0) {
      char c = picture.read();
      filenamePhoto += c;
    } 
    filenamePhoto.trim();
    filenamePhoto.replace(" ", "_");
    filenamePhoto += ".png";
 
    // Take picture
    picture.runShellCommand("fswebcam " + pathPhoto + filenamePhoto + " -r 1280x720");
    while(picture.running());

    lcd.clear();
    lcd.print("Photograph taken!");
    delay(1500);

    // Invoke Python script: 
    picture.runShellCommand("python " + pathPhoto + "upload_ftp.py " + pathPhoto + filenamePhoto);
    Serial.println("python " + pathPhoto + "upload_ftp.py " + pathPhoto + filenamePhoto);
    delay(1000);
    Serial.print("Uploading to server: ");
    Serial.print(pathPhoto);
    Serial.print(filenamePhoto);

    while(picture.running());  
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
