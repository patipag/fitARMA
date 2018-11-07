# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:23:42 2018

@author: PPAGACZ
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pandas import datetime
import pandas as pd 
from packets import *


class LoadDataFilter(IFilter):
   
    def process(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Choose a file", "","CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)
   
        series = pd.read_csv(fileName)       
        if LoadDataFilter.checkCondition(series):
            self.tekst.setText(DATA_LOADED)
            self.info.setText(series.head(n=30).to_string())
            series.index = pd.DatetimeIndex(freq = 'M', start = 0, periods=series.shape[0])
            columns = list(series.columns.values)
            self.data = Data(series[columns[1]])
            self.plot.plotData(self.data.orginal)
        else:
            q = QMessageBox(QMessageBox.Warning, "Warning",  WRONG_DATA)
            q.setStandardButtons(QMessageBox.Ok);
            #i = QIcon()
            #i.addPixmap(QStyle.SP_MessageBoxWarning, QIcon.Disabled, QIcon.Off)
            q.setWindowIcon(self.style().standardIcon(getattr(QStyle,'SP_MessageBoxCritical')))
            q.exec_()

    def checkCondition(series):
        return series.shape[1] == 2
