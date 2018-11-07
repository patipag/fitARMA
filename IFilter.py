# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:40:39 2018

@author: PPAGACZ
"""

import abc
from packets import *

class IFilter(abc.ABC):
    @abc.abstractmethod
    def process(self):
        pass



