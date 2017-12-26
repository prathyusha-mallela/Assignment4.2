# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:15:07 2017

@author: Prathyusha Mallela
"""

#Assignment 4.2.1
def getElementLength(lst):
    lenlst=[]
    for x in lst:
        #print(len(x))
        lenlst.append(len(x))
    return lenlst;

lst=['a','ab','cde','defg','hi']
z=getElementLength(lst)
print(z)