# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:53:44 2018

@author: PPAGACZ
"""

from packets import *

class ResidualsPipe(IPipe):
   
    def runFilter(self):
         if(ResidualsPipe.checkConditions(self.data)):
            ResidualsFilter.process(self)
    
    def checkConditions(data):
        return True
        