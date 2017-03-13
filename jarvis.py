#coder :- Salman Faris
import sys
import mraa
import time
import random
import datetime
import telepot
import serial 


 
s= None

def setup():
    global s
    s = serial.Serial("/dev/ttyS0", 57600)
    

 

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    
    
    if command =='/start':
       bot.sendMessage(chat_id,"Hi, Am Jarvis Your Personal Assistant Powerd by Linit7688 Duo developed by Salman Faris. ")
       bot.sendMessage(chat_id,"Am here to help You...! ")
       bot.sendMessage(chat_id,"to know more about my command type /help")
    elif command == '/help':
        bot.sendMessage(chat_id,"/TurnOnBedroomLight or /TurnOffBedroomLight :- to turn on/off bedroom light")
        bot.sendMessage(chat_id,"/TurnOnKitchenLight or /TurnOffKitchenLight :- to turn on/off Kitchen light")
        bot.sendMessage(chat_id,"/TurnOnLights or /TurnOffLights :- to turn on/off all the light")
        bot.sendMessage(chat_id,"/RoomTemp :- To know about Room Temperature ")
        bot.sendMessage(chat_id,"/RoomHumi :- To know about Room Humidity ")
        bot.sendMessage(chat_id,"/News :- To read Latest News ")
        s.write("1")
    elif command == '/TurnOnBedroomLight':
        bot.sendMessage(chat_id,"ok..Bedroom light now ON")
        s.write("1")
    elif command =='/TurnOffBedroomLight':
         bot.sendMessage(chat_id,"ok...Bedroom light now OFF")
         s.write("0")
    elif command == '/TurnOnKitchenLight':
         bot.sendMessage(chat_id,"ok...kitchen light now ON")
         s.write("3")
    elif command == '/TurnOffKitchenLight':
         bot.sendMessage(chat_id,"ok...kitchen light now OFF")
         s.write("2")
    elif command == '/TurnOnLights':
         bot.sendMessage(chat_id,"bedroom and kitchen light's are On")
         s.write("1")
         s.write("3")
    elif command == '/TurnOffLights':
         bot.sendMessage(chat_id,"bedroom and kitchen light's are On")
         s.write("0")
         s.write("2")
    elif command == '/RoomTemp':
         bot.sendMessage(chat_id,"Temperature is")
         s.write("5")
         a = s.read(5)
         bot.sendMessage(chat_id,a)
         bot.sendMessage(chat_id,"Celsius")
    elif command == '/RoomHumi':
         bot.sendMessage(chat_id,"Humidity is ")
         s.write("4")
         a = s.read(5)
         bot.sendMessage(chat_id,a)
    elif command == '/News':
         bot.sendMessage(chat_id,"http://www.bbc.com/news/world")
         bot.sendMessage(chat_id,"http://timesofindia.indiatimes.com/news")
         bot.sendMessage(chat_id,"http://www.ndtv.com/latest")
         
    else:
        bot.sendMessage(chat_id,"Wrong Command")
        bot.sendMessage(chat_id,"please check /help section to know more about Command's")



bot = telepot.Bot('bot token')
bot.message_loop(handle)
print 'I am listening...'

while True:
    setup()

    
    
    
    
    
        


