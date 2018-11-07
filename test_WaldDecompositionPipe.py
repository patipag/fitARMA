# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:53:50 2018

@author: PPAGACZ
"""

import pytest
from WaldDecompositionPipe import *
from unittest import TestCase

class Test_WaldDecompositionPipe(TestCase):

    def test_data_orignial_exist(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        assert WaldDecompositionPipe.checkConditions(data) == True

    def test_data_orignial_not_exist(self):
        data = Data(None)
        assert WaldDecompositionPipe.checkConditions(data) == False