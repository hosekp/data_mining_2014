'''
Created on 4. 6. 2014

@author: Ringael
'''

import pylab as pl
from utils import implicit

def plot2D(arr,params):
    Xattr=implicit(params,"X","id")
    Yattr=implicit(params,"Y","activity")
    plottype=implicit(params,"type","scatter")
    if(isinstance(Xattr,list)):
        Xtitle=implicit(params,"Xtitle",Xattr[0])
    else:
        Xtitle=implicit(params,"Xtitle",Xattr)
    if(isinstance(Xattr,list)):
        Ytitle=implicit(params,"Ytitle",Yattr[0])
    else:
        Ytitle=implicit(params,"Ytitle",Yattr)
    #show=implicit(params,"show",True)
    color=implicit(params,"color","b")
    title = implicit(params,"title","Zavislost "+Ytitle+" na "+Xtitle)
    if(arr[0]=="multiarray"):
        mlen=len(arr)-1
        if(not isinstance(Xattr,list)):
            Xattr=[Xattr for i in range(mlen)]
        if(not isinstance(Yattr,list)):
            Yattr=[Yattr for i in range(mlen)]
        if(not isinstance(color,list)):
            color=[color for i in range(mlen)]
        #print(Yattr)
        if plottype=="scatter":
            for i in range(mlen):
                X=[]
                Y=[]
                data=arr[i+1]
                if(len(data)==0):
                    continue
                print(str(i)+" : "+str(len(data)))
                for elem in data:
                    X.append(elem[Xattr[i]])
                    Y.append(elem[Yattr[i]])
                pl.scatter(X,Y,c=color[i])
            
    else:
        if plottype=="scatter":
            X=[]
            Y=[]
            for elem in arr:
                X.append(elem[Xattr])
                Y.append(elem[Yattr])
            pl.scatter(X,Y,c=color)
    pl.xlabel(Xtitle)
    pl.ylabel(Ytitle)
    pl.title(title)
    pl.show()
    return arr