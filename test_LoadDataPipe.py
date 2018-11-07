# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:54:46 2018

@author: PPAGACZ
"""

import pytest
from LoadDataPipe import *
from unittest import TestCase

class Test_LoadDataPipe(TestCase):

    def test_checkCondition(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        assert LoadDataPipe.checkConditions(data) == True
