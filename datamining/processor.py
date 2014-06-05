'''
Created on 23. 5. 2014

@author: Ringael
'''
#import rdkit
#from rdkit.Chem.Fingerprints import FingerprintMol as Topological 
import rdkit.Chem as Chem
import rdkit.Chem.AtomPairs.Pairs as AtomPairs
import rdkit.Chem.AtomPairs.Torsions as Torsions
import rdkit.Chem.AllChem as Morgan
import rdkit.DataStructs as DataStruct
import rdkit.SimDivFilters.rdSimDivPickers as DivPickers
from  sklearn.naive_bayes import MultinomialNB as Bayes
from sklearn import svm,datasets
from utils import Procents,implicit
import json



def fingerPrints(arr,params):
    def topological(rdmol,params):
        return Chem.RDKFingerprint(rdmol)
    def maccs(rdmol,params):
        return Chem.rdMolDescriptors.GetMACCSKeysFingerprint(rdmol)
    def atompairs(rdmol,params):
        sparse = Chem.rdMolDescriptors.GetAtomPairFingerprint(rdmol)
        return DataStruct.ConvertToExplicit(sparse)
    def torsions(rdmol,params):
        sparse = Chem.rdMolDescriptors.GetTopologicalTorsionFingerprint(rdmol)
        return DataStruct.ConvertToExplicit(sparse)
    def morgan(rdmol,params):
        return Morgan.GetMorganFingerprintAsBitVect(rdmol,params["radius"],useFeatures=True)
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
    ret=[]
    ret2=[]
    for x in range(len(arr)):
        if x in picked:
            ret.append(arr[x])
        else:
            ret2.append(arr[x])

    return ret,ret2

def SupVecMach(arr,params):
        activities=[elem.pIC for elem in arr]
        fingerprints=[elem.fingerprint for elem in arr]
        kernel=implicit(params,"kernel","linear")
        Cpar=implicit(params,"C",1.0)
        degree=implicit(params,"degree",2)
        gamma=implicit(params,"gamma",0.1)
        svr=svm.SVR(kernel=kernel,C=Cpar,degree=degree,gamma=gamma).fit(fingerprints,activities)
        #for elem in arr:
        #    elem.prediction=svc.predict(elem.fingerprint)
        return arr,svr
def SVMpredict(arrs,params):
    arr=arrs[1]
    svr=arrs[2]
    proc=Procents(len(arr))
    for elem in arr:
        elem.prediction=svr.predict(elem.fingerprint)
        proc.next()
    return arr







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
    
        

        
        
    