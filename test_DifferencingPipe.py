# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:21:44 2018

@author: PPAGACZ
"""

import pytest
from DifferencingPipe import *
from unittest import TestCase

class Test_DifferencingPipe(TestCase):

    def test_data_orignial_exist(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        assert DifferencingPipe.checkConditions(data) == True

    def test_data_orignial_not_exist(self):
        data = Data(None)
        assert DifferencingPipe.checkConditions(data) == False