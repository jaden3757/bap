# -*- coding: utf-8 -*-

# from bap3 import *
from ast import literal_eval

# list1 = ['난류', '우유', '메밀', '땅콩', '대두', '밀', '고등어', '게', '새우', '돼지고기', '복숭아', '토마토', '아황산류', '호두', '닭고기', '쇠고기', '오징어', '조개류']
# a = 19
# while a < 19:
#     print("btn%d = BT(text = \"%d. %s\", callback_data = \"%d\")" % (a, a, list1[a-1], a))
#     a = a + 1

# print(listc('dd', ['faew', 'fawefwg', 'd', 'fgag']))

rrr = literal_eval("{'update_id': 285205978, 'callback_query': {'id': '5654838918303691170', 'chat_instance': '-1066361618204246217', 'message': {'message_id': 46, 'date': 1603806165, 'chat': {'id': 1316619785, 'type': 'private', 'first_name': 'HS'}, 'text': '알레르기 목록(해당하는 것을 누르시오', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'reply_markup': {'inline_keyboard': [[{'text': '1. 난류', 'callback_data': '1'}, {'text': '2. 우유', 'callback_data': '2'}, {'text': '3. 메밀', 'callback_data': '3'}, {'text': '4. 땅콩', 'callback_data': '4'}, {'text': '5. 대두', 'callback_data': '5'}, {'text': '6. 밀', 'callback_data': '6'}], [{'text': '7. 고등어', 'callback_data': '7'}, {'text': '8. 게', 'callback_data': '8'}, {'text': '9. 새우', 'callback_data': '9'}, {'text': '10. 돼지고기', 'callback_data': '10'}, {'text': '11. 복숭아', 'callback_data': '11'}, {'text': '12. 토마토', 'callback_data': '12'}], [{'text': '13. 아황산류', 'callback_data': '13'}, {'text': '14. 호두', 'callback_data': '14'}, {'text': '15. 닭고기', 'callback_data': '15'}, {'text': '16. 쇠고기', 'callback_data': '16'}, {'text': '17. 오징어', 'callback_data': '17'}, {'text': '18. 조개류', 'callback_data': '18'}]]}, 'from': {'id': 1353878249, 'first_name': 'Hello', 'is_bot': True, 'username': 'Hello11world_bot'}}, 'data': '1', 'from': {'id': 1316619785, 'first_name': 'HS', 'is_bot': False, 'language_code': 'ko'}}}")

if 'update_id' in rrr:
    print(rrr['update_id'])