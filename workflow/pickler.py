'''
Created on 21. 5. 2014

@author: Ringael
'''

try:
    import cPickle as pickle
except:
    import pickle

prefix="./data/"
def dump(url,obj):
    try:
        fil=open(prefix+url+".txt","w+")
        fil.write(pickle.dumps(obj))
        print(url+" saved")
    except:
        print(url+" cannot be save")

def load(url):
    try:
        fil=open(prefix+url+".txt","r")
        text=fil.read()
        #print(url+" loaded")
        return pickle.loads(text)
    except:
        print(url+" cannot be load")
        return None
def loadable(url):
    try:
        open(prefix+url+".txt","r")
        return True
    except:
        return False