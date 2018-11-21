#Autor: Tomasz Hresiukiewicz
#Data: 9.21.2018
#
#
#Brief: Program checks city communication(busses) hours




from time import gmtime, strftime

import requests

import re

from tkinter import *



okno=Tk()

url = "http://www2.zkmgdynia.pl/rozklady/0181/0181t009.htm"
headers = {"Range": "bytes=0-5000"}  # first 100 bytes
print('requests')


global jest_wifi
jest_wifi=True

try:
    r = requests.post('http://www2.zkmgdynia.pl/rozklady/0181/0181t009.htm', data = {'key':'value'})
except:
    print ("No wifi!")

    jest_wifi=False
if(jest_wifi==True):
    r = requests.post('http://www2.zkmgdynia.pl/rozklady/0181/0181t009.htm', data = {'key':'value'})



    raw_data=r.text



##################################

    pattern=re.compile(r'.\d\.\d\d')

    terminy='dane: \n'


    matches=pattern.findall(raw_data)


    nr_tablicy=0
    tablica_powszednie=[]
    tablica_soboty=[]
    tablica_swieta=[]
    godzina_popsz=0.001

    for match in matches:

        terminy+=str(match)+' \n '
        godzina1=float(match)
    
        if(godzina1<godzina_popsz):
            nr_tablicy=nr_tablicy+1

        godzina_popsz=godzina1
    
        if(nr_tablicy==0):
            tablica_powszednie.append(godzina1)
        elif(nr_tablicy==1):
            tablica_soboty.append(godzina1)
        elif(nr_tablicy==2):
            tablica_swieta.append(godzina1)
    


#################################

Label(okno, text='podaj godzine').grid(row=2, column=0)


var= IntVar()
R1=Radiobutton(okno, text='pon-pt', variable=var, value=1)
R1.grid(row=1, column=0)

R2=Radiobutton(okno, text='sob', variable=var, value=2)
R2.grid(row=1, column=1)

R3=Radiobutton(okno, text='nd, sw', variable=var, value=3)
R3.grid(row=1, column=2)



label_ile=Label(okno, text="")
label_ile.grid(column=0, row=4)


godzina_=Entry(okno)

godzina_.grid(row=2, column=1)


def pjed(event):
    if(var.get()==1):
        rozklad_dzien=tablica_powszednie
    elif(var.get()==2):
        rozklad_dzien=tablica_soboty
    else:
        rozklad_dzien=tablica_swieta

    autobusy_naj_godzine=[]

    global godzina_get
    godzina_get=(float(strftime("%H", gmtime())))+(int(strftime("%M", gmtime()))/100)+1
    label_ile.config(text="")
    for hour in rozklad_dzien:
    
        if(hour>=float(godzina_.get())-1.0 and hour<=float(godzina_.get())+1.0):
            autobusy_naj_godzine.append(str('%.2f' % float(hour)))
            autobusy_naj_godzine.append(' ')


    for moj_autobos in autobusy_naj_godzine:
        label_ile.config(text=label_ile.cget("text")+str(moj_autobos))

#print(godzina_)

guzik=Button(okno, text="szukaj", command=lambda: pjed(1))
guzik.grid(row=3, column=0)

czas_sys=Button(okno, text="najbliższe \n autobusy", command=lambda: pobierz_czas(1))
czas_sys.grid(row=0, column=1)

def pobierz_czas(event):
   
    godzina_tera=(float(strftime("%H", gmtime())))+(int(strftime("%M", gmtime()))/100)+1
    if(var.get()==1):
        rozklad_dzien=tablica_powszednie
    elif(var.get()==2):
        rozklad_dzien=tablica_soboty
    else:
        rozklad_dzien=tablica_swieta

    autobusy_naj_godzine=[]

    global godzina_get
    godzina_get=(float(strftime("%H", gmtime())))+(int(strftime("%M", gmtime()))/100)+1
    label_ile.config(text="")
    for hour in rozklad_dzien:
    
        if(hour>=godzina_tera-1.0 and hour<=godzina_tera+1.0):
            autobusy_naj_godzine.append(str(hour))
            autobusy_naj_godzine.append(' ')


    for moj_autobos in autobusy_naj_godzine:
        label_ile.config(text=label_ile.cget("text")+str(moj_autobos))
################################################################

zapisz_dane=Button(okno, text="zapisz", command=lambda: nadpisz_plik(1))
zapisz_dane.grid(row=0, column=0)

def nadpisz_plik(event):
    if(jest_wifi==True):
        f=open('rozklad_autobosow.txt', 'w')
        f.write(str(matches))
        f.close()
    else:
        print('nie mozna nadpisac nie ma wifi')
    

odczytaj_dane=Button(okno, text="szukaj \n offline", command=lambda: czytaj_plik(1))
odczytaj_dane.grid(row=3, column=1)

def czytaj_plik(event):
    global jest_plik
    jest_plik=True
    try:
        g=open('rozklad_autobosow.txt')
        g.close()
    except:
        jest_plik=False
        print('Nie ma pliku')

    if(jest_plik==True):
        g=open('rozklad_autobosow.txt')
        raw_data=g.read()
        pattern=re.compile(r'.\d\.\d\d')
        terminy='dane: \n'
        nr_tablicy=0
        tablica_powszednie=[]
        tablica_soboty=[]
        tablica_swieta=[]
        godzina_popsz=0.001
        matches=pattern.findall(raw_data)
        for match in matches:
        
            terminy+=str(match)+' \n '
            godzina1=float(match)
    
            if(godzina1<godzina_popsz):
                nr_tablicy=nr_tablicy+1

            godzina_popsz=godzina1
    
            if(nr_tablicy==0):
                tablica_powszednie.append(godzina1)
            elif(nr_tablicy==1):
                tablica_soboty.append(godzina1)
            elif(nr_tablicy==2):
                tablica_swieta.append(godzina1)
        if(var.get()==1):
            rozklad_dzien=tablica_powszednie
        elif(var.get()==2):
            rozklad_dzien=tablica_soboty
        else:
            rozklad_dzien=tablica_swieta

        autobusy_naj_godzine=[]
        global godzina_get
        godzina_get=(float(strftime("%H", gmtime())))+(int(strftime("%M", gmtime()))/100)+1

        label_ile.config(text="")
        for hour in rozklad_dzien:
            if(hour>=float(godzina_.get())-1.0 and hour<=float(godzina_.get())+1.0):
                autobusy_naj_godzine.append(str('%.2f' % float(hour)))
                autobusy_naj_godzine.append(' ')

        for moj_autobos in autobusy_naj_godzine:
            label_ile.config(text=label_ile.cget("text")+str(moj_autobos))
    
        g.close()

################################################################
