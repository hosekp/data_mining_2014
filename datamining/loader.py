'''
Created on 21. 5. 2014

@author: Ringael
'''

import httplib
import socket
import ssl

def connect(self):
    "Connect to a host on a given (SSL) port."
    sock = socket.create_connection((self.host, self.port),
                                        self.timeout, self.source_address)
    if self._tunnel_host:
        self.sock = sock
        self._tunnel()
    self.sock = ssl.wrap_socket(sock, self.key_file,
                                self.cert_file,
                                ssl_version=ssl.PROTOCOL_TLSv1)

httplib.HTTPSConnection.connect = connect
import urllib2
import json
import rdkit.Chem as rd

chembl_all=False

if __name__ == '__main__':
    pass

def loadMoleculesFromChEMBL(arr,accession):
    address="http://www.ebi.ac.uk/chemblws/targets/"+accession+"/bioactivities.json"
    #print(address)
    #jsonn=urllib2.urlopen(address).read()   #  fallback
    jsonn=open("./data/"+accession+".json").read()
    return json.loads(jsonn)[u'bioactivities']
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
def getRDMolFromChEMBL(arr,params):
    #retarr=[]   # fallback
    for molec in arr:
        #retarr.append(molec.id)  # fallback
        #continue   #fallback
        molec.smiles=getSmilesFromChEMBLFall(molec.id) # fallback
        #molec.smiles=getSmilesFromChEMBL(molec.id)
        molec.RDMol=rd.MolFromSmiles(molec.smiles)
        if(not molec.RDMol):
            #print(molec.id+" not converted")
            arr.remove(molec)
            #print(molec.id)
    #return retarr  # fallback
    return arr
        #return self.RDMol
def getSmilesFromChEMBL(cid):
    string=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/compounds/"+cid+".json").read()

    bigjson=json.loads(string)
    smalljson=bigjson["compound"]
    return str(smalljson["smiles"])
def getSmilesFromChEMBLFall(cid):
    global chembl_all   # fallback
    #string=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/compounds/"+cid+".json").read()
    if not chembl_all:  # fallback
        chembl_all=json.loads(open("./data/CHEMBL_all.json").read())
    return str(chembl_all[cid]["smiles"])