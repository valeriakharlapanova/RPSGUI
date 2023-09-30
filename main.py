from tkinter import *
import random
root = Tk()
root.geometry("300x300")
root.title("Камень-Ножницы-Бумага")
Label(root,
      text="Камень Ножницы Бумага",
      font="normal 15 bold",
      fg="blue").pack(pady=20)
frame = Frame(root)
frame.pack()
computer_value = {
    "0": "Камень",
    "1": "Бумага",
    "2": "Ножницы"
}
l1 = Label(frame,
           text="Игрок"                          ,
           font=10)
l2 = Label(frame,
           text="vs"                          ,
           font="normal 10 bold")
l3 = Label(frame, text="      Бот", font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)
frame1 = Frame(root)
frame1.pack()

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Камень":
        match_result = "НИЧЬЯ"
    elif c_v == "Ножницы":
        match_result = "ИГРОК ПОБЕДИЛ"
    else:
        match_result = "БОТ ПОБЕДИЛ"
    l4.config(text=match_result)
    l1.config(text="Камень            ")
    l3.config(text=c_v)
    button_disable()

def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Бумага":
        match_result = "НИЧЬЯ"
    elif c_v == "Ножницы":
        match_result = "ИГРОК ПОБЕДИЛ"
    else:
        match_result = "БОТ ПОБЕДИЛ"
    l4.config(text=match_result)
    l1.config(text="Бумага            ")
    l3.config(text=c_v)
    button_disable()

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Камень":
        match_result = "НИЧЬЯ"
    elif c_v == "Ножницы":
        match_result = "ИГРОК ПОБЕДИЛ"
    else:
        match_result = "БОТ ПОБЕДИЛ"
    l4.config(text=match_result)
    l1.config(text="Ножницы            ")
    l3.config(text=c_v)
    button_disable()

b1 = Button(frame1, text="Камень", font=10,
            width=7, command=isrock)
b2 = Button(frame1, text="Бумага",
            font=10, width=7,
            command=ispaper)
b3 = Button(frame1, text="Ножницы",
            font=10, width=7,
            command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="ОБНОВИТЬ",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)
root.mainloop()



