# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:38:19 2018

@author: PPAGACZ
"""

from DifferencingFilter import *
import unittest.mock 
import pytest
from pytest_mock import mocker 
import numpy as np
import pandas as pd 

from unittest import TestCase

class Test_DifferencingFilter(TestCase):

    def test_log_ts(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = np.log(ts)
        actual = DifferencingFilter.ts_log(ts)
        assert  ((expected == actual).all())
    
    def test_log_shifted(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        expected = ts_log - ts_log.shift()
        actual = DifferencingFilter.ts_log_diff(ts_log)
        assert  ((expected == actual).any())
    
    def test_extract_NAN(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        ts_log_diff = ts_log - ts_log.shift()
        actual = DifferencingFilter.extractNan(ts_log_diff)
        assert  actual != 'NaN'
    
    def test_setDifferencedData(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        DifferencingFilter.setDifferencedData(data, series[columns[1]])
        assert  data.differencing.all() != None

    def test_getText(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        ts_log_diff = ts_log - ts_log.shift()
        ts_log_diff.dropna(inplace=True)
        expected = "Data after differencing\nMonth      #Passengers\n"+ts_log_diff.head(n=30).to_string()
        actual = DifferencingFilter.getText(ts_log_diff)
        assert expected == actual

