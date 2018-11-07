# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:42:43 2018

@author: PPAGACZ
"""

class Data:
  def __init__(self, orginal):
    self.orginal = orginal
    self.waldDecomposition = None
    self.differencing = None
    self.last = orginal
    self.modelARMA = None