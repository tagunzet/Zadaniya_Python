import sqlite3
from tkinter import *

def addItem():
    lbox.delete(0, END)

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    bag = entry.get()
    sql = "SELECT * FROM " + entry.get() + ""
    cursor.execute(sql)
    conn.commit()
    lambda: (create_ticket(entry.get()))
    for row in cursor:
        print(row)
        lbox.insert(0, row)

def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)

def saveList():
    y = Toplevel(root, width=300, height=300)
    login = Entry(y)
    login.pack(anchor=N)
    password = Entry(y)
    password.pack(anchor=N)
    loginper = login.get()
    passper = password.get()
    # create_ticket(loginper,passper)
    enter = Button(y, text="Enter", command=lambda: registr(login.get(), password.get()))
    enter = Button(y, text="Enter", command=lambda: create_ticket(login.get(), password.get()))
    enter.pack(fill=X)
    root.mainloop()

def registr(loginper, passper):
    print(loginper)
    print(passper)
    print('your login is ' + loginper + ' ' + passper)
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "CREATE TABLE " + loginper + " (Login varchar(255),Password varchar(255));"
        sqlkey = "INSERT INTO " + loginper + " VALUES (" + "'" + loginper + "'" + "," + "'" + passper + "'" + ")"
        cursor.execute(sql)
        cursor.execute(sqlkey)
        conn.commit()
        print('База данных создана')
    except:
        print('Ошибка вероятнее база уже есть или удалена ')


def create():
    b = Toplevel(root, width=400, height=400)
    key = Entry(b)
    key.pack(anchor=N)
    keys = key.get()
    enterkey = Button(b, text="Добавить", command=lambda: create_ticket(key.get()))
    enterkey.pack(fill=X)
    root.mainloop()


def create_ticket(keys, loginper, passper):
    print(keys)
    lbox.delete(0, END)
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "INSERT INTO " + keys + " VALUES (" + "'" + "Пользователь " + "'" + "," + "'" + "Вошел " + "'" + ")"
    cursor.execute(sql)
    conn.commit()
    for row in cursor:
        print(row)
        lbox.insert(0, row)


root = Tk()
root.geometry('600x400+200+100')
root.title('Vhod v BD')

lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
entry2 = Entry(f)
entry2.pack(anchor=N)
badd = Button(f, text="Отобразить", command=addItem)
badd.pack(fill=X)
bdel = Button(f, text="Удалить", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Регистрация", command=saveList)
bsave.pack(fill=X)
bcreate = Button(f, text="Создать заметку", command=create)
bcreate.pack(fill=X)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = "SELECT * FROM Persons"
cursor.execute(sql)
for row in cursor:
    lbox.insert(0, row)

root.mainloop()

##################№№№№№№№№№№№№№№№########################
