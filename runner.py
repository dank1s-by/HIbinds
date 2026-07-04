import json
import time
import subprocess

DB_file = 'HIbinds.json'

with open("HIBinds.json", "r", encoding="utf-8") as f:
    data = json.load(f)
binds = list(data)

print('choose bind, or pres 0 for exit:')
for index, i in enumerate(binds, start=1):
    print(index, i)

choosen_bind = None
try:
    the_bind = int(input(':'))

    if 0 < the_bind <= len(binds):
        choosen_bind = binds[the_bind - 1]
        print(binds[the_bind - 1])
    elif the_bind == 0:
        print('ok') #добавлю сбда потом функцию гл меню
    else:
        print('WROOONG')#добавлю сбда потом функцию гл меню
except:
    print('WROOONG')#добавлю сбда потом функцию гл меню
    
bind_info = data[choosen_bind] # Получаем словарь конкретного бинда
actions_list = bind_info["actions"]
print(actions_list)


