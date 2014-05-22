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

if __name__ == '__main__':
    pass

def loadMoleculesFromChEMBL(arr,accession):
    address="http://www.ebi.ac.uk/chemblws/targets/"+accession+"/bioactivities.json"
    #print(address)
    jsonn=urllib2.urlopen(address).read()
    #jsonn=open("./data/"+accession+".json").read()
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
    for molec in arr:
        molec.smiles=getSmilesFromChEMBL(molec.id)
        try:
            molec.RDMol=rd.MolFromSmiles(molec.smiles)
        except:
            print(molec.id+" not converted")
    return arr
        #return self.RDMol
def getSmilesFromChEMBL(cid):
    string=urllib2.urlopen("http://www.ebi.ac.uk/chemblws/compounds/"+cid+".json").read()
    #string="http://www.ebi.ac.uk/chemblws/compounds/"+cid+".json"
    #print(string)
    #print string
    bigjson=json.loads(string)
    smalljson=bigjson["compound"]
    return str(smalljson["smiles"])