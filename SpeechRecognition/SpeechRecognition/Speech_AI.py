import speech_recognition as sr 
import random
import time

# Воспроизведение речи
import pygame
from pygame import mixer
try:
    mixer.init()
except pygame.error:
    print("Аудио девайс не опознан");

import os
import sys
import time
import datetime
import logging
import webbrowser
import subprocess
import sqlite3
cls = lambda: os.system('cls')

class Speech_AI:

    def __init__(self):
        self._recognizer = sr.Recognizer()
        try:
            self._microphone = sr.Microphone()
        except OSError:
            print("Микрофон не опознан");
        
    def start(self):
        try:
            print("Минутку тишины, пожалуйста...")
            with self._microphone as source:
                self._recognizer.adjust_for_ambient_noise(source)
            while True:
                try:
                  print("Скажите старт")
                  with self._microphone as source:
                      audio = self._recognizer.listen(source)
                  statement = self._recognizer.recognize_google(audio, language="ru_RU")
                  statement=statement.lower()
                  print("Загрузка....")
                  if((statement.find("старт")!=-1) or (statement.find("star")!=-1)):
                      return True;
                  print("Вы сказали: {}".format(statement))
                except sr.UnknownValueError:
                   cls()
                   print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                  print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
                except TimeoutError:
                  print("Время ожидания ответа из сервера истекло")
                  return 0;
        except:
            print("Пока!")
            return 0;

    def work(self):
        print("Минутку тишины, пожалуйста...")
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

        try:
            print("Добрый день Мистер Cтарк")
            while True:
                print("Скажи что - нибудь!")
                with self._microphone as source:
                    audio = self._recognizer.listen(source)
                print("Понял, идет распознавание...")
                try:
                    statement = self._recognizer.recognize_google(audio, language="ru_RU")
                    statement=statement.lower()

                    # Команды для открытия различных внешних приложений

                    if((statement.find("калькулятор")!=-1) or (statement.find("calculator")!=-1)):
                        self.osrun('calc')
                        cls()

                    if((statement.find("блокнот")!=-1) or (statement.find("notepad")!=-1)):
                        self.osrun('notepad')
                        cls()
                             
                    if((statement.find("paint")!=-1) or (statement.find("паинт")!=-1)):
                        self.osrun('mspaint')
                        cls()

                    if((statement.find("диспетчер задач")!=-1)):
                        self.osrun('taskmgr')
                        cls()
                        
                    if((statement.find("командная строка")!=-1)):
                        self.osrun('start cmd')
                        cls()
                    
                    if((statement.find("проигрыватель виндоус")!=-1) or (statement.find("проигрыватель windows")!=-1)):
                        self.osrun('start wmplayer')
                        cls()

                    if((statement.find("browser")!=-1) or (statement.find("браузер")!=-1)):
                        cls()
                        self.openurl('http://google.ru', 'Открываю браузер')
 
                    # Команды для открытия URL в браузере
                    
                    if(((statement.find("youtube")!=-1) or (statement.find("youtub")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1)) and (statement.find("смотреть")==-1)):                        
                        cls()
                        self.openurl('http://youtube.com', 'Открываю ютуб')
 
                    if(((statement.find("новости")!=-1) or (statement.find("новость")!=-1) or (statement.find("на усть")!=-1))):
                        cls()
                        self.openurl('https://tengrinews.kz/', 'Открываю новости')
                         
                    if((statement.find("mail")!=-1) or (statement.find("майл")!=-1)):
                        cls()
                        self.openurl('https://e.mail.ru/messages/inbox/', 'Открываю почту')
                        
                    if((statement.find("вконтакте")!=-1) or (statement.find("в контакте")!=-1)):
                        cls()
                        self.openurl('http://vk.com', 'Открываю Вконтакте')

                    if((statement.find("телеграмм")!=-1) or (statement.find("телеграм")!=-1) or (statement.find("telegram")!=-1)):
                        cls()
                        self.openurl('https://web.telegram.org', 'Открываю Telegram')

                    if((statement.find("случайное аниме")!=-1) or (statement.find("рандом аниме")!=-1)):
                        cls()
                        self.openurl('https://yummyanime.com/random', 'Вот случайное аниме')

                    if((statement.find("включи музыку")!=-1) or (statement.find("включи музыки")!=-1)):
                        cls()
                        self.openurl('https://www.youtube.com/watch?v=5qap5aO4i9A&ab_channel=ChilledCow', 'Тихий хип-хоп')

                    if(statement.find("погода")!=-1):
                        cls()
                        self.openurl('https://www.gismeteo.kz/weather-nur-sultan-5164/10-days/', 'Открываю погоду')

                    # Команды для поиска в сети интернет
                  
                    if((statement.find("найти")!=-1) or (statement.find("поиск")!=-1) or (statement.find("найди")!=-1) or (statement.find("дайте")!=-1) or (statement.find("mighty")!=-1)):
                        statement=statement.replace('найди', '')
                        statement=statement.replace('найти', '')
                        statement=statement.replace('поиск', '')
                        statement=statement.strip()
                        cls()
                        self.openurl('https://yandex.ru/yandsearch?text=' + statement, "Я нашла следующие результаты")
                        
                    if((statement.find("смотреть")!=-1) and ((statement.find("фильм")!=-1) or (statement.find("film")!=-1))):
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('фильм', '')
                        statement=statement.replace('film', '')
                        statement=statement.strip()
                        cls()
                        self.openurl('https://yandex.ru/yandsearch?text=Смотреть+онлайн+фильм+' + statement, "Выберите сайт где смотреть фильм")

                    if(((statement.find("youtube")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1)) and (statement.find("смотреть")!=-1)):
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('на ютубе', '')
                        statement=statement.replace('на ютуб', '')
                        statement=statement.replace('на youtube', '')
                        statement=statement.replace('на you tube', '')
                        statement=statement.replace('на youtub', '')
                        statement=statement.replace('youtube', '')
                        statement=statement.replace('ютуб', '')
                        statement=statement.replace('ютубе', '')
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.strip()
                        cls()
                        self.openurl('http://www.youtube.com/results?search_query=' + statement, 'Ищу в ютуб')


                    if((statement.find("до свидания")!=-1) or (statement.find("досвидания")!=-1) or (statement.find("пока")!=-1) or (statement.find("увидимся")!=-1) or (statement.find("прощай")!=-1)):
                        print("Всего хорошего, мистер Старк!")
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                        sys.exit()
                    
                    if((statement.find("время")!=-1) or (statement.find("который час")!=-1) or (statement.find("сколько время")!=-1) or (statement.find("сколько щас")!=-1) or (statement.find("сколько сейчас")!=-1)):   
                        time_list = time.localtime()
                        hour = str(time_list[3]);
                        minute = str(time_list[4]);
                        print("Сейчас " + hour + ":" + minute);

                    if((statement.find("дата")!=-1) or (statement.find("какое сегодня число")!=-1) or (statement.find("сегоднящнее число")!=-1) or (statement.find("сегоднящняя дата")!=-1)):   
                        time_list = time.localtime()
                        year = str(time_list[0]);
                        month = str(time_list[1]);
                        day = str(time_list[2]);
                        print("Сейчас " + year + " год, " + month + " месяц и "+ day + " день");
                
                    if((statement.find("привет")!=-1) or (statement.find("здравствуй")!=-1) or (statement.find("приветствую")!=-1) or (statement.find("здорово")!=-1)):
                        time_list = time.localtime()
                        hours = time_list[3]
                        if(6 <= int(hours) <= 12):
                            cls()
                            print("Доброго утра!")
                        elif(13 <= int(hours) <= 18):
                            cls()
                            print("Добрый день!")
                        elif(19 <= int(hours) <= 23):
                            cls()
                            print("Добрый вечер!")
                        else:
                            cls()
                            print("Доброй ночи")
                    
                    if((statement.find("как дела")!=-1) or (statement.find("как твои дела")!=-1) or (statement.find("как поживаешь")!=-1) or (statement.find("как идут дела")!=-1)):
                        randAnswer = random.randint(0,2)
                        if(randAnswer==0):
                            cls()
                            print('Я всего лишь программа которая выполняет приказы на которые я способна, так что перестань спрашивать меня как идут у меня дела')
                        elif(randAnswer==1):
                            cls()
                            print("Хорошо, у вас как?")
                        elif(randAnswer==2):
                            cls()
                            print("Наилучшим образом.")

                    print("Вы сказали: {}".format(statement))
                    
                except sr.UnknownValueError:
                    cls()
                    print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                    print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
                except TimeoutError:
                    print("Не могу получить данные от сервиса Google Speech Recognition")
                    return 0;
        except:
            print("Пока!")
            return 0;
            
    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url, ans):
        webbrowser.open(url)
        print(ans)
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

