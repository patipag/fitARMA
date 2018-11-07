# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:47:42 2018

@author: PPAGACZ
"""

import sys
 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from packets import *


class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'appARMA'
        self.width = 1700
        self.height = 950
        
        self.initUI()
 
    def initUI(self):
     
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet(MAIN)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.logo = QLabel(self)
        pixmap = QPixmap('icon.png')
        self.logo.setPixmap(pixmap)
        self.logo.resize(300,100)
        self.logo.move(50,20)
    
        self.plot = PlotCanvas(self, width=8, height=8)
        self.plot.move(200,140)
        
        self.info = QtWidgets.QLabel(self)
        self.info.setObjectName("info")
        self.info.move(1050,140)
        self.info.resize(620,800)
        self.info.setText(INFO)
        self.info.setStyleSheet(INFO_CSS)
        
        self.data = []
        self.modelARMA = None
        
        self.tekst = QtWidgets.QLabel(self)
        self.tekst.setObjectName("tekst")
        self.tekst.move(425,40)
        self.tekst.resize(1200,50)
        self.tekst.setStyleSheet(TEKST_CSS)
        self.tekst.setText(START)
        
         
        # buttons
        loadData = QPushButton(LOAD_DATA, self)
        testStationary = QPushButton(TEST_STATIONARY, self)
        wald = QPushButton(DECO, self)
        differencing = QPushButton(DIFF, self)
        autocorr = QPushButton(ACV, self)
        arma = QPushButton(ARMA, self)
        residuals = QPushButton(RESIDUALS, self)
        forecast = QPushButton(FORECAST, self)
        
        #location
        loadData.move(15,140)
        testStationary.move(15,220)
        wald.move(15,300)
        differencing.move(15,380)
        autocorr.move(15,460)
        arma.move(15,540)
        residuals.move(15,620)
        forecast.move(15,700)
        
        #size
        loadData.resize(140,50)
        testStationary.resize(140,50)
        wald.resize(140,50)
        differencing.resize(140,50)
        autocorr.resize(140,50)
        arma.resize(140,50)
        residuals.resize(140,50)
        forecast.resize(140,50)
        
        #colors
        loadData.setStyleSheet(BUTTON)
        testStationary.setStyleSheet(BUTTON)
        wald.setStyleSheet(BUTTON)
        differencing.setStyleSheet(BUTTON)
        autocorr.setStyleSheet(BUTTON)
        arma.setStyleSheet(BUTTON)
        residuals.setStyleSheet(BUTTON)
        forecast.setStyleSheet(BUTTON)
        
        #functions
        loadData.clicked.connect(lambda:LoadDataPipe.runFilter(self))
        testStationary.clicked.connect(lambda:TestStationaryPipe.runFilter(self))
        wald.clicked.connect(lambda:WaldDecompositionPipe.runFilter(self))
        differencing.clicked.connect(lambda:DifferencingPipe.runFilter(self))
        autocorr.clicked.connect(lambda:ACF_PACFPipe.runFilter(self))
        arma.clicked.connect(lambda:FitARMAPipe.runFilter(self))
        residuals.clicked.connect(lambda:ResidualsPipe.runFilter(self))
        forecast.clicked.connect(lambda:ForecastPipe.runFilter(self))
        
        self.show()
        
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())