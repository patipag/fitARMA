# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:15:24 2018

@author: PPAGACZ
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:01:27 2018

@author: PPAGACZ
"""

import pytest
from ACF_PACFFilter import *
from unittest import TestCase
import pandas as pd

class Test_ACF_PACFFilter(TestCase):

    def test_get_item_org_diff_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD, DIFF)
        actual = ACF_PACFFilter.getItems(data)
        assert expected == actual

    def test_get_item_org_diff(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        expected = (ORGINAL, DIFF)
        actual = ACF_PACFFilter.getItems(data)
        assert expected == actual
    
    def test_get_item_org_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD)
        actual = ACF_PACFFilter.getItems(data)
        assert expected == actual
        
    def test_get_item_org(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        expected = (ORGINAL)
        actual = ACF_PACFFilter.getItems(data)
        assert expected == actual
        
    def test_get_title(self):
        title = "tytul"
        expected = ACF_MADE+title+DOT
        assert ACF_PACFFilter.get_title(title) == expected
        
    def test_get_title_without_dot(self):
        title = "tytul"
        expected = ACF_MADE+title
        assert ACF_PACFFilter.get_title(title) != expected
        
    def test_get_info(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = ts.head(n=30).to_string()
        assert ACF_PACFFilter.get_info(ts) == expected
        
    def test_get_info_short(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = ts.head(n=10).to_string()
        assert ACF_PACFFilter.get_info(ts) != expected
        
    def test_get_acf(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = acf(ts, nlags=20)
        actual = ACF_PACFFilter.get_acf(ts)
        assert (expected == actual).all()
        
    def test_get_acf_other_lags(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = acf(ts, nlags=10)
        actual = ACF_PACFFilter.get_acf(ts)
        assert expected != actual
        
    def test_get_pacf(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pacf(ts, nlags=20, method='ols')
        actual = ACF_PACFFilter.get_pacf(ts)
        assert (expected == actual).all()
        
    def test_get_pacf_other_lags(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        ts = series[columns[1]]
        expected = pacf(ts, nlags=10, method='ols')
        actual = ACF_PACFFilter.get_pacf(ts)
        assert expected != actual
        

