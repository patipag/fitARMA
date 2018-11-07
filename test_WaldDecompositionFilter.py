# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:57:26 2018

@author: PPAGACZ
"""

from WaldDecompositionFilter import *
import unittest.mock 
import pytest
from pytest_mock import mocker 
import numpy as np
import pandas as pd 
from statsmodels.tsa.seasonal import seasonal_decompose

from unittest import TestCase

class Test_WaldDecompositionFilter(TestCase):

    def test_log_ts(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = np.log(ts)
        actual = WaldDecompositionFilter.ts_log(ts)
        assert  ((expected == actual).all())
    
    def test_decomposition(self):
        series = pd.read_csv("AirPassengers.csv")
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        expected = seasonal_decompose(ts_log)
        actual = WaldDecompositionFilter.decomposition(ts_log)
        assert actual is not None
    
    def test_trend(self):
        series = pd.read_csv("AirPassengers.csv")
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        decomposition = seasonal_decompose(ts_log)
        expected = decomposition.trend
        actual = WaldDecompositionFilter.trend(decomposition)
        assert  ((expected == actual).any())
        
    def test_seasonal(self):
        series = pd.read_csv("AirPassengers.csv")
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        decomposition = seasonal_decompose(ts_log)
        expected = decomposition.seasonal
        actual = WaldDecompositionFilter.seasonal(decomposition)
        assert  ((expected == actual).all())
    
    def test_residuals(self):
        series = pd.read_csv("AirPassengers.csv")
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        decomposition = seasonal_decompose(ts_log)
        expected = decomposition.resid
        actual = WaldDecompositionFilter.residual(decomposition)
        assert  ((expected == actual).any())
    

    def test_getText(self):
        series = pd.read_csv("AirPassengers.csv")
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        ts = series[columns[1]]
        ts_log = np.log(ts)
        decomposition = seasonal_decompose(ts_log)
        ts_log_decompose = decomposition.resid
        ts_log_decompose.dropna(inplace=True)
        expected = "Data after Wald decomposition\nMonth      #Passengers\n"+ts_log_decompose.head(n=30).to_string()
        actual =  WaldDecompositionFilter.getText(ts_log_decompose)
        assert expected == actual
        
    def test_setDecomposedData(self):
        series = pd.read_csv("AirPassengers.csv")
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        WaldDecompositionFilter.setWaldDecomposition(data, series[columns[1]])
        assert  data.waldDecomposition.all() != None
