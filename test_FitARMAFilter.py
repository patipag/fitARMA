# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:36:00 2018

@author: PPAGACZ
"""

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
from FitARMAFilter import *
from unittest import TestCase
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

class Test_FitARMAFilter(TestCase):

    def test_get_item_org_diff_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD, DIFF)
        actual = FitARMAFilter.getItems(data)
        assert expected == actual

    def test_get_item_org_diff(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.differencing = series[columns[1]]
        expected = (ORGINAL, DIFF)
        actual = FitARMAFilter.getItems(data)
        assert expected == actual
    
    def test_get_item_org_wald(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        data.waldDecomposition = series[columns[1]]
        expected = (ORGINAL, WALD)
        actual = FitARMAFilter.getItems(data)
        assert expected == actual
        
    def test_get_item_org(self):
        series = pd.read_csv('AirPassengers.csv')
        columns = list(series.columns.values)
        data = Data(series[columns[1]])
        expected = (ORGINAL)
        actual = FitARMAFilter.getItems(data)
        assert expected == actual
        
    def test_get_title(self):
        expected = ARMA_FITTED
        actual = FitARMAFilter.get_title()
        assert expected == actual
        
    def test_calculate_arma_p_q(self):
        series = pd.read_csv('AirPassengers.csv')
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        data = series[columns[1]]
        model_expected = ARIMA(data, order=(4,0,4))
        model_actual = FitARMAFilter.calculate_arma_p_q(data, 4,4)
        expected = model_expected.fit(disp=0).bic
        actual = model_actual.fit(disp=0).bic
        assert expected == actual
    
    def test_calculate_arma_p_q_wrong(self):
        series = pd.read_csv('AirPassengers.csv')
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        data = series[columns[1]]
        expected = ARIMA(data, order=(3,0,3))
        actual = FitARMAFilter.calculate_arma_p_q(data, 4,4)
        assert expected != actual
        
    def test_calculate_arma_fit(model):
        series = pd.read_csv('AirPassengers.csv')
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        data = series[columns[1]]
        model = ARIMA(data, order=(3,0,3))
        expected = model.fit(disp=0)
        actual = FitARMAFilter.calculate_arma_fit(model)
        assert expected.bic == actual.bic
    
    
    def test_calculate_arma_fit_wrong(model):
        series = pd.read_csv('AirPassengers.csv')
        series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
        columns = list(series.columns.values)
        data = series[columns[1]]
        model = ARIMA(data, order=(3,0,3))
        expected = model.fit(disp=-1)
        actual = FitARMAFilter.calculate_arma_fit(model)
        assert expected != actual   
        
        
        
        
        
        
        
        
        