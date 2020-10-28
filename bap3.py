# -*- coding: utf-8 -*-

import telegram
import time

my_token = '1335732615:AAHRizqQGhUfwJCzDPwPd-_Mk4iGJOS8H_c'
bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id = '@helloworld11222', text = 'hello')

my_token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'

bot = telegram.Bot(token = my_token)

# print(bot.getUpdates()[-1])

get_id = ""
def sendm(msg):
	bot.sendMessage(chat_id = bot.getUpdates()[-1]['message']['chat']['id'], text = msg)

def listc(text, ls):
        if text in ls:
            return 1
        else:
            return 0
# while True:
#     get_id = bot.getUpdates()[-1]['message']['chat']['id']