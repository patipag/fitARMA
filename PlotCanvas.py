# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:30:26 2018

@author: PPAGACZ
"""
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets

from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import seaborn as sns

from statsmodels.tsa.stattools import adfuller


from dictionary import *

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
    def plotData(self,y):
        self.clear()
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.plot(y, 'r-')
        ax.set_title(DATA_FROM_THE_FILE)
        self.draw()
    
    def plotDataDiff(self,y):
        self.clear()
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.plot(y, 'r-')
        ax.set_title(DATA_DIFF)
        self.draw()
        
    def plotForecast(self,y):
        print("rysuje nowe dane")
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.plot(y, 'r-')
        ax.set_title(FORECAST)
        self.draw()
        
    def plotDataDetrended(self,y, y_detrended):
        print("rysuje nowe dane")
        ax = self.figure.add_subplot(111)
        ax.cla()
        #ax.plot(y, label="x")
        ax.plot(y_detrended, 'r-', label="x_detrended")
        ax.plot(y, 'b-', label="x")
        ax.legend(loc='best')
        #ax.scatter(y)
        ax.set_title('Dane po odfiltrowaniu trendu')
        self.draw()
        
    def plotDataWithTrend(self,trendSin, y_detrended):
        print("rysuje nowe dane")
        ax = self.figure.add_subplot(111)
        ax.cla()
        #ax.plot(y, label="x")
        ax.plot(trendSin, 'r-', label="trend okresowy")
        ax.plot(y_detrended, 'b-', label="y")
        ax.legend(loc='best')
        #ax.scatter(y)
        ax.set_title('Dane z trendem okresowym')
        self.draw()
        
    def plotStem(self, h,G):
        print("Autokowariancja")
        ax = self.figure.add_subplot(111)
        ax.cla()
        #ax.plot(y, label="x")
        ax.stem(h,G)
        #ax.scatter(y)
        ax.set_title('Autocovariation function for data')
        self.draw()
        
    def plotAutoCov(self, series):
        print("Autokowariancja rysowanie")
        print(series)
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.set_title('Autocovariation function for data')
        Z = autocorrelation_plot(series)
        ax.plot(Z)
        self.draw()
        
    def plotARMA(self, series, model_fit):
        self.clear()
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.plot(series, label = 'Data')
        ax.plot(model_fit.fittedvalues, color='red', label="Fitted ARMA Model")
        ax.legend(loc='best')
        ax.set_title('Fitted model ARMA')
        self.draw()
        
    def plotResiduals(self, residuals, bin_centers, pdf):
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.hist(residuals.values, bins=10, normed=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none', label = "Histogram of residuals")
        ax.set_title(HISTO)
        #ax.plot(bin_centers, pdf, label="Desity of standard normal distribution")
        ax.legend(loc='best')
        self.draw()
        
    def plotStationary(self, timeseries, rolmean, rolstd):
        self.clear()
        ax = self.figure.add_subplot(111)
        ax.cla()
        #Plot rolling statistics:
        ax.set_title(TEST_STATIONARY)
        ax.plot(timeseries, color='blue',label='Original')
        ax.plot(rolmean, color='red', label='Rolling Mean')
        ax.plot(rolstd, color='black', label = 'Rolling Std')
        ax.legend(loc='best')
        self.draw()
        
    def plotDecomposition(self,orginal, trend, seasonal, residual):
        print("rysuje decomposition")
        self.clear()
        a1 = self.figure.add_subplot(411)
        a2 = self.figure.add_subplot(412)
        a3 = self.figure.add_subplot(413)
        a4 = self.figure.add_subplot(414)
        a1.plot(orginal, color='blue', label='Original')
        a1.legend(loc='best')
        a2.plot(trend, color='red', label='Trend')
        a2.legend(loc='best')
        a3.plot(seasonal,color='black',label='Seasonality')
        a3.legend(loc='best')
        a4.plot(residual, color='blue', label='Residuals')
        a4.legend(loc='best')
        self.draw()
        
    def plotACF(self, acf, pacf, ts):
        print("rysuje acf")
        self.clear()
         #Plot ACF: 
        a1 = self.figure.add_subplot(121)
        a1.cla()
        a1.plot(acf, 'r-')
        a1.axhline(y=0,linestyle='--',color='gray')
        a1.axhline(y=-1.96/np.sqrt(len(ts)),linestyle='--',color='gray')
        a1.axhline(y=1.96/np.sqrt(len(ts)),linestyle='--',color='gray')
        a1.set_title('Autocorrelation Function')

        #Plot PACF:
        a2 = self.figure.add_subplot(122)
        a2.plot(pacf)
        a2.axhline(y=0,linestyle='--',color='gray')
        a2.axhline(y=-1.96/np.sqrt(len(ts)),linestyle='--',color='gray')
        a2.axhline(y=1.96/np.sqrt(len(ts)),linestyle='--',color='gray')
        a2.set_title('Partial Autocorrelation Function')
        self.draw()
  
        
    def clear(self):
        self.figure.clf()
        
     