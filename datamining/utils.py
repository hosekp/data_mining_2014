'''
Created on 21. 5. 2014

@author: Ringael
'''


def implicit(params,key,impl):
    try:
        val=params[key]
        return val
    except KeyError:
        return impl

class Procents:
    def __init__(self,maxlen,stride=5):
        self.maxlen=maxlen
        self.i=0
        self.proc=0
        self.stride=stride
        print("Procent: "),
    def next(self):
        self.i+=1
        while (self.i>=(self.proc+self.stride)/100.0*self.maxlen):
            self.proc+=self.stride
            #print("\b\b"),
            if(self.proc>=100):
                print(100)
            else:
                print(str(self.proc)),
            #sys.stdout.write("Procent: "+str(self.proc)+"\r")
            #sys.stdout.flush()
            #print("Procent: "+str(self.proc)),
        
def foreach(array,func,arg1=None,arg2=None,arg3=None):
    for elem in array:
        func(elem,arg1,arg2,arg3)
def concatenate(arrs,params):
    ret=[]
    for arr in arrs:
        if isinstance(arr,str):
            continue
        ret.extend(arr)
    return ret 
def addValue(arr,params):
    for key, value in params.items():
        for elem in arr:
            elem[key]=value
    return arr
def spitter(arr,params):
    """
        params={"key","value","comparator"="="}
    """
    ret1=[]
    ret2=[]
    def more(attr,value):
        return attr>value
    def less(attr,value):
        return attr<value
    def equa(attr,value):
        return attr==value
    comparator=equa
    key=params["key"]
    value=params["value"]
    try:
        comp=params["comparator"]
        if comp==">":
            comparator=more
        if comp=="<":
            comparator=less
    except KeyError:
        pass
    for elem in arr:
        if comparator(elem[key],value):
            ret1.append(elem)
        else:
            ret2.append(elem)
    return ret1,ret2
#def map(array,func):
def getPossibles(arr,key=None):
    retarr=[]
    if(isinstance(arr,list)):
        for elem in arr:
            if not elem in retarr:
                retarr.append(elem);
    elif(isinstance(arr,dict)):
        for elem in arr:
            if not elem[key] in retarr:
                retarr.append(elem[key]);
    return retarr
