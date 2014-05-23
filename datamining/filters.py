'''
Created on 21. 5. 2014

@author: Ringael
'''
import math
from molecule import Molecule

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
        mol=Molecule(line[u'parent_cmpd_chemblid'])

        #mol.id=line[u'ingredient_cmpd_chemblid']
        if(mol.id in mols):
            discard[5]+=1
            continue
        else:
            mols[mol.id]=True           
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
        nelem=Molecule(elem["id"])
        for key in params:
            nelem[key]=elem[key]
        retarr.append(nelem)
    return retarr
            
def getPossibles(arr,key):
    retarr=[]
    for line in arr:
        if not line[key] in retarr:
            retarr.append(line[key]);
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
            print("CheckPoint: vyrazeno "+elem.id)
    return retarr
