# -*- coding: utf-8 -*-

import telepot

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup as MU
from telepot.namedtuple import InlineKeyboardButton as BT

token = '1353878249:AAE886CdaD4FrDiZsPFoNZj0V03EhEjDUPE'
mc = '1316619785'
bot = telepot.Bot(token)

# ['난류', '우유', '메밀', '땅콩', '대두', '밀', '고등어', '게', '새우', '돼지고기', '복숭아', '토마토', '아황산류', '호두', '닭고기', '쇠고기', '오징어', '조개류']


def btn_show():
    btn1 = BT(text = "난류", callback_data = "1")
    btn2 = BT(text = "우유", callback_data = "2")
    btn3 = BT(text = "메밀", callback_data = "3")
    btn4 = BT(text = "땅콩", callback_data = "4")
    btn5 = BT(text = "대두", callback_data = "5")
    btn6 = BT(text = "밀", callback_data = "6")
    btn7 = BT(text = "고등어", callback_data = "7")
    btn8 = BT(text = "게", callback_data = "8")
    btn9 = BT(text = "새우", callback_data = "9")
    btn10 = BT(text = "돼지고기", callback_data = "10")
    btn11 = BT(text = "복숭아", callback_data = "11")
    btn12 = BT(text = "토마토", callback_data = "12")
    btn13 = BT(text = "아황산류", callback_data = "13")
    btn14 = BT(text = "호두", callback_data = "14")
    btn15 = BT(text = "닭고기", callback_data = "15")
    btn16 = BT(text = "쇠고기", callback_data = "16")
    btn17 = BT(text = "오징어", callback_data = "17")
    btn18 = BT(text = "조개류", callback_data = "18")
    btn19 = BT(text = "알레르기보기", callback_data = "19")
    btn20 = BT(text = "알레르기초기화", callback_data = "20")

    mu = MU(inline_keyboard = [[btn1, btn2, btn3, btn4, btn5], [btn6, btn7, btn8, btn9, btn10], [btn11, btn12, btn13, btn14, btn15], [btn16, btn17, btn18], [btn19, btn20]])

    bot.sendMessage(mc, "알레르기 목록(해당하는 것을 누르시오", reply_markup = mu)

# MessageLoop(bot, {'chat': btn_show, 'callback_query' : query_ans}).run_as_thread()
