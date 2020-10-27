# -*- coding: utf-8 -*-

from bap3 import *

list1 = ['난류', '우유', '메밀', '땅콩', '대두', '밀', '고등어', '게', '새우', '돼지고기', '복숭아', '토마토', '아황산류', '호두', '닭고기', '쇠고기', '오징어', '조개류']
a = 19
while a < 19:
    print("btn%d = BT(text = \"%d. %s\", callback_data = \"%d\")" % (a, a, list1[a-1], a))
    a = a + 1

print(listc('dd', ['faew', 'fawefwg', 'd', 'fgag']))