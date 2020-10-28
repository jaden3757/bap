# -*- coding: utf-8 -*-

from selenium import webdriver
import telegram
import time
from bap3 import *
from datetime import date

my_token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'

bot = telegram.Bot(token = my_token)

#bot.getUpdates()

list1 = []
list2 = {1: '난류', 2: '우유', 3: '메밀', 4: '땅콩', 5: '대두', 6: '밀', 7: '고등어', 8: '게', 9: '새우', 10: '돼지고기', 11: '복숭아', 12: '토마토', 13: '아황산류', 14: '호두', 15: '닭고기', 16: '쇠고기', 17: '오징어', 18: '조개류'}

al_name = []
al_list = []
#print(list2)

# def sendm(msg):
# 	bot.sendMessage(chat_id = bap2.getid(), text = msg)

def timecutter(date, mode):
	i = 0
	month = 0
	day = 0
	fin = 0
	while i < len(date):
		if date[i] == "월" and fin == 0:
			month = i + 1
			fin = 1
		if date[i] == "일" and fin == 1:
			day = i + 1
			fin = 2
		i = i + 1
	#월,일 보내기
	if mode == 1:
		return int(date[0:month-1])
	if mode == 2:
		return int(date[month+1:day-1])

def cut(strn, ct):
	i = 0
	c1 = -1
	while i < len(strn):
		if strn[i] == ct:
			list1.append(strn[c1+1:i])
			c1 = i
		i = i + 1
	list1.append(strn[c1+1:i])

def setal(uname, alist):
	i = 0
	al_num = -1
	while i < len(al_name):
		if al_name[i] == uname:
			al_num = i
		i = i + 1
	if al_num == -1:
		al_name.append(uname)
		al_list.append(alist)
	else:
		al_list[al_num] = alist

def addal(uid, alist):
	i = 0
	al_num = -1
	while i < len(al_name):
		if al_name[i] == uid:
			al_num = i
		i = i + 1
	if al_num == -1:
		al_name.append(uid)
		al_list.append([])
		i = 0
		while i < len(al_name):
			if al_name[i] == uid:
				al_num = i
			i = i + 1
		if listc(alist, al_list[al_num]) == 1:
			i = 0
			while i < len(al_list[al_num]):
				if al_list[al_num][i] == alist:
					del al_list[al_num][i]
				i = i + 1
			bot.sendMessage(chat_id = uid, text = "%s을(를) 제거했습니다" % alist)
			return 0
		al_list[al_num].append(alist)
		bot.sendMessage(chat_id = uid, text = "%s을(를) 추가했습니다" % alist)
	else:
		if listc(alist, al_list[al_num]) == 1:
			i = 0
			while i < len(al_list[al_num]):
				if al_list[al_num][i] == alist:
					del al_list[al_num][i]
				i = i + 1
			bot.sendMessage(chat_id = uid, text = "%s을(를) 제거했습니다" % alist)
			return 0
		al_list[al_num].append(alist)
		bot.sendMessage(chat_id = uid, text = "%s을(를) 추가했습니다" % alist)

def findnum(uid):
	i = 0
	al_num = -1
	while i < len(al_name):
		if al_name[i] == uid:
			return i
	return -1

def alcheck(username):
	if findnum(username) == -1:
		sendm("당신의 알레르기 정보가 등록되지 않았습니다.")
	else:
		getbap(1, findnum(username))

def showlist1(id2):
	if findnum(id2) == -1:
		bot.sendMessage(chat_id = id2, text = "당신의 알레르기 정보가 등록되지 않았습니다.")
	else:
		bot.sendMessage(chat_id = id2, text = "알레르기 목록 : %s" % al_list[findnum(id2)])

def listre(id2):
	if findnum(id2) > -1:
		al_list[findnum(id2)] = []
		bot.sendMessage(chat_id = id2, text = "당신의 알레르기 목록을 초기화했습니다")

# l = 0
# while l == 0:
# 	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 	getlist = input("알러지가 있는 음식을 입력해주세요(반드시 띄어쓰기로 구분을 해주세요)\n1. 난류 2. 우유 3. 메밀 4. 땅콩 5. 대두 6. 밀 7. 고등어 8. 게 9. 새우 10. 돼지고기 11. 복숭아 12. 토마토 13. 아황산류 14. 호두 15. 닭고기 16. 쇠고기 17. 오징어 18. 조개류\n입력 > ")

# 	cut(getlist, ' ')
# 	print("\n\n")

# 	print("입력하신 음식이 ::%s::(이)가 맞습니까?" % ' '.join(list1))
# 	getok = input("yes or no > ")
# 	if getok == 'yes':
# 		l = 1
# 	else:
# 		l = 0
# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# exit()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('lang=ko_KR')
options.add_argument("--disable-gpu")

driver = webdriver.Chrome("C:/Users/HS/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

url = "https://bloodcat.com/carte/"

driver.get(url)

time.sleep(1)

#driver.find_element_by_name().send_keys("")
# driver.find_element_by_xpath('//*[@id="root"]/header/div/button[1]').click()
#time.sleep(1)
# print("1")
driver.find_element_by_xpath('/html/body/div[4]/div[2]/ul/li[1]/div/div[2]/button').click()
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="root"]/header/div/div/input').send_keys("용문고등학교")
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="root"]/header/div/div/input').submit()
#time.sleep(1)

driver.find_element_by_xpath('//*[@id="root"]/main/ul/div[2]').click()
time.sleep(0.5)

def getbap(mode1, usernum):
	# options = webdriver.ChromeOptions()
	# options.add_argument('headless')
	# options.add_argument('lang=ko_KR')
	# options.add_argument("--disable-gpu")

	# driver = webdriver.Chrome("C:/Users/HS/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

	# url = "https://bloodcat.com/carte/"

	# driver.get(url)

	# time.sleep(1)

	# #driver.find_element_by_name().send_keys("")
	# # driver.find_element_by_xpath('//*[@id="root"]/header/div/button[1]').click()
	# #time.sleep(1)
	# # print("1")
	# driver.find_element_by_xpath('/html/body/div[4]/div[2]/ul/li[1]/div/div[2]/button').click()
	# time.sleep(0.5)

	# driver.find_element_by_xpath('//*[@id="root"]/header/div/div/input').send_keys("용문고등학교")
	# time.sleep(1)
	# # driver.find_element_by_xpath('//*[@id="root"]/header/div/div/input').submit()
	# #time.sleep(1)

	# driver.find_element_by_xpath('//*[@id="root"]/main/ul/div[2]').click()
	# time.sleep(0.5) #fin

	month1 = int(str(date.today())[5:7])
	day1 = int(str(date.today())[8:10])
	# # "8월 21일"
	# month1 = 8
	# day1 = 21
	ok = 0

	# def sendm(msg):
	# 	bot.sendMessage(chat_id = bot.getUpdates()[-1]['channel_post']['chat']['id'], text = msg)

	while ok == 0:
		date2 = (driver.find_element_by_xpath('//*[@id="root"]/header/div/button[2]/span[1]/h2').text)
		#print(date2)
		month2 = timecutter(date2, 1)
		#print(month2)
		day2 = timecutter(date2, 2)
		#print(day2)

		if month2 == month1:
			if day2 == day1:
				ok = 1
		if ok == 0:
			if month2 > month1:
				driver.find_element_by_xpath('//*[@id="root"]/header/div/div/button[1]').click()
			if month2 == month1:
				if day2 > day1:
					driver.find_element_by_xpath('//*[@id="root"]/header/div/div/button[1]').click()
				if day2 < day1:
					driver.find_element_by_xpath('//*[@id="root"]/header/div/div/button[2]').click()
			if month2 < month1:
				driver.find_element_by_xpath('//*[@id="root"]/header/div/div/button[2]').click()
	# '//*[@id="root"]/header/div/div/button[1]' : 이전 '//*[@id="root"]/header/div/div/button[2]' : 이후

	time.sleep(2)

	#급식 여부
	if not driver.find_elements_by_xpath('//*[@id="root"]/main/div/header/div/div/div/div/button/span[1]/span/span'):
		sendm("오늘 급식 없다")
	else:
		driver.find_element_by_xpath('//*[@id="root"]/main/div/header/div/div/div/div/button').click()
		#급식 목록 출력
		gk = driver.find_element_by_xpath('//*[@id="root"]/main/div/ul').text
		#print(gk)
	#print("")
		if mode1 == 0:
			sendm(gk)
	if mode1 == 1:
		gk1 = gk.split('\n')
		gk2 = []
		gk3 = []
		n = 0
		# test1.2.3 => test, 1 2 3
		while n < len(gk1):
			m = 0
			while m < len(gk1[n]):
				if gk1[n][m] >= '0' and gk1[n][m] <= '9':
					gk2.append(gk1[n][m:])
					gk3.append(gk1[n][0:m])
					break
				m = m + 1
			n = n + 1

		gk4 = []
		gk5 = []
		gk6 = []
		n = 0
		#checking
		while n < len(gk2):
			m = 0
			gk4 = gk2[n].split('.')
			gk4.pop()
			check = 0
			while m < len(gk4):
				if al_list[usernum].count(list2[int(gk4[m])]) > 0:
					check = 1
				m = m + 1
			if check == 1:
				gk5.append('알러지 성분 포함됨 *')
			else:
				gk5.append('알러지 성분 없음')
			n = n + 1

		#print("\n\n\n\n\n\n\n\n\n\n\n\n\n[ 오늘의 급식 ]\n%s\n\n" % gk)
		n = 0
		while n < len(gk3):
			gk6.append("%s에 %s\n" % (gk3[n], gk5[n]))
			n = n + 1
		
		if mode1 == 1:
			sendm(''.join(gk6))
			# for i in gk6:
			# 	sendm(i)
			# 	print(i)
		# 1. 난류 2. 우유 3. 메밀 4. 땅콩 5. 대두 6. 밀 7. 고등어 8. 게 9. 새우 10. 돼지고기 
		# 11. 복숭아 12. 토마토 13. 아황산류 14. 호두 15. 닭고기 16. 쇠고기 17. 오징어 18. 조개류(굴, 전복, 홍합 포함)

# up_check = len(bot.getUpdates())

# while True:
# 	#print("getting...")
# 	updates = bot.getUpdates()
# 	#print(len(bot.getUpdates()))
# 	#chat_id = bot.getUpdates()[-1].message.chat.id
# 	update_c = len(bot.getUpdates())
# 	last_m = bot.getUpdates()[-1]

# 	if update_c != up_check:
# 		get_text = last_m['channel_post']['text']
# 		get_id = last_m['channel_post']['chat']['id']
# 		get_name = last_m['channel_post']['chat']['username']
# 		#print("%s가 %s 이라고 말함(ID : %s)" % (get_name, get_text, get_id))
# 		text_l = get_text.split(' ')
# 		if get_text == "/밥":
# 			getbap(0, get_id)
# 		if get_text == "/밥2":
# 			getbap(1, findnum(get_id))
# 		if text_l[0] == '/알레르기':
# 			setal(get_id, text_l[1:])
# 			print("등록 완료 %s" % text_l[1:])
# 		update_c = len(bot.getUpdates())
# 		up_check = update_c
