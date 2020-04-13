# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:13:05 2020

@author: minim
"""


import tkinter
from tkinter import *


master = Tk()
##############################################################################
tlf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="green",
                 relief=FLAT,
                 text="INPUT",
                 fg="white",
                 labelanchor=N)

trf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="black",
                 relief=FLAT,
                 text="OUTPUT",
                 fg="white",
                 labelanchor=N)

tle = Entry(tlf, width=15, text="0", justify=CENTER)

ans = StringVar()
tre = Label(trf, width=13, textvariable=ans)


def Multiply():
    n = int(tle.get())
    ans_int = n*n
    ans.set(str(ans_int))


tlb = Button(tlf, text="Calculate", command=Multiply)
trb = Button(trf, text="Done", command=master.destroy)

tlb.grid(row=2)
trb.grid(row=2)





tle.grid(row=0)
tre.grid(row=0)

tld = Frame(tlf, height=5, bg="green")
trd = Frame(trf, height=5, bg="black")


tld.grid(row=1)
trd.grid(row=1)


tlf.grid_propagate(0)

trf.grid_propagate(0)

tlf.grid(row=0, column=0)
trf.grid(row=0, column=1)

##############################################################################
mainloop()