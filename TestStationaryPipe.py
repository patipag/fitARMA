# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:45:39 2018

@author: PPAGACZ
"""

from packets import *

class TestStationaryPipe(IPipe):
   
    def runFilter(self):
        if(TestStationaryPipe.checkConditions(self.data)):
            TestStationaryFilter.process(self)
    
    def checkConditions(data):
        return data.orginal is not None
        