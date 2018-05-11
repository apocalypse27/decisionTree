# -*- coding: utf-8 -*-
from fileIO import *
import numpy as np

INFOGAIN_HEURISTIC=0;
IMPURITY_HEURISTIC=1;

def chooseBestAttribute(dataframe,fileObj,attributes,classifierType):
        if(classifierType==INFOGAIN_HEURISTIC):
            return(runInfoGainClassifier(dataframe,attributes,fileObj));
        else:
            return(runImpurityVarianceClassifier(dataframe,attributes,fileObj));
            
            
def runInfoGainClassifier(dataframe,attributes,fileObj):
        maxInfoGain=0;
        classifyingFeature=""
        entropy=findEntropy(dataframe,fileObj);        
        for feature in attributes[:-1]:
            featureInfoGain=entropy-calcInfoGain(dataframe,feature,fileObj);
            if(featureInfoGain>=maxInfoGain):
                maxInfoGain=featureInfoGain;
                classifyingFeature=feature;
        return(classifyingFeature);
        
        
        
def calcInfoGain(df,feature,fileObj):
        classificationCounts={};
        totalGain=0;
        totalExamples=df.shape[0];
        for featureValue in fileObj.uniqueValDictionary[feature]:
            dfSubset=df.loc[df[feature]==featureValue];
            
            if((dfSubset.shape[0]==0) or (dfSubset.shape[0]==totalExamples)):
                entropy=0;
            else:
                entropy=findEntropy(dfSubset,fileObj);
            partialGain=(dfSubset.shape[0]*entropy)/totalExamples;
            totalGain+=partialGain;
        return totalGain;


       
def findEntropy(df,fileObj):
        positiveNegativeCounts={};
        total=df.shape[0];
        entropy=0;
        
        for uniqueValue in fileObj.uniqueValDictionary[fileObj.targetFeature]:
            dfSubset=df.loc[df[fileObj.targetFeature]==uniqueValue];
            positiveNegativeCounts.update({uniqueValue:dfSubset.shape[0]});
            
        for key,value in positiveNegativeCounts.items():
            if(value==0 or value==total):
                entropy=0;
            else:
                logValue=np.log2(value/total);
                multipliedValue=(-1)*logValue*(value/total);
                entropy+=multipliedValue;
        return(entropy);

def runImpurityVarianceClassifier(dataframe,attributes,fileObj):
    maxVarImpurityGain=0;
    classifyingFeature=""
    entropy=findVarImpurity(dataframe,fileObj);
    for feature in attributes[:-1]:
        featureVarImpurityGain=entropy-calcVarImpurityGain(dataframe,feature,fileObj);
        if(featureVarImpurityGain>maxVarImpurityGain):
            maxVarImpurityGain=featureVarImpurityGain;
            classifyingFeature=feature;
    return(classifyingFeature);

def calcVarImpurityGain(df,feature,fileObj):
    totalGain=0;
    totalExamples=df.shape[0];
    for featureValue in fileObj.uniqueValDictionary[feature]:
        dfSubset=df.loc[df[feature]==featureValue];            
        if((dfSubset.shape[0]==0) or (dfSubset.shape[0]==totalExamples)):
            entropy=0;
        else:
            entropy=findVarImpurity(dfSubset,fileObj);
        partialGain=(dfSubset.shape[0]*entropy)/totalExamples;
        totalGain+=partialGain;
    return totalGain;
    

def findVarImpurity(df,fileObj):
    numerator=1;
    total=df.shape[0];
    for uniqueValue in fileObj.uniqueValDictionary[fileObj.targetFeature]:
        dfSubset=df.loc[df[fileObj.targetFeature]==uniqueValue];
        numerator*=(dfSubset.shape[0]/total);
    return(numerator);
        
        
    
    
    
