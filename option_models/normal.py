# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:56:58 2017

@author: jaehyuk
"""

class NormalModel:
    
    '''
    <-- class variables here
    '''
    
    def __init__(self):
        ''' 
        <-- PUT your implementation here
        '''
        pass
    
    def price(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp_sign=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0
    
    def delta(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp_sign=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def vega(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp_sign=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def gamma(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp_sign=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def impvol(self, price, strike, spot, texp, cp_sign=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0