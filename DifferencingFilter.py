# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 19:53:13 2018

@author: PPAGACZ
"""

import numpy as np
from packets import *
from pandas import datetime
import pandas as pd 


class DifferencingFilter(IFilter):
   
    def process(self):
        ts = self.data.orginal
        ts_log = DifferencingFilter.ts_log(ts)
        #plt.plot(ts_log)
        ts_log_diff = DifferencingFilter.ts_log_diff(ts_log)
        DifferencingFilter.extractNan(ts_log_diff)
        self.tekst.setText(DIFF_MADE)
        DifferencingFilter.setDifferencedData(self.data, ts_log_diff)
        self.plot.plotDataDiff(self.data.differencing)
        self.info.setText(DifferencingFilter.getText(ts_log_diff))
          
    def ts_log(ts):
        return np.log(ts)
        
    def ts_log_diff(ts_log):
        return ts_log - ts_log.shift()
        
    def extractNan(ts_log_diff):
        return ts_log_diff.dropna(inplace=True)
        
    def setDifferencedData(data, ts_log_diff):
        data.differencing = ts_log_diff
    
    def getText(ts_log_diff):
        return "Data after differencing\nMonth      #Passengers\n"+ts_log_diff.head(n=30).to_string()