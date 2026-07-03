import json

DB_file = "HIbinds.json"

# основная функиця 
def create_new_bind():
    bind_name = input('\nwrite name for your bind: \n') #имя
    bind_act = {'actions': []}

    while True: # основной цикл сборки
        action = input('\nEnter the path to the .exe file or URL, ending with 0: \n')
        if action == '0':
            break



        if action.startswith("http://") or action.startswith("https://"): # проврка на сайт или прогу
            action_type = "url"
        else:
            action_type = 'app'

        try:
            delay = int(input('\nEnter a delay before starting the action(ms) : \n'))
        except:
            print('\n WROOONG delay = 2 sec')
            delay = 2000
        



        bind_act["actions"].append({"type": action_type, "action": action, "delay_ms": delay})
    #запись



    if bind_act['actions']:
        with open(DB_file, "r", encoding="utf-8") as f:
            sych_binds = json.load(f)
            sych_binds[bind_name] = bind_act

        with open(DB_file, "w", encoding="utf-8") as f:
            json.dump(sych_binds, f, indent=4, ensure_ascii=False)
        print(f'\nbind {bind_name} load!!! OWO')
        
    else:
        print('\nbind not load, try one more time :(')