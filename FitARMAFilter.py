# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:24:37 2018

@author: PPAGACZ
"""
from PyQt5.QtWidgets import  QFileDialog,QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
from packets import *
from statsmodels.tsa.arima_model import ARIMA


class FitARMAFilter(IFilter):
   
    def process(self):
        FitARMAFilter.getData(self)
        
    def getParams(self, ts, title):
        text, okPressed = QInputDialog.getText(self, "ARMA Parameters","AR (p), MA(q):", QLineEdit.Normal, "")
        if okPressed and text != '':
            p,q=text.split(',')
            FitARMAFilter.fitARMAModelWithParams(self, ts, int(float(p)), int(float(q)), title)
        
    def getMethod(self, ts, title):
        items = FitARMAFilter.getMethodItems()
        item, okPressed = QInputDialog.getItem(self, "Choose method","Method:", items, 0, False)
        if okPressed and item:
            if item == OWN:
                FitARMAFilter.getParams(self, ts, title)
            elif item == ALL:
                FitARMAFilter.fitARMAModelAllCheck(self, ts, title)
            else:
                FitARMAFilter.fitARMAModelNMMethod(self, ts, title)
                
    def getData(self):
        items = FitARMAFilter.getItems(self.data)
        item, okPressed = QInputDialog.getItem(self, "Choose data to fit ARMA","Data:", items, 0, False)
        if okPressed and item:
            if item == ORGINAL:
                FitARMAFilter.getMethod(self,self.data.orginal, "orginal data")
            elif item == WALD:
                FitARMAFilter.getMethod(self,self.data.waldDecomposition, "data after Wald decomposition")
            else:
                FitARMAFilter.getMethod(self,self.data.differencing, "differenced data")
    
    def getItems(data):
        if( data.orginal is not None and data.differencing is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD, DIFF)
        elif( data.orginal is not None and data.waldDecomposition is not None):
            return (ORGINAL, WALD)
        elif( data.orginal is not None and data.differencing is not None):
            return (ORGINAL, DIFF)
        else:
            return (ORGINAL)
            
    def getMethodItems():
        return (OWN, ALL, NM)
            
    def fitARMAModelWithParams(self, series, p, q, title):
        model = FitARMAFilter.calculate_arma_p_q(series,p,q)
        modelARMA = FitARMAFilter.calculate_arma_fit(model)
        print(modelARMA.bic)

        self.plot.plotARMA(series, modelARMA)
        #print(modelARMA.summary().to_string
        self.info.move(1050,100)
        self.info.resize(850,900)
        self.info.setText(str(modelARMA.summary()))
        self.tekst.setText(ARMA_FITTED+title+DOT)
        self.data.modelARMA = modelARMA
        
    def fitARMAModelAllCheck(self, series):
        # fit model
        model = FitARMAFilter.calculate_arma_p_q(series,4,4)
        modelARMA = FitARMAFilter.calculate_arma_fit(model)
        print(modelARMA.bic)

        self.plot.plotARMA(series, modelARMA)
        #print(modelARMA.summary().to_string
        self.info.resize(820,800)
        self.info.setText(str(modelARMA.summary()))
        self.tekst.setText(ARMA_FITTED)
        self.data.modelARMA = modelARMA
        
    def fitARMAModelNMMethod(self, series):
        # fit model
        model = FitARMAFilter.calculate_arma_p_q(series,4,4)
        modelARMA = FitARMAFilter.calculate_arma_fit(model)

        self.plot.plotARMA(series, modelARMA)
        #print(modelARMA.summary().to_string
        self.info.resize(820,800)
        self.info.setText(str(modelARMA.summary()))
        self.tekst.setText(FitARMAFilter.get_title())
        self.data.modelARMA = modelARMA
        
    def get_title():
        return ARMA_FITTED
        
    def calculate_arma_p_q(series, p,q):
        return ARIMA(series, order=(p,0,q))
        
    def calculate_arma_fit(model):
        return model.fit(disp=0)
