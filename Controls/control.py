"""
Created on Wed Apr  7 13:20:48 2020

@author: minim
"""

import numpy as np

def Run_Sim(time):
    # THE FOLLOWING CODE IS DESIGNED TO CREATE EXAMPLE GRAPHS.
    # CODE IS NOT RESPRESENTATIVE OF THE FINAL PRODUCT.
    
    data = [0,0,0,0]   
    
    data[0] = np.random.randint(low=1400, high=1600, size=time)
    data[1] = np.random.randint(low=350, high=450, size=time)
    data[2] = np.random.randint(low=15, high=18, size=time)
    data[3] = np.random.randint(low=80, high=100, size=time)
    
    return data

if (__name__ == "__main__"):
    data = Run_Sim(20)