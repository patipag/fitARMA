# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:15:45 2018

@author: PPAGACZ
"""

import numpy
from packets import *


class ForecastFilter(IFilter):
   
    def process(self):
        ForecastFilter.getNumber(self)
        
    def prediction(modelARMA, startIndex, lastIndex, self, number):
        print(startIndex)
        print(lastIndex)
        print(modelARMA)
        forecast = modelARMA.predict(start = startIndex, end = lastIndex)
        self.info.setText("Forecast was made for " + str(number) + " next observations.\n" + str(forecast))
        self.plot.plotForecast(forecast)
        self.tekst.setText(FORE)

    def getNumber(self):
         text, okPressed = QInputDialog.getText(self, "Forecast","Number of observations", QLineEdit.Normal, "")
         if okPressed and text != '':
             ForecastFilter.prediction(self.data.modelARMA, self.data.orginal.shape[0]-10, self.data.orginal.shape[0]-10+int(float(text)), self, int(float(text)))