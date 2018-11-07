# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:14:41 2018

@author: PPAGACZ
"""

from packets import *

class ForecastPipe(IPipe):
   
    def runFilter(self):
        if(ForecastPipe.checkConditions(self.data)):
            ForecastFilter.process(self)
    
    def checkConditions(data):
        return True