# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:45:02 2020

@author: minim
"""


import tkinter
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


master = Tk()

def Make_Graph():
    x_str = x_entry.get()
    y_str = y_entry.get()
    
    if not (len(x_str)==len(y_str)):
        return None
    
    x = []
    y = []
    i = 0
    
    while (i < len(x_str)):
        x.append(float((x_str[i])))
        y.append(float((y_str[i])))
        i = i + 2
        
    plt.plot(x,y)
    plt.savefig(fname="graph")
    
    graph_window = wait_window()
    
    photo = PhotoImage(graph_window, file="graph.png")
    graph = Label(graph_window, image=photo)
    
    graph.pack()
    
    
def Test():
    x_str = x_entry.get()
    y_str = y_entry.get()
    
    if not (len(x_str)==len(y_str)):
        return None
    
    x = []
    y = []
    i = 0
    
    while (i < len(x_str)):
        x.append(float((x_str[i])))
        y.append(float((y_str[i])))
        i = i + 2
    
    print(x)
    print(y)


button = Button(text="Make Graph", command=Make_Graph)
button_test = Button(text="Test", command=Test)
x_entry = Entry(text="X Values")
y_entry = Entry(text="Y Values")

title = Label(text="Graph")

title.pack()
x_entry.pack()
y_entry.pack()
button.pack()
button_test.pack()


mainloop()