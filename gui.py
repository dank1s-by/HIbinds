import customtkinter as ctk
import json
import runner
 

class HiBindsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.new_bind_actions = []
        self.bind_buttons = []


        self.title("HiBinds Launcher")
        self.geometry("700x500")
        self.resizable(False, False)

        # Создаем вкладки
        self.tabview = ctk.CTkTabview(self, width=660, height=450)
        self.tabview.pack(padx=20, pady=20)
        self.tabview.add("Run Binds")
        self.tabview.add("Create Bind")

        # Заголовок во вкладке запуска
        self.run_label = ctk.CTkLabel(self.tabview.tab("Run Binds"), text="Click a bind to launch:", font=("Arial", 16, "bold"))
        self.run_label.pack(pady=10)

        # Вызываем метод, который создаст кнопки для существующих биндов
        self.load_bind_buttons()

        # --- Верстка вкладки "Create Bind" ---
        tab_create = self.tabview.tab("Create Bind")

        # 1. Поле для имени бинда
        self.lbl_name = ctk.CTkLabel(tab_create, text="1. Название бинда:", font=("Arial", 14, "bold"))
        self.lbl_name.pack(pady=(10, 2))
        self.entry_bind_name = ctk.CTkEntry(tab_create, placeholder_text="", width=400)
        self.entry_bind_name.pack(pady=5)

        # 2. Поле для пути/ссылки
        self.lbl_action = ctk.CTkLabel(tab_create, text="2. Путь к .exe или URL-ссылка:", font=("Arial", 14, "bold"))
        self.lbl_action.pack(pady=(10, 2))
        self.entry_action_path = ctk.CTkEntry(tab_create, placeholder_text="", width=400)
        self.entry_action_path.pack(pady=5)

        # 3. Поле для задержки
        self.lbl_delay = ctk.CTkLabel(tab_create, text="3. Задержка (в миллисекундах):", font=("Arial", 14, "bold"))
        self.lbl_delay.pack(pady=(10, 2))
        self.entry_delay = ctk.CTkEntry(tab_create, placeholder_text="2000", width=400)
        self.entry_delay.pack(pady=5)

        # 4. Кнопка "Добавить это действие в последовательность"
        self.btn_add_action = ctk.CTkButton(tab_create, text=" Добавить действие", fg_color="green", hover_color="darkgreen", command=self.add_action_to_memory)
        self.btn_add_action.pack(pady=15)

        # 5. Кнопка "Сохранить весь бинд на ПК"
        self.btn_save_bind = ctk.CTkButton(tab_create, text=" СОХРАНИТЬ БИНД", width=300, height=40, font=("Arial", 14, "bold"), command=self.save_full_bind)
        self.btn_save_bind.pack(pady=(20, 5))

    def load_bind_buttons(self):
        # 1. Сначала полностью удаляем старые кнопки с экрана, чтобы они не дублировались
        for button in self.bind_buttons:
            button.destroy()
        self.bind_buttons.clear() # Очищаем сам список в памяти

        # 2. Читаем твой JSON файл
        try:
            with open("HIBinds.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # 3. Перебираем все имена биндов и создаем кнопки заново
        for bind_name in data.keys():
            btn = ctk.CTkButton(
                self.tabview.tab("Run Binds"), 
                text=f"{bind_name}", 
                width=300,
                height=40,
                font=("Arial", 14),
                command=lambda name=bind_name: self.start_bind(name)
            )
            btn.pack(pady=5)
            
            #сохраняем ссылку на кнопку в наш список класса
            self.bind_buttons.append(btn)

    def add_action_to_memory(self):
        # Получаем данные из текстовых полей
        target = self.entry_action_path.get().strip('"')
        delay_raw = self.entry_delay.get()

        if not target:
            print("Интерфейс: Поле пути пустое!")
            return

        # Переводим задержку в число
        try:
            delay = int(delay_raw)
        except ValueError:
            delay = 0

        # Определяем тип (приложение или ссылка)
        if target.startswith("http://") or target.startswith("https://"):
            action_type = "url"
        else:
            action_type = "app"

        # Сохраняем действие во временный список в памяти класса
        self.new_bind_actions.append({
            "type": action_type,
            "action": target,
            "delay_ms": delay
        })

        print(f"Интерфей: Добавлено действие -> {target} с задержкой {delay}мс")
        
        # Очищаем поля ввода для следующей программы, а имя бинда оставляем
        self.entry_action_path.delete(0, 'end')
        self.entry_delay.delete(0, 'end')

    def save_full_bind(self):
        bind_name = self.entry_bind_name.get().strip()

        if not bind_name:
            print("Интерфейс: Введите название бинда!")
            return
        if not self.new_bind_actions:
            print("Интерфейс: Вы не добавили ни одного действия!")
            return

        # 1. Читаем существующий JSON
        try:
            with open("HIBinds.json", "r", encoding="utf-8") as f:
                current_binds = json.load(f)
        except FileNotFoundError:
            current_binds = {}

        # 2. Упаковываем данные в твою структуру
        current_binds[bind_name] = {
            "actions": self.new_bind_actions
        }

        # 3. Записываем в файл
        with open("HIBinds.json", "w", encoding="utf-8") as f:
            json.dump(current_binds, f, indent=4, ensure_ascii=False)

        print(f"Интерфейс: Бинд '{bind_name}' успешно сохранен в HIBinds.json!")

        # Полностью очищаем все поля формы и временную память для следующего бинда
        self.entry_bind_name.delete(0, 'end')
        self.new_bind_actions = []
        
        # Обновляем кнопки на первой вкладке, чтобы новый бинд сразу появился!
        self.load_bind_buttons()

    def start_bind(self, bind_name):
        print(f"start '{bind_name}'...")
        runner.use_bind(bind_name) 

if __name__ == "__main__":
    app = HiBindsApp()
    app.mainloop()