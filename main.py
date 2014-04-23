import rdkit.Chem as rd
import numpy,scipy,math
import sklearn as scikit
import json
import urllib2

decoy=[]
active=[]
def readMolecules(address,arr):
    file1=open(address,"r")
    allstr=file1.read()
    i=0
    j=0
    while (i<len(allstr)):
        j=allstr.find("@<TRIPOS>MOLECULE",j+1)
        if (j==-1):
            j=len(allstr)
        arr.append(rd.MolFromMol2Block(allstr[i:j]))
        i=j
def loadMoleculesFromChEMBL(accession):
    jsonn=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/targets/"+accession+"/bioactivities.json").read()
    return json.loads(jsonn)
class Molecule:
    def getStructure(self):
        string=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/compounds/"+self.id+".json").read()
        #print string
        bigjson=json.loads(string)
        self.json=bigjson["compound"]
        self.smiles=self.json["smiles"]
        
    pass
def filterChEMBLMolecules(arr):
    retarr=[]
    discard=[0,0,0,0,0,0,0]
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
        mol=Molecule()
        mol.id=line[u'ingredient_cmpd_chemblid']
        mol.pIC=-math.log(value)
        retarr.append(mol)
        discard[5]+=1
    return retarr
def getPossibles(arr,key):
    retarr=[]
    for line in arr:
        if not line[key] in retarr:
            retarr.append(line[key]);
    return retarr
#readMolecules("data/er_antagonist_decoys.mol2", decoy)
#readMolecules("data/er_antagonist_ligands.mol2", active)
#print len(decoy)
#print len(active)
chembl=loadMoleculesFromChEMBL("CHEMBL206")
#print chembl["bioactivities"][0]
#print getPossibles(chembl["bioactivities"],u'units')
filtrate=filterChEMBLMolecules(chembl["bioactivities"])
filtrate[0].getStructure()
print filtrate[0].__dict__


        







