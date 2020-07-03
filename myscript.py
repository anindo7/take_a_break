# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

from pynput import mouse, keyboard
import time
import win32api
import tkinter
import subprocess

ti=20

def change():
    global ti
    ti=int(en.get())

win=tkinter.Tk()
tkinter.Label(win, text="You have used your computer for"+str(ti)+"minutes").grid(row=0)
tkinter.Label(win, text="Take a break").grid(row=1)
tkinter.Label(win, text="If you want to change the time interval, enter new time").grid(row=3)
en=tkinter.Entry(win)
en.grid(row=3,column=1)
tkinter.Button(win,text="Change",command=change).grid(row=3, column=2)
tkinter.Button(win, text="OK", command=win.destroy).grid(row=5)
tkinter.Button(win, text="CANCEL", command=win.destroy).grid(row=5,column=1)

ttime=0
ltime=0
c=0


def fn(x,y,button, pressed):
    global c
    global ttime
    global ltime
    if pressed:
        print(x,y)
        print(button)
        if c==0:
            ltime=int(time.time())
            ttime=0
            c=1
            print('1')
        else:
            if int(time.time())-ltime > 60:
                ltime=int(time.time())
                ttime=0
                print('2')
            else:
                ttime+=int(time.time())-ltime
                ltime=int(time.time())
                print('3')
                if ttime>60:
                    ttime=0
                    c=0
                    #listener.wait()
                    #listener1.wait()
                    win.update()
                    #result=win32api.MessageBox(0,'You have used the computer for 1 min. Your computer will lock in 15 seconds','alert',1)
                    #if int(result)==1:
                        #subprocess.call(["shutdown","/h","/t","15"])
                    print('4')
        #print(time.time())

def press(key):
    print(key)
    global c
    global ttime
    global ltime
    global listener
    if c==0:
            ltime=int(time.time())
            ttime=0
            c=1
            print('1')
    else:
            if int(time.time())-ltime > 60:
                ltime=int(time.time())
                ttime=0
                print('2')
            else:
                ttime+=int(time.time())-ltime
                ltime=int(time.time())
                print('3')
                if ttime>60:
                    ttime=0
                    c=0
                    #result=Tk.simpledialog.askstring('alert','You have used the computer for 1 min. Your computer will lock in 15 seconds')
                    #result=win32api.MessageBox(0,'You have used the computer for 1 min. Your computer will lock in 15 seconds','alert',1)
                    win.update()
                    #print(result)
                    #if int(result)==1:
                        #subprocess.call(["shutdown","/h","/t","15"])
                    print('4')
        #print(time.time())
    if key == keyboard.Key.esc:
        listener.stop()
        listener1.stop()

listener= mouse.Listener(on_click=fn)
listener.start()

with keyboard.Listener(on_press=press) as listener1:
    listener1.join()

