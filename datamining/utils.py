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
#def map(array,func):
