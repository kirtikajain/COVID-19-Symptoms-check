import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from tkinter import *

window = Tk()

window.geometry('2000x1400')
window.configure(bg='misty rose')
window.title('COVID_TEST')
bget1 = 0
bget2 = 0
bget3 = 0
bget4 = 0
bget5 = 0
bget6 = 0
bget7 = 0
bget8 = 0
bget9 = 0
bget10 = 0
bget11 = 0
bget12 = 0

age=0
male=0
female=0

def bget():
    global bget1
    bget1=1
    print (bget1)
def bget0():
    global bget2
    bget2=1
    print (bget2)
def bgeta():
    global bget3
    bget3=1
    print (bget3)
def bgetb():
    global bget4
    bget4=1
    print (bget4)
def bgetc():
    global bget5
    bget5=1
    print (bget5)
def bgetd():
    global bget6
    bget6=1
    print (bget6)
def bgete():
    global bget7
    bget7=1
    print (bget7)
def bgetf():
    global bget8
    bget8=1
    print (bget8)
def bgetg():
    global bget9
    bget9=1
    print (bget9)
def bgeth():
    global bget10
    bget10=1
    print (bget10)
def bgeti():
    global bget11
    bget11=1
    print (bget11)
def bgetj():
    global bget12
    bget12=1
    print (bget12)

def get_me():
    global age
    global gender
    age=entry1.get()
    gender=entry2.get()
    if(gender=="male" or gender=="MALE" or gender=="Male"):
        male=1
        female=0
    else:
        male=0
        female=1
    print(age)
    print(gender)  

l=Label(text="Please enter your age",font=8,fg='#646060',bg='misty rose').grid(row=2,column=1,sticky=W)
entry1 = Entry(window)
entry1.grid(row=2,column=2,sticky=W)
entry2 = Entry(window)
entry2.grid(row=4,column=2,sticky=W)

#B1=Button(text='GET',command=get_me).grid(row=4,column=3)


j=StringVar()

B2=Button(text='ENTER',width=9,height=2,bg='lavender blush',fg='black',activebackground='black',command=lambda:[ent1(),get_me(),pre()],activeforeground='white',bd=10,relief=RAISED,cursor='arrow').grid(row=12,column=4)
def ent1():
    n=j.get()
    
    dataset = pd.read_csv('COVID19_data.csv')
    x=dataset.iloc[:,1:-1].values
    y=dataset.iloc[:,-1].values
    x.astype(float)
    y.astype(float)
    clas=LogisticRegression()
    clas.fit(x,y)

    #INPUT
    if bget1==1:
        fever=1
    else:
        fever=0
            
    if bget2==1:
        cough=1
    else:
        cough=0

    if bget3==1:
        SoB=1
    else:
        SoB=0

    if bget4==1:
        ST=1
    else:
        ST=0

    if bget5==1:
        chills=1
    else:
        chills=0

    if bget6==1:
        MP=1
    else:
        MP=0

    if bget7==1:
        nausea=1
    else:
        nausea=0

    if bget8==1:
        diarrhoea=1
    else:
        diarrhoea=0

    if bget9==1:
        fatigue=1
    else:
        fatigue=0

    if bget10==1:
        vomiting=1
    else:
        vomiting=0

    if bget11==1:
        headache=1
    else:
        headache=0

    if bget12==1:
        malaise=1
    else:
        malaise=0
   

    xinp = []
    xinp.append(male)
    xinp.append(female)
    xinp.append(age)
    xinp.append(fever)
    xinp.append(cough)
    xinp.append(SoB)
    xinp.append(ST)
    xinp.append(chills)
    xinp.append(MP)
    xinp.append(nausea)
    xinp.append(diarrhoea)
    xinp.append(fatigue)
    xinp.append(vomiting)
    xinp.append(headache)
    xinp.append(malaise)


    xinp_np = np.array(xinp)
    xinp_np = xinp_np.reshape(1, 15)
    
    ypred = clas.predict_proba(xinp_np)
    print(ypred)
    ypred = ypred.reshape(2, 1)
    print(ypred[1])
    l3=Label(text="YOUR CHANCE OF TESTING POSITIVE=",font=6,bg='misty rose').grid(row=14,column=1,sticky=E)
    l33 = Label(text=ypred[1]*100,font=5,bg='coral1').grid(row=14,column=2,sticky=W)
def callback():
    b2['bg']="black"
    b2['fg']="white"
def callback1():
    b3['bg']="black"
    b3['fg']="white"
def callback2():
    b4['bg']="black"
    b4['fg']="white"
def callback3():
    b5['bg']="black"
    b5['fg']="white"
def callback4():
    b6['bg']="black"
    b6['fg']="white"
def callback5():
    b7['bg']="black"
    b7['fg']="white"
def callback6():
    b8['bg']="black"
    b8['fg']="white"
def callback7():
    b9['bg']="black"
    b9['fg']="white"
def callback8():
    b10['bg']="black"
    b10['fg']="white"
def callback9():
    b11['bg']="black"
    b11['fg']="white"
def callback10():
    b12['bg']="black"
    b12['fg']="white"
def callback11():
    b13['bg']="black"
    b13['fg']="white"
    
l1=Label(text="Select your Gender",font=8,fg='#646060',bg='misty rose').grid(row=4,column=1,sticky=W)
l2=Label(text="Please select what symptoms are you facing",font=10,fg='#646060',bg='misty rose').grid(row=7,column=1,sticky=W)
b2=Button(text="FEVER",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bget(),callback()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b2.grid(row=8,column=3,sticky=W)
b3=Button(text="COUGH",width=10,height=2,bg='lavender blush',fg='black',command=lambda:[bget0(),callback1()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b3.grid(row=8,column=4,sticky=W)
b4=Button(text="SHORTNESS OF BREATH",width=18,height=2,bg='lavender blush',fg='black',command=lambda:[bgeta(),callback2()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b4.grid(row=8,column=5,sticky=W)
b5=Button(text="SORE THROAT",width=15,height=2,bg='lavender blush',fg='black',command=lambda:[bgetb(),callback3()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b5.grid(row=10,column=5,sticky=W)
b6=Button(text="CHILLS",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgetc(),callback4()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b6.grid(row=9,column=4,sticky=W)
b7=Button(text="MUSCLE PAIN",width=11,height=2,bg='lavender blush',fg='black',command=lambda:[bgetd(),callback5()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b7.grid(row=9,column=5,sticky=W)
b8=Button(text="NAUSEA",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgete(),callback6()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b8.grid(row=10,column=3,sticky=W)
b9=Button(text="DIARRHOEA",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgetf(),callback7()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b9.grid(row=10,column=4,sticky=W)
b10=Button(text="FATIGUE",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgetg(),callback8()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b10.grid(row=9,column=3,sticky=W)
b11=Button(text="VOMITING",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgeth(),callback9()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b11.grid(row=11,column=3,sticky=W)
b12=Button(text="HEADACHE",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgeti(),callback10()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b12.grid(row=11,column=4,sticky=W)
b13=Button(text="MALAISE",width=9,height=2,bg='lavender blush',fg='black',command=lambda:[bgetj(),callback11()],activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus')
b13.grid(row=11,column=5,sticky=W)



z=StringVar()
def pre():
    o=z.get()
    l4=Label(text="Based on your scan, here are some recommendations:",font=3,bg='azure',fg='navy').grid(row=16,column=1,sticky=W)
    l5=Label(text="1.Seek immediate medical attention and get yourself tested.",font=2,bg='azure').grid(row=17,column=1,sticky=W)
    l6=Label(text="2.Please visit physician as there may be requirement for further care.",font=2,bg='azure').grid(row=18,column=1,sticky=W)
    l7=Label(text="3.COVID-19 testing may be needed at your physician's advise.",font=2,bg='azure').grid(row=19,column=1,sticky=W)
    l8=Label(text="4.Monitor your symptoms and isolate yourself",font=2,bg='azure').grid(row=20,column=1,sticky=W)
    l9=Label(text="Preventions and Precautions->",font=2,bg='cornsilk3').grid(row=21,column=5,sticky=W)
    a1=Label(text="   a) HANDS: Wash them often!!!",fg='black',bg='cornsilk2',font=3).grid(row=22,column=5,sticky=W)
    a2=Label(text="   b) ELBOWS:Cough into it!!!",fg='black',bg='cornsilk2',font=3).grid(row=23,column=5,sticky=W)
    a3=Label(text="   c) FACE: Dont touch it!!!",fg='black',bg='cornsilk2',font=3).grid(row=24,column=5,sticky=W)
    a4=Label(text="   d) SPACE: Stay more than 6ft apart!!!",fg='black',bg='cornsilk2',font=3).grid(row=25,column=5,sticky=W)
    a5=Label(text="   e) FEEL: Sick? Stay at home!!!",fg='black',bg='cornsilk2',font=3).grid(row=26,column=5,sticky=W)
    



import requests
import bs4

resno = requests.get('https://www.worldometers.info/coronavirus/')
resno.text
soupno = bs4.BeautifulSoup(resno.text, 'lxml')
casesNo = soupno.find(class_ = 'maincounter-number').get_text()
print("current no of cases globally: ",casesNo)
L9=Label(text="CORONAVIRUS SYMPTOMS CHECK",font=15,bg="misty rose",fg='black').grid(row=1,column=1,sticky=W)
l91=Label(text="Current number of cases globally:",font=5,bg='misty rose').grid(row=1,column=5,sticky=E)
l99=Label(text=casesNo,font=5,fg='white',bg='black').grid(row=1,column=6)
window.mainloop()