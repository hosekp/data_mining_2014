'''
Created on 21. 5. 2014

@author: Ringael
'''

import pickler

checked=False

class CheckError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
def oldchecker(network,final,pos=0):
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
            valid=checker(network,finode.need[1],finode.needpos[1]) and valid
        else:    
            valid=checker(network,finode.need[0])
            valid=checker(network,finode.need[1]) and valid
    valid=valid and finode.check()
    if(not valid):
        finode.invalidate()
    return valid

def checker(network,final,pos):
    finode=network[final]
    valid=True
    for i in range(len(finode.need)):
        if(network[finode.need[i]]==finode):
            raise CheckError("Self-recursion, please check dependencies")
        valid=checker(network,finode.need[i],finode.needpos[i]) and valid
    valid=valid and finode.check()
    if(not valid):
        finode.invalidate()
    return valid

def oldexecute(network,final,pos=0):
    global checked
    if(not checked):
        checker(network,final,pos)
        checked=True
    finode=network[final]
    if(len(finode.need)==0):
        arr=finode.do([],pos)
    elif(len(finode.need)==1):
        oldarr=execute(network,finode.need[0],finode.needpos[0])
        arr=finode.do(oldarr,pos)
    elif(len(finode.need)==2):
        oldarr1=execute(network,finode.need[0],finode.needpos[0])
        oldarr2=execute(network,finode.need[1],finode.needpos[1])
        arr=finode.do2(oldarr1,oldarr2,pos)
    else:
        arrs=["multiarray"]
        for i in range(len(finode.need)):
            arrs.append(execute(network,finode.need[i],finode.needpos[i]))
        arr=finode.doX(arrs,pos)
    print ("executed node "+str(final))
    return arr;

def execute(network,final,pos=0):
    global checked
    if(not checked):
        checker(network,final,pos)
        checked=True
        print("Checking completed")
    finode=network[final]
    if(len(finode.need)==0):
        arr=finode.do([],pos)
    elif(len(finode.need)==1):
        neednode=network[finode.need[0]]
        if neednode.check():
            oldarr=neednode.getArr(finode.needpos[0])
        else:
            oldarr=execute(network,finode.need[0],finode.needpos[0])
        arr=finode.do(oldarr,pos)
    else:
        arrs=["multiarray"]
        for i in range(len(finode.need)):
            neednode=network[finode.need[i]]
            if neednode.check():
                arrs.append(neednode.getArr(finode.needpos[i]))
            else:
                arrs.append(execute(network,finode.need[i],finode.needpos[i]))
        arr=finode.doX(arrs,pos)
    print ("executed node "+str(final))
    return arr;
        


class Node:
    name="generic"
    arr=None
    arr2=None
    func=lambda x : x
    valid=False
    
    def __init__(self,name,func,need=[],needpos=[],params=None):
        self.name=name
        self.func=func
        self.need=need
        self.needpos=needpos
        while(len(needpos)<len(need)):
            needpos.append(0)
        self.params=params
        self.valid=pickler.loadable(self.name)
        #self.arr=pickler.load(self.name)
        #self.arr2=pickler.load(self.name+"_2")
    def getArr(self,pos):
        if self.arr==None:
            self.arr=pickler.load(self.name)
            self.arr2=pickler.load(self.name+"_2")
        if(pos==0):
            return self.arr
        else:
            return self.arr2
    
    def do(self,array,pos):
        if(self.arr==None):
            self.arr=self.func(array,self.params)
            if(isinstance(self.arr,tuple)):
                self.arr2=self.arr[1]
                self.arr=self.arr[0]
                pickler.dump(self.name+"_2", self.arr2)
            pickler.dump(self.name, self.arr)
            self.valid=True
        return self.getArr(pos)
    def olddo2(self,array1,array2,pos):
        if(self.arr==None):
            self.arr=self.func(array1,array2,self.params)
            if(isinstance(self.arr,tuple)):
                self.arr2=self.arr[1]
                self.arr=self.arr[0]
                pickler.dump(self.name+"_2", self.arr2)
            pickler.dump(self.name, self.arr)
            self.valid=True
        return self.getArr(pos)
    def doX(self,arrs,pos):
        if(self.arr==None):
            self.arr=self.func(arrs,self.params)
            if(isinstance(self.arr,tuple)):
                self.arr2=self.arr[1]
                self.arr=self.arr[0]
                pickler.dump(self.name+"_2", self.arr2)
            pickler.dump(self.name, self.arr)
            self.valid=True
        return self.getArr(pos)
    
    def invalidate(self):
        self.arr=None
        self.arr2=None
        self.valid=False
        print(self.name+" invalidated")
    def check(self):
        return self.valid==True
        #return self.arr!=None

