# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:25:33 2018

@author: PPAGACZ
"""

import abc
from packets import *

class IPipe(abc.ABC):
    
    @abc.abstractmethod
    def runFilter(self):
        pass
    
    @abc.abstractmethod
    def checkConditions(data):
        pass