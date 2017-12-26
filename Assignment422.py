# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:16:01 2017

@author: Prathyusha Mallela
"""

#Assignment 4.2.2
def vowel_checker(letter):
    l=letter.lower()
    if l in ['a','e','i','o','u']:
        return True
    else:
        return False
    
vowel_checker('O')