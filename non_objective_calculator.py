#################################
#Tomasz Hresiukiewicz 13.08.2018#
#################################

from tkinter import *
from tkinter import ttk
gui=Tk()


gui.title("apk test")

####################################################

def pjedynka(licz):
#    print(licz)
    label_ile.config(text=label_ile.cget("text")+licz)
##

def operacja(z):
    global wartosc
    wartosc=float(label_ile.cget("text"))
    print(wartosc)
    label_ile.config(text="")
    global znak
    znak=z

##

def wynik(g):
    print(g)
    if(znak=="+"):
        wartosc2=float(label_ile.cget("text"))
        jaki_wynik=str(wartosc+wartosc2)
        label_ile.config(text=jaki_wynik)
    elif(znak=="-"):
        wartosc2=float(label_ile.cget("text"))
        jaki_wynik=str(wartosc-wartosc2)
        label_ile.config(text=jaki_wynik)
    elif(znak=="*"):
        wartosc2=float(label_ile.cget("text"))
        jaki_wynik=str(wartosc*wartosc2)
        label_ile.config(text=jaki_wynik)
    elif(znak=="/"):
        wartosc2=float(label_ile.cget("text"))
        jaki_wynik=str(wartosc/wartosc2)
        label_ile.config(text=jaki_wynik)
    elif(znak=="%"):
        wartosc2=float(label_ile.cget("text"))
        jaki_wynik=str(wartosc%wartosc2)
        label_ile.config(text=jaki_wynik)
    else:
        print("error")
    
######
    
label_ile=ttk.Label(gui, text="")
label_ile.grid(column=0, row=0)

jedynka=ttk.Button(gui, text="1", command=lambda: pjedynka("1"))
jedynka.grid(row=1, column=0)

dwojka=ttk.Button(gui, text="2", command=lambda: pjedynka("2"))
dwojka.grid(row=1, column=1)

trojka=ttk.Button(gui, text="3", command=lambda: pjedynka("3"))
trojka.grid(row=1, column=2)

czworka=ttk.Button(gui, text="4", command=lambda: pjedynka("4"))
czworka.grid(row=2, column=0)

piatka=ttk.Button(gui, text="5", command=lambda: pjedynka("5"))
piatka.grid(row=2, column=1)

szostka=ttk.Button(gui, text="6", command=lambda: pjedynka("6"))
szostka.grid(row=2, column=2)

siodemka=ttk.Button(gui, text="7", command=lambda: pjedynka("7"))
siodemka.grid(row=3, column=0)

osemka=ttk.Button(gui, text="8", command=lambda: pjedynka("8"))
osemka.grid(row=3, column=1)

dziewiatka=ttk.Button(gui, text="9", command=lambda: pjedynka("9"))
dziewiatka.grid(row=3, column=2)

zero=ttk.Button(gui, text="0", command=lambda: pjedynka("0"))
zero.grid(row=1, column=3)

######

plus=ttk.Button(gui, text="+", command=lambda: operacja("+"))
plus.grid(row=2, column=3)

plus=ttk.Button(gui, text="-", command=lambda: operacja("-"))
plus.grid(row=3, column=3)

plus=ttk.Button(gui, text="*", command=lambda: operacja("*"))
plus.grid(row=4, column=0)

plus=ttk.Button(gui, text="/", command=lambda: operacja("/"))
plus.grid(row=4, column=1)

plus=ttk.Button(gui, text="%", command=lambda: operacja("%"))
plus.grid(row=4, column=2)

rowna=ttk.Button(gui, text="=", command=lambda: wynik(1))
rowna.grid(row=4, column=3)

####################################################


gui.mainloop()
