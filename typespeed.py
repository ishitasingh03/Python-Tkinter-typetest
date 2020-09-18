

import tkinter as tk
import random
sentence=""
time=0
stop=False

def countdown():
    global stop,time
    if stop==False:
        time+=1
        l1.after(1000,countdown)
        
def startgame():
    global sentence
    global time
    time=0
    f=open('text.txt').read()
    sentences=f.split('\n')
    sentence=random.choice(sentences)
    l2.config(text=sentence)
    countdown()
    
def stopgame(event):
    global stop,time,sentence
    stop=True
    input1=e1.get()
    count=0
    for i,c in enumerate(input1):
        if(sentence[i]==c):
            count+=1
    accuracy=round((count/len(sentence))*100)
    wpm=round(len(input1)*60/(time*5))
    l3.config(text="Total time: "+str(time)+"secs  Accuracy:"+str(accuracy)+"%   wpm: "+str(wpm))
        
def reset():
    global stop,time
    stop=False
    time=0
    e1.delete(0,tk.END)
    l3.config(text="")
    startgame()
     
    

root=tk.Tk()
root.geometry('1000x600')
root.config(bg="black")
l1=tk.Label(root,text="Typing Speed Test",font=('Helvetica',50),fg='Yellow',bg="black")
l1.pack(padx=20,pady=40)
l2=tk.Label(root,text="",font=('Helvetica',30),fg='White',bg="black")
l2.pack(padx=10,pady=20)
e1=tk.Entry(root,font=('Helvetica',20),width=50)
e1.pack(padx=10,pady=20)
l3=tk.Label(root,text="",font=('Helvetica',20),fg='White',bg="black")
l3.pack(padx=20,pady=20)
b1=tk.Button(root,text="Start",bg="yellow",fg="black",font=('Helvetica',20),command=startgame)
b1.pack(padx=200,pady=20,side=tk.LEFT)
b2=tk.Button(root,text="Reset",bg="yellow",fg="black",font=('Helvetica',20),command=reset,)
b2.pack(padx=200,pady=20,side=tk.RIGHT)
root.bind('<Return>',stopgame)
root.mainloop()
