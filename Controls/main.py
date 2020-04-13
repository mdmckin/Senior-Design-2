"""
Created on Wed Apr  7 12:22:08 2020

@author: minim
"""

# Standard Imports
import tkinter
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# Module Imports
import control

#Global Variables
global time
time = None
global tune
tune = 2


# Creates and saves Temperature VS Time Graph
def Temp_Graph(temp, time):
    
    plt.plot(time, temp, color="#E16600")
    plt.xlabel("Time (Years)")
    plt.ylabel("Temperature (K)")
    plt.ylim(1200,1800)
    plt.title("Temperature VS Time")
    plt.savefig("Temp_Graph")
    plt.figure()
    
    return

# Creates and saves Power VS Time Graph
def Power_Graph(power, time):

    plt.plot(time, power, "r")
    plt.xlabel("Time (Years)")
    plt.ylabel("Power (MW)")
    plt.ylim(200,600)
    plt.title("Power VS Time")
    plt.savefig("Power_Graph")    
    plt.figure()
    
    return

# Creates and saves Pressure VS Time Graph
def Pressure_Graph(pressure, time):
    
    plt.plot(time, pressure)
    plt.xlabel("Time (Years)")
    plt.ylabel("Pressure (MPa)")
    plt.ylim(10,23)
    plt.title("Pressure VS Time")
    plt.savefig("Pressure_Graph")    
    plt.figure()
    
    return

# Creates and saves Purity VS Time Graph
def Purity_Graph(purity, time):
    
    plt.plot(time, purity, color="#55FF55")
    plt.xlabel("Time (Years)")
    plt.ylabel("Purity (%)")
    plt.ylim(70,100)
    plt.title("Purity VS Time")
    plt.savefig("Purity_Graph")    
    plt.figure()
    
    return

# Sets time variable to 5 years
def Five_Years():
    global time
    time=int(5*tune)
    return

# Sets time variable to 10 years
def Ten_Years():
    global time
    time=int(10*tune)
    return

# Sets time variable to 20 years
def Twenty_Years():
    global time
    time=int(20*tune)
    return

# Opens Input window
def Input():
    global time
    global tune
    
    window = Tk()
    
    title = Label(window, text="MSRE Simulation", font=("Times New Roman", 16)).grid(row=0,columnspan=2)
    
    button_title = Label(text="Reactor runtime:").grid(row=1)
    v = IntVar()
    Radiobutton(text="5 years", variable=v, value=1,
                command=Five_Years).grid(row=2)
    Radiobutton(text="10 years", variable=v, value=2,
                command=Ten_Years).grid(row=3)
    Radiobutton(text="20 years", variable=v, value=3,
                command=Twenty_Years).grid(row=4)
    
    run = Button(text="Run Simulation", command=window.destroy).grid(row=5, column=0, sticky=E, pady=5, padx=50)
    
    mainloop()
    
    
    return

# Creates simluation Output
def Output():
    global mma
    
    graph_window = Tk()
    
    title = Label(text="Simulation Results", font=("Times New Roman", 20, "bold")).grid(row=0, columnspan=8)
    
    # Correctly formats each section of the Output window
    ##########################################################################
    Temp_Image = PhotoImage(file="Temp_Graph.png")
    TempG = Label(image=Temp_Image).grid(row=1,column=0,columnspan=4)
    TempMaxL = Label(text="Max Temp:",bg="#F94F5B").grid(row=2,column=0,sticky=E)
    TempMax = Label(text=mma[0],bg="#F94F5B").grid(row=2,column=1,sticky=W)
    TempMinL = Label(text="Min Temp:",bg="#CFFCFF").grid(row=2,column=2,sticky=E)
    TempMin = Label(text=mma[1],bg="#CFFCFF").grid(row=2,column=3,sticky=W)
    TempAvgL = Label(text="Average Temp:").grid(row=3,column=0,columnspan=2,sticky=E)
    TempAvg = Label(text=mma[2]).grid(row=3,column=2,columnspan=2,sticky=W)
    
    Power_Image = PhotoImage(file="Power_Graph.png")
    PowerG = Label(image=Power_Image).grid(row=1,column=4,columnspan=4)
    PowerMaxL = Label(text="Max Power:",bg="#F94F5B").grid(row=2,column=4,sticky=E)
    PowerMax = Label(text=mma[3],bg="#F94F5B").grid(row=2,column=5,sticky=W)
    PowerMinL = Label(text="Min Power:",bg="#CFFCFF").grid(row=2,column=6,sticky=E)
    PowerMin = Label(text=mma[4],bg="#CFFCFF").grid(row=2,column=7,sticky=W)
    PowerAvgL = Label(text="Average Power:").grid(row=3,column=4,columnspan=2,sticky=E)
    PowerAvg = Label(text=mma[5]).grid(row=3,column=6,columnspan=2,sticky=W)
    
    Pressure_Image = PhotoImage(file="Pressure_Graph.png")
    PressureG = Label(image=Pressure_Image).grid(row=4,column=0,columnspan=4)
    PressureMaxL = Label(text="Max Pressure:",bg="#F94F5B").grid(row=5,column=0,sticky=E)
    PressureMax = Label(text=mma[6],bg="#F94F5B").grid(row=5,column=1,sticky=W)
    PressureMinL = Label(text="Min Pressure:",bg="#CFFCFF").grid(row=5,column=2,sticky=E)
    PressureMin = Label(text=mma[7],bg="#CFFCFF").grid(row=5,column=3,sticky=W)
    PressureAvgL = Label(text="Average Pressure:").grid(row=6,column=0,columnspan=2,sticky=E)
    PressureAvg = Label(text=mma[8]).grid(row=6,column=2,columnspan=2,sticky=W)
    
    Purity_Image = PhotoImage(file="Purity_Graph.png")
    PurityG = Label(image=Purity_Image).grid(row=4,column=4,columnspan=4)
    PurityMaxL = Label(text="Max Purity:",bg="#F94F5B").grid(row=5,column=4,sticky=E)
    PurityMax = Label(text=mma[9],bg="#F94F5B").grid(row=5,column=5,sticky=W)
    PurityMinL = Label(text="Min Purity:",bg="#CFFCFF").grid(row=5,column=6,sticky=E)
    PurityMin = Label(text=mma[10],bg="#CFFCFF").grid(row=5,column=7,sticky=W)
    PurityAvgL = Label(text="Average Purity:").grid(row=6,column=4,columnspan=2,sticky=E)
    PurityAvg = Label(text=mma[11]).grid(row=6,column=6,columnspan=2,sticky=W)
    ##########################################################################
    
    b = Button(text="Exit", command=graph_window.destroy).grid(row=7, columnspan=8, pady=5)
    
    mainloop()
    
    
    return

# Function that will be used to initiate the calculative iterations and obtain data
def Data_Processing():
    global time
    global mma
    global tune
    
    data = control.Run_Sim(time)
    
    temp = data[0]
    power = data[1]
    pressure = data[2]
    purity = data[3]
    
    time_array = np.zeros(time)
    
    i = 0
    while (i < time):
        time_array[i] = i + 1
        i = i + 1
        
    time_array = time_array/tune
    
    Temp_Graph(temp, time_array)
    Power_Graph(power, time_array)
    Pressure_Graph(pressure, time_array)
    Purity_Graph(purity, time_array)
    
    mma = np.zeros(12)
    mma[0] = max(temp)
    mma[1] = min(temp)
    mma[2] = sum(temp)/time
    mma[3] = max(power)
    mma[4] = min(power)
    mma[5] = sum(power)/time
    mma[6] = max(pressure)
    mma[7] = min(pressure)
    mma[8] = sum(pressure)/time
    mma[9] = max(purity)
    mma[10] = min(purity)
    mma[11] = sum(purity)/time
    
    return

# Alerts the user when no input was detected
def Error_Message():
    
    error = Tk()
    
    message = Label(text="Reactor runtime was not chosen.", padx=10,pady=10).pack()
    message2 = Label(text="Please try again.", padx=10,pady=10).pack()
    
    mainloop()
    
    return

# Used to run this script from an outside file
def RunGUI():
    Input()
    if not (time == None):
        Data_Processing()
        Output()
    else:
        Error_Message()    
    return

if __name__ == "__main__":
    Input()
    if not (time == None):
        Data_Processing()
        Output()
    else:
        Error_Message()