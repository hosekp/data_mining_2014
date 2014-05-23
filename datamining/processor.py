'''
Created on 23. 5. 2014

@author: Ringael
'''
#import rdkit
#from rdkit.Chem.Fingerprints import FingerprintMol as Topological 
import rdkit.Chem as Chem
import rdkit.Chem.MACCSkeys as MACCS
import rdkit.Chem.AtomPairs.Pairs as AtomPairs
import rdkit.Chem.AtomPairs.Torsions as Torsions
import rdkit.Chem.AllChem as Morgan
import rdkit.DataStructs as DataStruct
import rdkit.SimDivFilters.rdSimDivPickers as DivPickers
from  sklearn.naive_bayes import MultinomialNB as Bayes
from sklearn import datasets
import json

def fingerPrints(arr,params):
    def topological(rdmol,params):
        return Chem.RDKFingerprint(rdmol)
    def maccs(rdmol,params):
        return MACCS.GenMACCSKeys(rdmol)
    def atompairs(rdmol,params):
        return AtomPairs.GetAtomPairFingerprintAsIntVect(rdmol)
    def torsions(rdmol,params):
        return Torsions.GetTopologicalTorsionFingerprintAsIntVect(rdmol)
    def morgan(rdmol,params):
        return Morgan.GetMorganFingerprint(rdmol,params["radius"],useFeatures=True)
    methods={"topological":topological,"maccs":maccs,"atompairs":atompairs,"torsions":torsions,"morgan":morgan}
    
    try:
        for mol in arr:
            mol.fingerprint=methods[params["fingerprint"]](mol.RDMol,params)
    except KeyError:
        print("Selected fingerprint not found")
    return arr

def DiversePicker(arr,params):
    def dist(i,j,arr=arr):
        return 1-DataStruct.DiceSimilarity(arr[i].fingerprint, arr[j].fingerprint)
    picker=DivPickers.MaxMinPicker()
    picked=picker.LazyPick(dist,len(arr),params["size"])
    return [arr[x] for x in picked]

def naiveBayes(arr,params):
    bayes=Bayes()
    activities=[elem.activity for elem in arr]
    fingerprints=[elem.fingerprint for elem in arr]
    #fingerprints=[[10,20,30] for elem in arr]
    print("X="+str(len(fingerprints))+" Y="+str(len(activities)))
    fit=bayes.fit(fingerprints,activities)
    predict=fit.predict(fingerprints)
    miss=0
    right=0
    for i in range(len(predict)):
        if predict[i]==activities[i]:
            right+=1
        else:
            miss+=1
    print("Right: "+str(right)+" Miss: "+str(miss))
        
    #predic.fit(X, y, class_prior)
    
        

        
        
    