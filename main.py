import datetime
import random

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta,'JST')
time = datetime.datetime.now(JST)
time = time.strftime('%Y/%m/%d %H:%M:%S')
print(time)

name = input("氏名を入力してください：")

number = [random.random(), random.random(), random.random(),
          random.random(), random.random(), random.random()]

number2 = [1,1,1,1,1,1]

hel= number[0]
gun= number[1]
han= number[2]
an= number[3]
full= number[4]
soku= number[5]


def check(hel, gun, han, an, full, soku, name):
    word = name + 'さんは'
    if (hel < 0.5):
        word += 'ヘルメット,'

    if (gun < 0.5):
        word += '軍手,'

    if (han < 0.5):
        word += '反射ベスト,'

    if (an < 0.5):
        word += '安全帯,'

    if (full < 0.5):
        word += 'フルハーネス,'

    if (soku < 0.5):
        word += '測定器具,'
    if (hel and gun and han and an and full and soku) >= 0.5:
        word = '全て装着されています。'
    else:
        word += 'が装着されていません。'

    return word

sentence = check(hel, gun, han, an, full, soku, name)

sentenceOK = check(1, 1, 1, 1, 1, 1, name)
print(sentence)

#print(sentenceOK)





