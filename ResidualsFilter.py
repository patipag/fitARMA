# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:54:55 2018

@author: PPAGACZ
"""

from pandas import DataFrame
from packets import *
import numpy as np
from scipy import stats


class ResidualsFilter(IFilter):
   
    def process(self):
        residuals = DataFrame({"Residuals":self.data.modelARMA.resid})
        test = self.data.modelARMA.resid
        print(type(test))
        #print(self.data.modelARMA.resid)
        #print(residuals)
        self.info.resize(620,800)
        self.info.setText(str(residuals.describe()))
        print(residuals.describe())
        
        #Compute pdf of normal distribution
        samples = np.random.normal(size=10000)
        bins = np.linspace(-5, 5, 30)
        histogram, bins = np.histogram(samples, bins=bins, normed=True)
        bin_centers = 0.5*(bins[1:] + bins[:-1])
        pdf = stats.norm.pdf(bin_centers)
        
        self.plot.plotResiduals(residuals, bin_centers, pdf)
        self.tekst.setText(HIST)