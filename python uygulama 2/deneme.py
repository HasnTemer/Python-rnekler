from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title(" PENCERE ")
tk.geometry("400x250")
Label(tk,text="Python Deneme").pack()

Label(tk,text="Hasan Semih Temer",font="Times 12 bold").pack()

def fonksiyon():
    bilgi = entry.get()
    messagebox.showinfo("Bilgilendirme",bilgi)

btn = Button(tk,text="Tıkla",bg="gray",padx="20",pady="10", activebackground="red", command=fonksiyon)
btn.place(x="40",y="70")


entry = Entry(tk,width=20)
entry.pack()


tk.mainloop()