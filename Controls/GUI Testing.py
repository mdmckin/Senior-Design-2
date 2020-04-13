# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:36:14 2020

@author: minim
"""

import tkinter
from tkinter import *


master = Tk()
##############################################################################
tlf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="blue",
                 relief=FLAT,
                 text="TOP LEFT",
                 fg="white",
                 labelanchor=N)

blf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="red",
                 relief=FLAT,
                 text="BOTTOM LEFT",
                 fg="white",
                 labelanchor=N)

trf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="green",
                 relief=FLAT,
                 text="TOP RIGHT",
                 fg="white",
                 labelanchor=N)

brf = LabelFrame(master,
                 height=100,
                 width=100,
                 bg="black",
                 relief=FLAT,
                 text="BOTTOM RIGHT",
                 fg="white",
                 labelanchor=N)

tlb = Button(tlf, text="OKAY")
trb = Button(trf, text="OKAY")
blb = Button(blf, text="OKAY")
brb = Button(brf, text="OKAY")

tlb.grid(row=2)
trb.grid(row=2)
blb.grid(row=2)
brb.grid(row=2)

tle = Entry(tlf, width=15)
tre = Entry(trf, width=15)
ble = Entry(blf, width=15)
bre = Entry(brf, width=15)

tle.grid(row=0)
tre.grid(row=0)
ble.grid(row=0)
bre.grid(row=0)

tld = Frame(tlf, height=5, bg="blue")
trd = Frame(trf, height=5, bg="green")
bld = Frame(blf, height=5, bg="red")
brd = Frame(brf, height=5, bg="black")

tld.grid(row=1)
trd.grid(row=1)
bld.grid(row=1)
brd.grid(row=1)

tlf.grid_propagate(0)
blf.grid_propagate(0)
trf.grid_propagate(0)
brf.grid_propagate(0)

tlf.grid(row=0, column=0)
trf.grid(row=0, column=1)
blf.grid(row=1, column=0)
brf.grid(row=1, column=1)

##############################################################################
mainloop()