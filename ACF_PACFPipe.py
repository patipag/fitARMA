# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:06:15 2018

@author: PPAGACZ
"""

from packets import *

class ACF_PACFPipe(IPipe):
   
    def runFilter(self):
        if(ACF_PACFPipe.checkConditions(self.data)):
            ACF_PACFFilter.process(self)
    
    def checkConditions(data):
        return data.orginal is not None