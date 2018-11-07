# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 19:34:49 2018

@author: PPAGACZ
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
from packets import *


class WaldDecompositionFilter(IFilter):
   
    def process(self):
        ts = self.data.orginal
        rcParams['figure.figsize'] = 15, 6
        ts_log = WaldDecompositionFilter.ts_log(ts)
        decomposition = WaldDecompositionFilter.decomposition(ts_log)
    
        trend = WaldDecompositionFilter.trend(decomposition)
        seasonal = WaldDecompositionFilter.seasonal(decomposition)
        residual = WaldDecompositionFilter.residual(decomposition)
        
        self.plot.plotDecomposition(ts_log, trend, seasonal, residual)
        self.tekst.setText(DECO_MADE)
        ts_log_decompose = residual
        ts_log_decompose.dropna(inplace=True)
        self.info.setText(WaldDecompositionFilter.getText(ts_log_decompose))
        WaldDecompositionFilter.setWaldDecomposition(self.data, ts_log_decompose)

    def ts_log(ts):
        return np.log(ts)
        
    def decomposition(ts_log):
        return seasonal_decompose(ts_log)
    
    def trend(decomposition):
        return decomposition.trend
    
    def seasonal(decomposition):
        return decomposition.seasonal
    
    def residual(decomposition):
        return decomposition.resid
        
    def getText(ts_log_decompose):
        return "Data after Wald decomposition\nMonth      #Passengers\n"+ts_log_decompose.head(n=30).to_string()
        
    def setWaldDecomposition(data, ts_log_decompose):
        data.waldDecomposition = ts_log_decompose