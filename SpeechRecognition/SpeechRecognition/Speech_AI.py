import speech_recognition as sr
import Functions
from gtts import gTTS
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
class Speech_AI:

    def __init__(self):
        self._recognizer = sr.Recognizer()
        try:
            self._microphone = sr.Microphone()
        except OSError:
            print("Микрофон не опознан");
        
        now_time = datetime.datetime.now()
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        self._mp3_nameold='111'

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
                   print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                  print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
                except TimeoutError:
                  print("Время ожидания ответа из сервера истекло")
                  return 0;
        except KeyboardInterrupt:
            self._clean_up()
            print("Пока!")

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
                               
                    if((statement.find("блокнот")!=-1) or (statement.find("notepad")!=-1)):
                        self.osrun('notepad')
                             
                    if((statement.find("paint")!=-1) or (statement.find("паинт")!=-1)):
                        self.osrun('mspaint')

                    if((statement.find("диспетчер задач")!=-1)):
                        self.osrun('taskmgr')
                        
                    if((statement.find("командная строка")!=-1)):
                        self.osrun('start cmd')
                    
                    if((statement.find("проигрыватель виндоус")!=-1) or (statement.find("проигрыватель windows")!=-1)):
                        self.osrun('start wmplayer')

                    if((statement.find("browser")!=-1) or (statement.find("браузер")!=-1)):
                        self.openurl('http://google.ru', 'Открываю браузер')
 
                    # Команды для открытия URL в браузере
                    
                    if(((statement.find("youtube")!=-1) or (statement.find("youtub")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1)) and (statement.find("смотреть")==-1)):                        
                        self.openurl('http://youtube.com', 'Открываю ютуб')
 
                    if(((statement.find("новости")!=-1) or (statement.find("новость")!=-1) or (statement.find("на усть")!=-1))):
                        self.openurl('https://www.nur.kz', 'Открываю новости')
                         
                    if((statement.find("mail")!=-1) or (statement.find("майл")!=-1)):
                        self.openurl('https://e.mail.ru/messages/inbox/', 'Открываю почту')
                        
                    if((statement.find("вконтакте")!=-1) or (statement.find("в контакте")!=-1)):
                        self.openurl('http://vk.com', 'Открываю Вконтакте')

                    if((statement.find("майстат")!=-1) or (statement.find("май стат")!=-1) or (statement.find("mystat")!=-1) or (statement.find("my stat")!=-1)):
                        self.openurl('https://mystat.itstep.org/en/main', 'Открываю Mystat')

                    if((statement.find("телеграмм")!=-1) or (statement.find("телеграм")!=-1) or (statement.find("telegram")!=-1)):
                        self.openurl('https://web.telegram.org', 'Открываю Telegram')

                    if((statement.find("голосование")!=-1)):
                        self.openurl('https://www.youtube.com/watch?v=3eToZUkGluk', 'Открываю Рикардо Милоса')

                    if((statement.find("покажи бога")!=-1)):
                        self.openurl('https://pbs.twimg.com/profile_images/679621054361239552/X8Xu2CHm_400x400.jpg', 'Показывают бога')

                    if((statement.find("случайное аниме")!=-1) or (statement.find("рандом аниме")!=-1)):
                        self.openurl('https://yummyanime.com/random', 'Вот случайное аниме')

                    if((statement.find("включи музыку")!=-1) or (statement.find("включи музыки")!=-1)):
                        self.openurl('https://www.youtube.com/watch?v=hHW1oY26kxQ', 'Тихий хип-хоп')

                    # Команды для поиска в сети интернет
                  
                    if((statement.find("найти")!=-1) or (statement.find("поиск")!=-1) or (statement.find("найди")!=-1) or (statement.find("дайте")!=-1) or (statement.find("mighty")!=-1)):
                        statement=statement.replace('найди', '')
                        statement=statement.replace('найти', '')
                        statement=statement.replace('поиск', '')
                        statement=statement.strip()
                        self.openurl('https://yandex.ru/yandsearch?text=' + statement, "Я нашла следующие результаты")
                        
                    if((statement.find("смотреть")!=-1) and ((statement.find("фильм")!=-1) or (statement.find("film")!=-1))):
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('фильм', '')
                        statement=statement.replace('film', '')
                        statement=statement.strip()
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
                        self.openurl('http://www.youtube.com/results?search_query=' + statement, 'Ищу в ютуб')


                    #if((statement.find("слушать")!=-1) and (statement.find("песни")!=-1)):
                    #    statement=statement.replace('песню', '')
                    #    statement=statement.replace('песни', '')
                    #    statement=statement.replace('песня', '')
                    #    statement=statement.replace('песней', '')
                    #    statement=statement.replace('послушать', '')
                    #    statement=statement.replace('слушать', '')
                    #    statement=statement.replace('хочу', '')
                    #    statement=statement.strip()
                    #    self.openurl('https://vk.com/audios356018751?q=' + statement, "Нажмите плэй")


                    #    # бд
                    #if((statement.find("запомни")) != -1 or (statement.find("запиши") != 1)):
                    #    conn = sqlite3.connect("Data.db")
                    #    c = conn.cursor()
                    #    if(statement.find("адрес") != 1):
                    #       Functions.InsertAdress()
                            
                    #    if((statement.find("событи") != 1) or (statment.find("день рождени") != 1) or (statment.find("мероприяти") != 1)):
                    #        Functions.InsertEvent()


                    #    # файловая система

                            
                    #if((statement.find("пиши") != -1) and (statement.find("блокнот")!=-1)):
                    #    Functions.WriteFile()
                            
                            
                            # Поддержание диалога
                    
                    if((statement.find("до свидания")!=-1) or (statement.find("досвидания")!=-1) or (statement.find("пока")!=-1) or (statement.find("увидимся")!=-1) or (statement.find("прощай")!=-1)):
                        answer = "Пока!"
                        self.say(str(answer))
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                        sys.exit()
                    
                    if((statement.find("время")!=-1) or (statement.find("который час")!=-1) or (statement.find("сколько время")!=-1) or (statement.find("сколько щас")!=-1) or (statement.find("сколько сейчас")!=-1)):   
                        time_list = time.localtime()
                        hour = str(time_list[3]);
                        minute = str(time_list[4]);
                        print("Сейчас " + hour + ":" + minute);
                        self.say("Сейчас " + hour + ":" + minute);

                    if((statement.find("дата")!=-1) or (statement.find("какое сегодня число")!=-1) or (statement.find("сегоднящнее число")!=-1) or (statement.find("сегоднящняя дата")!=-1)):   
                        time_list = time.localtime()
                        year = str(time_list[0]);
                        month = str(time_list[1]);
                        day = str(time_list[2]);
                        print("Сейчас " + year + " год, " + month + " месяц и "+ day + " день");
                        self.say("Сейчас " + year + " год, " + month + " месяц и "+ day + " день");
                
                    if((statement.find("привет")!=-1) or (statement.find("здравствуй")!=-1) or (statement.find("приветствую")!=-1) or (statement.find("здорово")!=-1)):
                        time_list = time.localtime()
                        hours = time_list[3]
                        if(6 <= int(hours) <= 12):
                            self.say("Доброго утра!")
                        elif(13 <= int(hours) <= 18):
                            self.say("Добрый день!")
                        elif(19 <= int(hours) <= 23):
                            self.say("Добрый вечер!")
                        else:
                            self.say("Доброй ночи")
                    
                    if((statement.find("как дела")!=-1) or (statement.find("как твои дела")!=-1) or (statement.find("как поживаешь")!=-1) or (statement.find("как идут дела")!=-1)):
                        randAnswer = random.randint(0,2)
                        if(randAnswer==0):
                            self.say('Я всего лишь программа которая выполняет приказы на которые я способна, так что перестань спрашивать меня как идут у меня дела')
                        elif(randAnswer==1):
                            self.say("Хорошо, у вас как?")
                        elif(randAnswer==2):
                            self.say("Наилучшим образом.")
                    else:
                        randAnswer = random.randint(0,10)
                        if(randAnswer==0):
                            self.say("Отлично")
                        if(randAnswer==1):
                            self.say("Я рада")
                        if(randAnswer==2):
                            self.say("Хорошо")
                        if(randAnswer==3):
                            self.say("А вы знали, что пэйпал это плохая вещь?")
                        if(randAnswer==4):
                            self.say("Я не знаю")
                        if(randAnswer==5):
                            self.say("Как же так вышло?")
                        if(randAnswer==6):
                            self.say("Ага")
                        if(randAnswer==7):
                            self.say("Возможно")
                        if(randAnswer==8):
                            self.say("Я не могу понять вас, я всего лишь робот")
                        if(randAnswer==9):
                            self.say("Гло́кая ку́здра ште́ко будлану́ла бо́кра и курдя́чит бокрёнка")
                        if(randAnswer==10):
                            self.say("А?")
                    print("Вы сказали: {}".format(statement))
                    
                except sr.UnknownValueError:
                    print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                    print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
                except TimeoutError:
                    print("Не могу получить данные от сервиса Google Speech Recognition")
                    return 0;
        except KeyboardInterrupt:
            self._clean_up()
            print("Пока!")
        
    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url, ans):
        webbrowser.open(url)
        #self.say(str(ans))
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    def say(self, phrase):
        try:
            tts = gTTS(text=phrase, lang="ru")
            tts.save(self._mp3_name)
        except RuntimeError:
            print("");

        # Play answer
        try:
            mixer.music.load(self._mp3_name)
            mixer.music.play()
            if(os.path.exists(self._mp3_nameold)):
                os.remove(self._mp3_nameold)
        except pygame.error:
            print("");
       
        now_time = datetime.datetime.now()
        self._mp3_nameold=self._mp3_name
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        
        
    

    def _clean_up(self):
        def clean_up():
            os.remove(self._mp3_name)

