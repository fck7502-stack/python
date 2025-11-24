import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext

window = tk.Tk()
window.title("Пояк Артем Евгеньевич")
window.geometry("400x300")

notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

calc = ttk.Frame(notebook)
notebook.add(calc, text="Калькулятор")

n1 = ttk.Entry(calc)
n1.pack(pady=5)
op = ttk.Combobox(calc, values=["+","-","*","/"], state="readonly")
op.set("+")
op.pack(pady=5)
n2 = ttk.Entry(calc)
n2.pack(pady=5)

def cal():
    try:
        result = eval(f"{n1.get()} {op.get()} {n2.get()}")
        messagebox.showinfo("Результат", f"= {result}")
    except:
        messagebox.showerror("Ошибка", "Неверные данные")

ttk.Button(calc, text="=", command=cal).pack(pady=5)

check_frame = ttk.Frame(notebook)
notebook.add(check_frame, text="Чекбоксы")

vars = [tk.BooleanVar() for _ in range(3)]
for i, var in enumerate(vars):
    ttk.Checkbutton(check_frame, text=f"Вариант {i+1}", variable=var).pack()

def show_check():
    selected = [f"Вариант {i+1}" for i, var in enumerate(vars) if var.get()]
    messagebox.showinfo("Выбор", f"Выбрано: {', '.join(selected)}" if selected else "Ничего не выбрано")

ttk.Button(check_frame, text="Показать", command=show_check).pack(pady=10)

text_frame = ttk.Frame(notebook)
notebook.add(text_frame, text="Текст")

text_area = scrolledtext.ScrolledText(text_frame, height=10)
text_area.pack(fill='both', expand=True)

def load_file():
    if path := filedialog.askopenfilename(filetypes=[("Text", "*.txt")]):
        with open(path, 'r') as f:
            text_area.delete('1.0', tk.END)
            text_area.insert('1.0', f.read())

menu = tk.Menu(window)
menu.add_command(label="Загрузить", command=load_file)
window.config(menu=menu)

window.mainloop()