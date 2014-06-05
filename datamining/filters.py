'''
Created on 21. 5. 2014

@author: Ringael
'''
import math,utils
from molecule import Molecule
import rdkit.DataStructs as DataStruct

def filterByActivity(arr,params):
    retarr=[]
    discard=[0,0,0,0,0,0,0,0]
    mols={}
    for line in arr:
        #print(line)
        if not line[u'bioactivity_type'] == u'IC50':
            discard[0]+=1
            continue
        if line[u"target_confidence"]<7:
            discard[1]+=1
            continue
        if line[u"units"]!=u"nM":
            discard[2]+=1
            continue
        value=0.0
        try:
            value=float(line[u"value"])
        except ValueError:
            discard[3]+=1
            continue
        if value > 1000:
            discard[4]+=1
            continue
        mol=Molecule(name=line[u'parent_cmpd_chemblid'])

        #mol.id=line[u'ingredient_cmpd_chemblid']
        if(mol.name in mols):
            discard[5]+=1
            continue
        else:
            mols[mol.name]=True           
        mol.pIC=-math.log(value)
        retarr.append(mol)
        discard[6]+=1
    print(discard)
    return retarr
def createMolecules(arr,params):
    retarr=[]
    for elem in arr:
        mol=Molecule()
        mol.RDMol=elem["RDMol"]
        retarr.append(mol)
    return retarr
def filterKeys(arr,params):
    retarr=[]
    for elem in arr:
        nelem=Molecule(ID=elem["id"],name=elem["name"])
        for key in params:
            nelem[key]=elem[key]
        retarr.append(nelem)
    return retarr
            
def checkPoint(arr,params):
    retarr=[]
    for elem in arr:
        valid=True
        for key in params:
            try:
                elem[key]
            except KeyError:
                valid=False
        if valid:
            retarr.append(elem)
        else:
            print("CheckPoint: vyrazeno "+elem.name)
    return retarr

def DiceFilter(arr,sample,params):
    treshold=utils.implicit(params,"limit",0.5)
    def dist(i,j,tres=treshold):
        return (1-DataStruct.DiceSimilarity(i.fingerprint, j.fingerprint)) < tres
    ret=[]
    ret2=[]
    proc=utils.Procents(len(arr))
    for elem in arr:
        valid=False
        for sam in sample:
            if(dist(elem,sam)):
                valid=True
                break
        if valid:
            ret.append(elem)
        else:
            ret2.append(elem)
        proc.next()
    return ret,ret2
            
        