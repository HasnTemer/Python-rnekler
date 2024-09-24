from tkinter import *
from tkinter import messagebox
import random

tk = Tk()
tk.title("PENCERE")
tk.geometry("800x450")

zar_resim = PhotoImage(file="zarlar.png")
resim1 = PhotoImage(file="1.png")
resim2 = PhotoImage(file="2.png")
resim3 = PhotoImage(file="3.png")
resim4 = PhotoImage(file="4.png")
resim5 = PhotoImage(file="5.png")
resim6 = PhotoImage(file="6.png")

Label(tk, text="Python Deneme").pack()
Label(tk, text="Hasan Semih Temer", font="Times 12 bold").pack()


zar_label = Label(tk, image=zar_resim)
zar_label.place(x=250, y=100)

zar_label2 = Label(tk, image="")
zar_label2.place(x=550, y=100)

def fonksiyon():
    bilgi = entry.get()
    messagebox.showinfo("Bilgilendirme", bilgi)

def random_sayi_uret():
    rs = random.randint(1, 6)
    rs2 = random.randint(1, 6)
    if rs == 1:
        zar_label.config(image=resim1)
    elif rs == 2:
        zar_label.config(image=resim2)
    elif rs == 3:
        zar_label.config(image=resim3)
    elif rs == 4:
        zar_label.config(image=resim4)
    elif rs == 5:
        zar_label.config(image=resim5)
    elif rs == 6:
        zar_label.config(image=resim6)

    if rs2 == 1:
        zar_label2.config(image=resim1)
    elif rs2 == 2:
        zar_label2.config(image=resim2)
    elif rs2 == 3:
        zar_label2.config(image=resim3)
    elif rs2 == 4:
        zar_label2.config(image=resim4)
    elif rs2 == 5:
        zar_label2.config(image=resim5)
    elif rs2 == 6:
        zar_label2.config(image=resim6)

btn = Button(tk, text="Çalıştır", bg="green", padx="20", pady="10", activebackground="brown", command=fonksiyon)
btn.place(x=20, y=40)

btn2 = Button(tk, text="Rastgele Sayı", bg="green", padx="20", pady="10", activebackground="brown", command=random_sayi_uret)
btn2.place(x=20, y=100)

entry = Entry(tk, width=20)
entry.pack()

tk.mainloop()
