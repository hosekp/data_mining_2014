'''
Created on 21. 5. 2014

@author: Ringael
'''

def foreach(array,func,arg1=None,arg2=None,arg3=None):
    for elem in array:
        func(elem,arg1,arg2,arg3)
def concatenate(array,array2,params):
    return array+array2
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
