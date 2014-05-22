'''
Created on 21. 5. 2014

@author: Ringael
'''

import urllib2
import json
import rdkit.Chem as rd

if __name__ == '__main__':
    pass

def loadMoleculesFromChEMBL(accession):
    jsonn=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/targets/"+accession+"/bioactivities.json").read()
    return json.loads(jsonn)
def getStructureFromChEMBL(molec):
    string=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/compounds/"+molec.id+".json").read()
    #print string
    bigjson=json.loads(string)
    molec.json=bigjson["compound"]
    molec.smiles=str(molec.json["smiles"])
def readMoleculesFromMol2(arr,address):
    file1=open(address,"r")
    allstr=file1.read()
    i=0
    j=0
    while (i<len(allstr)):
        j=allstr.find("@<TRIPOS>MOLECULE",j+1)
        if (j==-1):
            j=len(allstr)
        arr.append({"RDMol":rd.MolFromMol2Block(allstr[i:j])})
        i=j
    return arr
def getRDMol(molec):
        try:
            molec.RDMol=rd.MolFromSmiles(molec.smiles)
        except:
            print(molec.id+" not converted")
        #return self.RDMol