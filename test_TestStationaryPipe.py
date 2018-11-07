# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:59:47 2018

@author: PPAGACZ
"""

import pytest
from TestStationaryPipe import *
from unittest import TestCase

class Test_TestStationaryPipe(TestCase):

    def test_data_orignial_exist(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        assert TestStationaryPipe.checkConditions(data) == True

    def test_data_orignial_not_exist(self):
        data = Data(None)
        assert TestStationaryPipe.checkConditions(data) == False