price = 123
bonus = 23
bonus_granted = True
 
##if bonus_granted:
##    price -= bonus
## 
##print(price)

print(price-bonus) if bonus_granted else '?'


rating = 5
 
##if rating == 5:
##    print('very good')
##elif rating == 4:
##    print('good')
##else:
##    print('weak')

print('very good') if rating == 5 else print('ggod') if rating ==4 else print('weak')

import datetime

x=datetime.datetime.now().strftime("%A")
print(type(x))

today_weekday = datetime.datetime.now().strftime("%A")

poniedziałek = 'pomagam mamie'
wtorek = 'mam w domu pranie'
środa = 'mam w domu pranie'
czwartek = 'dyżur'
piątek = 'zebrania'
sobota = 'lekcje grania'
niedziela = 'będzie dla nas'

if today_weekday == 'poniedziałek':
    print(poniedziałek)
elif today_weekday == 'środa' or today_weekday=='wtorek':
    print(środa)
elif today_weekday == 'Wednesday':
    print(czwartek)
elif today_weekday == 'piątek':
    print(piątek)
elif today_weekday=='sobota':
    print(sobota)
else:
    print(niedziela)

print('pomagam') if today_weekday=='środa' else print('będzie dla nas')
