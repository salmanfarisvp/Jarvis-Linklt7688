#include <DHT.h>

#define DHTPIN A1  // DHTT pin connected to A1
#define DHTTYPE DHT11   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE);  // Initialize DHT sensor 


int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup() { 
          
          dht.begin();  //begin the DHTT
          
          Serial.begin(115200);  // open serial connection to USB Serial 
                                 //port(connected to your computer)
          Serial1.begin(57600);  // open internal serial connection to 
                                 //MT7688

          pinMode(13, OUTPUT); // Bedroom light
          pinMode(12,OUTPUT);  // kitchen light  
          
      }
      void loop() { 
         hum = dht.readHumidity();   // read humdity
         temp= dht.readTemperature();  //read temperature
         
            int c = Serial1.read();      // read from MT7688
            if (c != -1) {
                  switch(c) { 
                        case '0':                // turn off D13 when receiving "0"
                        digitalWrite(13, 0); 
                        break; 
                        case '1':                // turn on D13 when receiving "1" 
                        digitalWrite(13, 1); 
                        break; 
                        case '2':                // turn off D12 when receiving "1" 
                        digitalWrite(12,0);
                        break;
                        case '3':                // turn on D12 when receiving "1" 
                        digitalWrite(12,1);
                        break;
                        case '4':               // print temperature when receiving "4"
                        Serial1.print(hum);
                        break;
                        case '5':               //print humidity when receiving "5"
                        Serial1.print(temp);
                        break;
                        
                        
                        
                       
                  } 
            } 
      }
