# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 19:51:58 2018

@author: PPAGACZ
"""

from packets import *


class DifferencingPipe(IPipe):
   
    def runFilter(self):
        if(DifferencingPipe.checkConditions(self.data)):
            DifferencingFilter.process(self)
    
    def checkConditions(data):
        return data.orginal is not None