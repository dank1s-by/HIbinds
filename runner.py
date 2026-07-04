import json
import time
import subprocess
import webbrowser

DB_file = 'HIbinds.json'


def use_bind():
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
            return
        else:
            return
    except:
        return
        
    bind_info = data[choosen_bind] # Получаем словарь конкретного бинда
    actions_list = bind_info["actions"]

    for i in actions_list:

        delay_now = i['delay_ms'] / 1000
        if delay_now > 0:
            print(f'wait {delay_now} sec...')
            time.sleep(delay_now)

        if i['type'] == 'app':
            print(i['action'])
            print('start the program...')
            subprocess.Popen(i['action'])
        elif i['type'] == 'url':
            print('open the link...')
            webbrowser.open(i['action'])
    