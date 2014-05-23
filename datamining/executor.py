'''
Created on 21. 5. 2014

@author: Ringael
'''

import pickler

checked=False

def execute(network,final,pos=0):
    global checked
    if(not checked):
        checker(network,final)
    finode=network[final]
    if(len(finode.need)==0):
        arr=finode.do([])
    elif(len(finode.need)==1):
        if(len(finode.needpos)>0 and finode.needpos[0]>0):
            oldarr=execute(network,finode.need[0],finode.needpos[0])
            arr=finode.do(oldarr,pos)
        else:
            oldarr=execute(network,finode.need[0])
            arr=finode.do(oldarr,pos)
    else:
        if(len(finode.needpos)>0):
            oldarr1=execute(network,finode.need[0],finode.needpos[0])
            oldarr2=execute(network,finode.need[1],finode.needpos[1])
        else:
            oldarr1=execute(network,finode.need[0])
            oldarr2=execute(network,finode.need[1])
        arr=finode.do2(oldarr1,oldarr2,pos)
    print ("executed node "+str(final))
    return arr;
        
def checker(network,final,pos=0):
    finode=network[final]
    if(len(finode.need)==0):
        valid=True
    elif(len(finode.need)==1):
        if(len(finode.needpos)>0 and finode.needpos[0]>0):
            valid=checker(network,finode.need[0],finode.needpos[0])
        else:
            valid=checker(network,finode.need[0])
    else:
        if(len(finode.needpos)>0):
            valid=checker(network,finode.need[0],finode.needpos[0])
            valid=valid and checker(network,finode.need[1],finode.needpos[1])
        else:    
            valid=checker(network,finode.need[0])
            valid=valid and checker(network,finode.need[1])
    valid=valid and finode.check(pos)
    if(not valid):
        finode.invalidate()
    return valid


class Node:
    name="generic"
    arr=None
    func=lambda x : x
    
    def __init__(self,name,func,need=[],needpos=[],params=None):
        self.name=name
        self.func=func
        self.need=need
        self.needpos=needpos
        self.params=params
        self.arr=pickler.load(self.name)
        self.arr2=pickler.load(self.name+"_2")
    
    def do(self,array,pos=0):
        if(self.arr==None):
            self.arr=self.func(array,self.params)
            if(isinstance(self.arr,tuple)):
                self.arr2=self.arr[1]
                self.arr=self.arr[0]
                pickler.dump(self.name+"_2", self.arr2)
            pickler.dump(self.name, self.arr)
        if(pos==0):
            return self.arr
        else:
            #print(self.name+" vraci arr2")
            return self.arr2
    def do2(self,array1,array2,pos=0):
        if(self.arr==None):
            self.arr=self.func(array1,array2,self.params)
            if(isinstance(self.arr,tuple)):
                self.arr2=self.arr[1]
                self.arr=self.arr[0]
                pickler.dump(self.name+"_2", self.arr2)
            pickler.dump(self.name, self.arr)
        if(pos==0):
            return self.arr
        else:
            return self.arr2
    
    def invalidate(self):
        self.arr=None
        self.arr2=None
    def check(self,pos=0):
        if(pos==0):
            return self.arr!=None
        else:
            return self.arr2!=None

