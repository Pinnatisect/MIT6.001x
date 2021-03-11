# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:41:15 2021

@author: selin
"""

## towers of hanoi example

def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))
    
def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1,fr,to,spare)
        Towers(n-1, spare, to, fr)
        
        
print(Towers(4,"P1","P2", "P3"))




