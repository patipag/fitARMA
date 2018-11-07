# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:11:05 2018

@author: PPAGACZ
"""

import pytest
from ACF_PACFPipe import *
from unittest import TestCase

class Test_ACF_PACFPipe(TestCase):

    def test_data_orignial_exist(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        assert ACF_PACFPipe.checkConditions(data) == True

    def test_data_orignial_not_exist(self):
        data = Data(None)
        assert ACF_PACFPipe.checkConditions(data) == False