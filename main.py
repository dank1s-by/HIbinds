import json
import os
from creater import create_new_bind
DB_file = "HIbinds.json"

if not os.path.exists(DB_file):
    with open(DB_file, "w", encoding="utf-8") as f:
        json.dump({}, f)
    print('data base file create!\n')
else:
    print('database file found OwO\n')


while True:
    first_mess = input('Hi, this is HiBinds. Choose what you want to do:\n1. Use a working bind\n2. Create a new bind\n:')
    if first_mess == '1': 
        pass
        break
    elif first_mess == '2':
        create_new_bind()
        break
    else:
        print('wrong way!!!')





















# program1 = r'"C:\Program Files\FACEIT AC\faceitclient.exe"'
# program2 = r'"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64\cs2.exe"'

# delay1 = 3
# delay2 = 0

# subprocess.Popen(program1)
# time.sleep(delay1)
# subprocess.Popen(program2)