'''
Created on 23. 5. 2014

@author: Ringael
'''
#import rdkit
#from rdkit.Chem.Fingerprints import FingerprintMol as Topological 
import rdkit.Chem.Fingerprints.FingerprintMols as Topological
import rdkit.Chem.MACCSkeys as MACCS
import rdkit.Chem.AtomPairs.Pairs as AtomPairs
import rdkit.Chem.AtomPairs.Torsions as Torsions
import rdkit.Chem.AllChem as Morgan
import rdkit.DataStructs as DataStruct
import rdkit.SimDivFilters.rdSimDivPickers as DivPickers

def fingerPrints(arr,params):
    def topological(rdmol,params):
        return Topological.FingerprintMol(rdmol)
    def maccs(rdmol,params):
        return MACCS.GenMACCSKeys(rdmol)
    def atompairs(rdmol,params):
        return AtomPairs.GetAtomPairFingerprint(rdmol)
    def torsions(rdmol,params):
        return Torsions.GetTopologicalTorsionFingerprintAsIntVect(rdmol)
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
    return [arr[x] for x in picked]
        

        
        
    