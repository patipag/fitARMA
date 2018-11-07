# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:23:16 2018

@author: PPAGACZ
"""

from packets import *

class FitARMAPipe(IPipe):
   
    def runFilter(self):
         if(FitARMAPipe.checkConditions(self.data)):
            FitARMAFilter.process(self)
    
    def checkConditions(data):
        return data.orginal is not None
        
 