# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:01:27 2018

@author: PPAGACZ
"""

import pytest
from TestStationaryFilter import *
from unittest import TestCase
import pandas as pd

class Test_TestStationaryFilter(TestCase):

    def test_get_item_org_diff_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD, DIFF)
        actual = TestStationaryFilter.getItems(data)
        assert expected == actual

    def test_get_item_org_diff(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        expected = (ORGINAL, DIFF)
        actual = TestStationaryFilter.getItems(data)
        assert expected == actual
    
    def test_get_item_org_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD)
        actual = TestStationaryFilter.getItems(data)
        assert expected == actual
        
    def test_get_item_org(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        expected = (ORGINAL)
        actual = TestStationaryFilter.getItems(data)
        assert expected == actual
        
    def test_getInfo(self):
        title = "tytul"
        expected = TEST_MADE + title + DOT
        assert TestStationaryFilter.getMessage(title) == expected
        
    def test_getMessage(self):
        title = "tytul"
        dfoutput = "dfoutput"
        expected = DICKER_TEST + title+'\n'+str(dfoutput)
        assert TestStationaryFilter.getInfo(title, dfoutput) == expected
        
    def test_compute_rolmean(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pd.rolling_mean(ts, window=12)
        actual = TestStationaryFilter.compute_rolmean(ts)
        return expected == actual
        
    def test_compute_rolmean_other_window(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pd.rolling_mean(ts, window=7)
        actual = TestStationaryFilter.compute_rolmean(ts)
        return expected != actual
        
    def test_compute_rolstd(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pd.rolling_std(ts, window=12)
        actual = TestStationaryFilter.compute_rolstd(ts)
        return expected == actual
        
    def test_compute_rolstd_other_window(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pd.rolling_std(ts, window=7)
        actual = TestStationaryFilter.compute_rolstd(ts)
        return expected != actual

    def test_perform_DickerFullerTest(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = adfuller(ts, autolag='AIC')
        actual = TestStationaryFilter.perform_DickerFullerTest(ts)
        return expected == actual
        
    def test_perform_DickerFullerTest_Other_Autolag(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = adfuller(ts, autolag='BIC')
        actual = TestStationaryFilter.perform_DickerFullerTest(ts)
        return expected != actual
        
    def test_get_results_DickerFullerTest(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        dftest = adfuller(ts, autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value    
        expected = dfoutput
        actual = TestStationaryFilter.get_results_DickerFullerTest(dftest)
        assert (actual == expected).all()
