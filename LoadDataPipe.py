# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:30:27 2018

@author: PPAGACZ
"""

from packets import *

class LoadDataPipe(IPipe):
   
    def runFilter(self):
        if(LoadDataPipe.checkConditions(self.data)):
            LoadDataFilter.process(self)
    
    def checkConditions(data):
        return True
        
