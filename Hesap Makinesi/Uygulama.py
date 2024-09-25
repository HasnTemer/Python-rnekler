import tkinter
from tkinter import *
tk = Tk()
tk.title("-- Hesap Makinesi --")
tk.geometry("450x470+200+100")
tk.resizable(False,False)
tk.configure(bg="#17161b")

label_sonuc =Label(tk,width=20,height=2,text="",font=("arial",30))
label_sonuc.pack()

def sonuc():
    global ek 
    cevap = ""
    if ek != "":
        try:
            cevap = eval(ek)
            ek = ""
        except:
            cevap = " ! HATA ! "
            ek = ""
    ek = f"{cevap}"
    label_sonuc.config(text=cevap)
def clear():
    global ek
    ek = ""
    label_sonuc.config(text=ek)
def show(x):
    global ek
    ek+=x
    label_sonuc.config(text=ek)

ek = ""

    


Button(tk, text="C" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="orange", command=lambda:clear()).place(x=15,y=100)
Button(tk, text="/" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="#2a2d56",command=lambda:show("/")).place(x=120,y=100)
Button(tk, text="%" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="#2a2d56",command=lambda:show("%")).place(x=225,y=100)
Button(tk, text="X" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="#2a2d56",command=lambda:show("*")).place(x=330,y=100)

Button(tk, text="7" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("7")).place(x=15,y=170)
Button(tk, text="8" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("8")).place(x=120,y=170)
Button(tk, text="9" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("9")).place(x=225,y=170)
Button(tk, text="-" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="#2a2d56",command=lambda:show("-")).place(x=330,y=164)

Button(tk, text="4" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("4")).place(x=15,y=240)
Button(tk, text="5" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("5")).place(x=120,y=240)
Button(tk, text="6" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("6")).place(x=225,y=240)
Button(tk, text="+" ,width=5,height=1 , font=("arial",23,"bold"), bd = 1 ,fg="gray",bg="#2a2d56",command=lambda:show("+")).place(x=330,y=228)

Button(tk, text="1" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("1")).place(x=15,y=310)
Button(tk, text="2" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("2")).place(x=120,y=310)
Button(tk, text="3" ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("3")).place(x=225,y=310)
Button(tk, text="=" ,width=5,height=3 , font=("arial",23,"bold"), bd = 1 ,fg="black",bg="gray",command=lambda:sonuc()).place(x=330,y=310)

Button(tk, text="0" ,width=9,height=1 , font=("arial",25,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show("0")).place(x=15,y=375)
Button(tk, text="." ,width=5,height=1 , font=("arial",20,"bold"), bd = 1 ,fg="gray",bg="#2a2d96",command=lambda:show(".")).place(x=225,y=375)





tk.mainloop()
