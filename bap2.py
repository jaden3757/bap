# -*- coding: utf-8 -*-

import telegram
import time
import bap

my_token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'

bot = telegram.Bot(token = my_token)

yyy = ['난류', '우유', '메밀', '땅콩', '대두', '밀', '고등어', '게', '새우', '돼지고기', '복숭아', '토마토', '아황산류', '호두', '닭고기', '쇠고기', '오징어', '조개류']

bap.sendm("start")

time.sleep(5)

aaa = len(bot.getUpdates(offset = -10))
# print(aaa)
up_check = len(bot.getUpdates())
print(up_check)
onoff = 1

while True:
	#print("getting...")
	updates = bot.getUpdates()
	#print(len(bot.getUpdates()))
	#chat_id = bot.getUpdates()[-1].message.chat.id
	update_c = len(bot.getUpdates())
	#print(update_c)
	last_m = bot.getUpdates()[-1]

	if update_c != up_check:
		get_text = last_m['channel_post']['text']
		get_id = last_m['channel_post']['chat']['id']
		get_name = last_m['channel_post']['chat']['username']
		#print("%s가 %s 이라고 말함(ID : %s)" % (get_name, get_text, get_id))
		text_l = get_text.split(' ')
		if onoff == 1:
			if get_text == "/오늘의급식":
				bap.getbap(0, get_id)
			if get_text == "/알레르기검사":
				bap.alcheck(get_id)
			if text_l[0] == '/알레르기등록':
				if len(text_l) < 2:
					sendm("뒤에 알레르기 정보를 입력해주세요")
				else:
					print("등록 감지")
					ll = []
					bap.setal(get_id, text_l[1:])
					#print("등록 완료 %s" % text_l[1:])
					i = 0
					while i < len(text_l[1:]):
						if yyy.count(text_l[i+1]) > 0:
							if not ll.count(text_l[i+1]) > 0:
								ll.append(text_l[i+1])
						i = i + 1
					bap.sendm("%s님의 알러지를 ::%s::로 설정했습니다" % (get_name, ', '.join(ll)))
		if get_text == "/on" and get_name == 'ymschool':
				onoff = 1
				bap.sendm("작동을 시작합니다.")
		if get_text == "/off" and get_name == 'ymschool':
				onoff = 0
				bap.sendm("작동을 중지합니다.")
		aaa = len(bot.getUpdates(offset = -10))
		time.sleep(0.5)
		update_c = len(bot.getUpdates())
		up_check = update_c