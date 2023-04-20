import pandas as pd
from tkinter import messagebox

def dataExtract(lst):
    data=pd.read_csv("data.csv")
    diction=data.to_dict()
    for i in diction.keys():
        lst[i]=[]
        for j in diction[i].values():
            if not pd.isna(j):
                lst[i].append(j)


def quota_lst(diction):
    lst=[]
    for i in diction.keys():
        lst.append(i)
    for i in range(4):
        lst.pop(0)
    lst.insert(0,"--Select-Quota--")
    return lst


def branch_lst(diction):
    lst=[]
    for i in diction["Branch"]:
        lst.append(i)
    lst=set(lst)
    lst=list(lst)
    lst.sort()
    return lst


def location_lst(diction):
    lst=[]
    for i in diction["Location"]:
        temp=i.split(",")
        lst.append(temp[len(temp)-1].lstrip())
    lst=set(lst)
    lst=list(lst)
    lst.sort()
    return lst