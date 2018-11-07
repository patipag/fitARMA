# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 19:32:16 2018

@author: PPAGACZ
"""

from packets import *

class WaldDecompositionPipe(IPipe):
   
    def runFilter(self):
        if(WaldDecompositionPipe.checkConditions(self.data)):
            WaldDecompositionFilter.process(self)
    
    def checkConditions(data):
        return data.orginal is not None