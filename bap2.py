# -*- coding: utf-8 -*-

import telegram
import time
import bap
from bap3 import *
import bap4
from ast import literal_eval

my_token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'
bot = telegram.Bot(token = my_token)

yyy = ['난류', '우유', '메밀', '땅콩', '대두', '밀', '고등어', '게', '새우', '돼지고기', '복숭아', '토마토', '아황산류', '호두', '닭고기', '쇠고기', '오징어', '조개류']

time.sleep(5)
#aaa = len(bot.getUpdates(offset = -10))
# print(aaa)

# my_token = '1335732615:AAHRizqQGhUfwJCzDPwPd-_Mk4iGJOS8H_c'
# bot = telegram.Bot(token = my_token)

# bot.sendMessage(chat_id = '@helloworld11222', text = 'hello')

# my_token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'
# bot = telegram.Bot(token = my_token)

up_check = len(bot.getUpdates())
print(up_check)
onoff = 1
ch_id = ""
get_id = ""
text_l = ['dddd']

while True:
	#print("getting...")
	updates = bot.getUpdates()
	#print(len(bot.getUpdates()))
	#chat_id = bot.getUpdates()[-1].message.chat.id
	update_c = len(bot.getUpdates())
	#print(update_c)
	last_m = literal_eval("%s" % bot.getUpdates()[-1])
	if update_c != up_check:
		# print(last_m)
		if 'callback_query' in last_m:
			get_id = last_m['callback_query']['from']['id']
			get_text = last_m['callback_query']['data']
			bt_on = 1
			text_l = get_text.split(' ')
		else:
			get_text = last_m['message']['text']
			get_id = last_m['message']['chat']['id']
			get_name = last_m['message']['chat']['first_name']
			text_l = get_text.split(' ')
			bt_on = 0
		# print("bt_on : %d, get_id : %s, get_text : %s" % (bt_on, get_id, get_text))
		ch_id = get_id
		#print("%s가 %s 이라고 말함(ID : %s)" % (get_name, get_text, get_id))
		if onoff == 1:
			if get_text == "/help" or get_text == "/?":
				sendm('/오늘의급식 : 오늘의 급식를 알려줌\n/알레르기등록 : 알레르기 등록 메뉴\n/알레르기검사 : 오늘 급식에서 자신의 알레르기 검사')
			if get_text == "/오늘의급식":
				bap.getbap(0, get_id)
			if get_text == "/알레르기검사":
				bap.alcheck(get_id)
			if text_l[0] == '/알레르기등록':
				bap4.btn_show()
				# if len(text_l) < 2:
				# 	sendm("뒤에 알레르기 정보를 입력해주세요")
				# else:
				# 	print("등록 감지")
				# 	ll = []
				# 	bap.setal(get_id, text_l[1:])
				# 	#print("등록 완료 %s" % text_l[1:])
				# 	i = 0
				# 	while i < len(text_l[1:]):
				# 		if yyy.count(text_l[i+1]) > 0:
				# 			if not ll.count(text_l[i+1]) > 0:
				# 				ll.append(text_l[i+1])
				# 		i = i + 1
				# 	sendm("%s님의 알러지를 ::%s::로 설정했습니다" % (get_name, ', '.join(ll)))
			if bt_on == 1:
				if int(get_text) < 19:
					bap.addal(get_id, yyy[int(get_text)-1])
					# bot.sendMessage(chat_id = get_id, text = "%s을(를) 추가했습니다" % yyy[int(get_text)-1])
				elif int(get_text) == 19:
					bap.showlist1(get_id)
				elif int(get_text) == 20:
					bap.listre(get_id)
		if get_text == "/on" and get_name == 'ymschool':
				onoff = 1
				sendm("작동을 시작합니다.")
		if get_text == "/off" and get_name == 'ymschool':
				onoff = 0
				sendm("작동을 중지합니다.")
		aaa = len(bot.getUpdates(offset = -10))
		time.sleep(0.5)
		update_c = len(bot.getUpdates())
		up_check = update_c