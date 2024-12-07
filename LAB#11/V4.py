# -- Coding UTF-8 --

from tkinter import *
import requests
from pprint import pprint
import json

def click():
    username = 'nixos'
    url = f'https://api.github.com/users/{username}'
    user_data = requests.get(url).json()

    selected_keys = {'company', 'created_at', 'email', 'id', 'url'}
    filtered_data = {key: user_data[key] for key in selected_keys if key in user_data}

    with open('V4.json', 'w') as write_file:
        json.dump(filtered_data, write_file, indent=2)

    close()

def close():
    newindow = Tk()
    newindow.geometry('400x150')
    newindow.title('GitHUB API')

    lbl2 = Label(newindow, text='Файлы успешно загружены!', font=('Arial', 20))
    lbl2.pack(pady=50)

    window.destroy()

window = Tk()
window.geometry('400x200')
window.title('GitHUB API')

window.columnconfigure(0, weight=1)
window.rowconfigure([0, 10], weight=1)

lbl = Label(window, text='Номер зачетки - 4', font=('Arial', 20))
lbl.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)

btn = Button(window, text='Установить ключи', command=click)
btn.grid(column=0, row=10, sticky='ew', pady=20, ipady=5, ipadx=40)

window.mainloop()
