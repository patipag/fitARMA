# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:56:20 2018

@author: PPAGACZ
"""
import pytest
from LoadDataFilter import *

from unittest import TestCase

class Test_LoadDataFilter(TestCase):

    def test_data_format(self):
        series = pd.read_csv('AirPassengers.csv')
        assert LoadDataFilter.checkCondition(series) == True

    def test_data_wrong_format(self):
        series = pd.read_csv('wrong_data.csv')
        assert LoadDataFilter.checkCondition(series) == False