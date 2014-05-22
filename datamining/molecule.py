'''
Created on 21. 5. 2014

@author: Ringael
'''



class Molecule(object):
    '''
    classdocs
    '''
    smiles=False
    RDMol=False
    lastID=0
    def __init__(self,ID=None):
        if(ID==None):
            self.id=Molecule.lastID
            Molecule.lastID+=1
        else:
            self.id=ID
    def out(self):
        ret = {}
        ret["smiles"]=self.smiles
        ret["pIC"]=self.pIC
        ret["ID"]=self.id
        return ret
    
    def load(self,line):
        self.RDMol=line.RDMol
        self.activity=line.activity
        self.pIC = line.pIC
    def __getitem__(self, key):
        return self.__dict__[key]
 
    def __setitem__(self, key, value):
        self.__dict__[key] = value
 
    def __delitem__(self, key):
        del self.__dict__[key]