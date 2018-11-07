# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:44:30 2018

@author: PPAGACZ
"""

from PyQt5.QtWidgets import  QFileDialog,QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import datetime
import pandas as pd 
from packets import *



class TestStationaryFilter(IFilter):
   
    def process(self):
        TestStationaryFilter.getData(self)
        
    def compute(self, timeseries, title):
        #Determing rolling statistics
        rolmean = TestStationaryFilter.compute_rolmean(timeseries)
        rolstd = TestStationaryFilter.compute_rolstd(timeseries)
        
        self.plot.plotStationary(timeseries, rolmean, rolstd)

        #Perform Dickey-Fuller test:
        print("Here1")
        dftest = TestStationaryFilter.perform_DickerFullerTest(timeseries)
        print("Here2")
        dfoutput = TestStationaryFilter.get_results_DickerFullerTest(dftest)
        print("Here")
    
        self.tekst.setText(TestStationaryFilter.getMessage(title))
        self.info.setText(TestStationaryFilter.getInfo(title, dfoutput))
        
        
    def compute_rolmean(ts):
        return pd.rolling_mean(ts, window=12)
        
    def compute_rolstd(ts):
        return pd.rolling_std(ts, window=12)
        
    def perform_DickerFullerTest(ts):
        return adfuller(ts, autolag='AIC')
        
    def get_results_DickerFullerTest(dftest):
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value    
        return dfoutput
        
    def getInfo(title, dfoutput):
        return DICKER_TEST + title+'\n'+str(dfoutput)
        
    def getMessage(title):
        return TEST_MADE + title + DOT
    
    def getData(self):
        items = TestStationaryFilter.getItems(self.data)
        #items = (ORGINAL, WALD, DIFF)
        item, okPressed = QInputDialog.getItem(self, "Choose data to test","Data:", items, 0, False)
        if okPressed and item:
            if item == ORGINAL:
                TestStationaryFilter.compute(self,self.data.orginal, "orginal data")
            elif item == WALD:
                TestStationaryFilter.compute(self,self.data.waldDecomposition, "data after Wald decomposition")
            else:
                TestStationaryFilter.compute(self,self.data.differencing, "differenced data")
    
    def getItems(data):
        if( data.orginal is not None and data.differencing is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD, DIFF)
        elif( data.orginal is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD)
        elif( data.orginal is not None and data.differencing is not None):
            return (ORGINAL, DIFF)
        else:
            return (ORGINAL)