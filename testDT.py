# -*- coding: utf-8 -*-
from ID3 import *
import sys

INFOGAIN_HEURISTIC=0;
IMPURITY_HEURISTIC=1;

print("Num of args",len(sys.argv));
#print(sys.argv[1]);

def main():     
    infoGainRun=ID3(sys.argv);
    print("INFO_GAIN TREE");
    infoGainRun.runID3(INFOGAIN_HEURISTIC);
    print("Accuracy over test data-original tree",infoGainRun.validateTestDataOrg());
    print("Accuracy over test data-pruned tree",infoGainRun.validateTestData());
    impurityVarRun=ID3(sys.argv);
    print("IMPURITY VARIANCE");
    impurityVarRun.runID3(IMPURITY_HEURISTIC);
    print("Accuracy over test data-original tree",impurityVarRun.validateTestDataOrg());
    print("Accuracy over test data-pruned tree",impurityVarRun.validateTestData());
    
    
main();