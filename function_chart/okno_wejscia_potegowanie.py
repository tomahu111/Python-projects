from tkinter import *

##################################

entry_window=Tk()


wzor=Label(entry_window, text='f(x)=a*x+b')
wzor.grid(row=0, column=0)

txt_a=Label(entry_window, text='a=')
txt_a.grid(row=1, column=0, sticky=E)
get_a=Entry(entry_window)
get_a.grid(row=1, column=1)

txt_b=Label(entry_window, text='b=')
txt_b.grid(row=2, column=0, sticky=E)
get_b=Entry(entry_window)
get_b.grid(row=2, column=1)








##################################


ready=Button(entry_window, text="submit", command=lambda: pobierz_argumenty(1))
ready.grid(row=3, column=0)

def pobierz_argumenty(event):
    a=float(get_a.get())
    b=float(get_b.get())
    import wkres
    wkres.rysownik_wykresu.up()
    wkres.rysownik_wykresu.goto(-200, a*-200+b)
    wkres.rysownik_wykresu.down()
    for i in range(-200, 200):
        xi=float(i)
        yi=a*xi+b
#        print("----")
#        print(xi)
#        print(yi)
#        print("----")
        wkres.rysowanie(xi, yi)

