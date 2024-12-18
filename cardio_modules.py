import pandas as pd
import numpy as np

class Outliers:
    def __init__(self,df,col_name):
        self.df = df #Define as attributes
        self.col_name = col_name
        self.iqr = None
        self.percentile_75 = None
        self.percentile_25 = None
    def percentiles(self):
        self.percentile_75 = np.percentile(self.df[self.col_name], 75)
        self.percentile_25 = np.percentile(self.df[self.col_name], 25)
        self.iqr = self.percentile_75 - self.percentile_25
        return self.iqr
    def outliers_min(self):
        if self.iqr is None:
            self.percentiles()
        return self.percentile_25 - 1.5*self.iqr
    def outliers_max(self):
        if self.iqr is None:
            self.percentile()
        return self.percentile_75 + 1.5*self.iqr

