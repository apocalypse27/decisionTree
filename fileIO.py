# -*- coding: utf-8 -*-
import pandas as pd;
class fileIO:
    
    def __init__(self,filePath):
        try:
            self.masterCopy=pd.read_csv(filePath);
            self.uniqueValDictionary={};
            numColumns=self.masterCopy.shape[1];
            self.allFeatures=list(self.masterCopy.columns[:numColumns]);
            self.targetFeature=self.allFeatures[numColumns-1];
        
            for feature in self.allFeatures:
                listTobeAdded=list(self.masterCopy[feature].unique());
                self.uniqueValDictionary.update({feature:listTobeAdded});
        except:
            print("CSV file not available at the location",filePath);
                
        