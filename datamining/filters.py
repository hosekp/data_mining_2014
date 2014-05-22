'''
Created on 21. 5. 2014

@author: Ringael
'''
import math

def filterByActivity(arr):
    retarr=[]
    discard=[0,0,0,0,0,0,0,0]
    mols={}
    for line in arr:
        if not line[u'bioactivity_type'] in [u'IC50']:
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
        if value > 10:
            discard[4]+=1
            continue
        #mol=Molecule()

        line.id=line[u'parent_cmpd_chemblid']
        #mol.id=line[u'ingredient_cmpd_chemblid']
        if(line.id in mols):
            discard[5]+=1
            continue
        else:
            mols[line.id]=True           
        line.pIC=-math.log(value)
        retarr.append(line)
        discard[6]+=1
    return retarr
def getPossibles(arr,key):
    retarr=[]
    for line in arr:
        if not line[key] in retarr:
            retarr.append(line[key]);
    return retarr
