#import os, winshell
#import speech_recognition as sr
#import Functions
#from gtts import gTTS

## Воспроизведение речи
#import pygame
#from pygame import mixer
#try:
#    mixer.init()
#except pygame.error:
#    print("Аудио девайс не опознан");

#import os
#import sys
#import time
#import datetime
#import logging
#import webbrowser
#import subprocess
#import sqlite3

#class Functions():
#    def InsertAdress():
#        print("Скаижите адрес ( пример : 'Сатпаева 25 это дом' )")
#        with self._microphone as source:
#            audio = self._recognizer.listen(source)

#            adres = statement[0:statement.find("это")]
#            name = statement[statement.find("это") : statement.length]

#            con.create_aggregate("name", 1, name)
#            con.create_aggregate("adres", 2, adres)

#            c.execute("insert into adreses(?,?) values(1,2)")

#    def InsertEvent():
#        print("Скажите дату и имя мероприятия (пример: 'день рождение Димы дата 20 3 2019')")
#        with self._microphone as source:
#            audio = self._recognizer.listen(source)

#            event = statement[0:statement.find("дата")]
#            name = statement[statement.find("дата") : statement.length]

#            con.create_aggregate("name", 1, name)
#            con.create_aggregate("event", 2, event)

#            c.execute("insert into adreses(?,?) values(1,2)")

#    def WriteFile():
#        print("Скажите чтох записать в блокнот: ")
#        with self._microphone as source:
#            audio = self._recognizer.listen(source)
             
#            desktop = winshell.desktop()
#            path = os.path.join(desktop, "Твоя запись.txt")            
            
#            shortcut = file(path, 'w') # это из версии 2.х
#            shortcut.write(statment)
#            shortcut.close()

