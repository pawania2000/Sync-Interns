from plyer import notification
import time
title= 'Get motivation'
with open('Quotes.txt' , 'r', encoding='utf-8') as q :
    lines = q.readlines()

    for quote in lines:
       notification.notify(title = title , message = quote.strip() , timeout = 25 , app_icon="C:\\Users\\PAWENI\\Desktop\\sync intern tasks\\Golden-Key.ico")
       time.sleep(5)