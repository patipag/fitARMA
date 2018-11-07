# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:07:38 2018

@author: PPAGACZ
"""
from statsmodels.tsa.stattools import acf, pacf
import matplotlib.pylab as plt
import numpy as np
from packets import *


class ACF_PACFFilter(IFilter):
   
    def process(self):
        ACF_PACFFilter.getData(self)
        
    def compute(self, ts, title):
        lag_acf = ACF_PACFFilter.get_acf(ts)
        lag_pacf = ACF_PACFFilter.get_pacf(ts)
    
        self.plot.plotACF(lag_acf, lag_pacf, ts)
        self.tekst.setText(ACF_PACFFilter.get_title(title))
        self.info.setText(ACF_PACFFilter.get_info(ts))
        # self.plot.plotData(lag_acf)

    def getData(self):
        items = ACF_PACFFilter.getItems(self.data)
        item, okPressed = QInputDialog.getItem(self, "Choose data to test","Data:", items, 0, False)
        if okPressed and item:
            if item == ORGINAL:
                ACF_PACFFilter.compute(self,self.data.orginal, "orginal data")
            elif item == WALD:
                ACF_PACFFilter.compute(self,self.data.waldDecomposition, "data after Wald decomposition")
            else:
                ACF_PACFFilter.compute(self,self.data.differencing, "differenced data")
            
    def getItems(data):
        if( data.orginal is not None and data.differencing is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD, DIFF)
        elif( data.orginal is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD)
        elif( data.orginal is not None and data.differencing is not None):
            return (ORGINAL, DIFF)
        else:
            return (ORGINAL)
            
    def get_acf(ts):
        return acf(ts, nlags=20)
        
    def get_pacf(ts):
        return pacf(ts, nlags=20, method='ols')
        
    def get_title(title):
        return ACF_MADE+title+DOT
     
    def get_info(ts):
        return ts.head(n=30).to_string()