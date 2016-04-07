import sys
from collections import defaultdict

def Load_Idioms():
    filepath = "../resource/skelatrics/Veale's idiomatic actions.tsv"

    lines = open(filepath,'r').readlines()
    dict = defaultdict()

    for i,line in enumerate(lines):
        if i == 0:
            continue

        items = line.split("\t")
        key = items[0]
        uses = items[1]
        forms = items[2]
        iforms = items[3].strip().split(',')
        dict[key] = (uses,forms, iforms)
    return dict

def GetIdiomsActionsByKey(key, dict):
    return dict[key][2]

def GetStoriesCountByKey(key, dict):
    return dict[key][1]

def GetUsesCountByKey(key, dict):
    return dict[key][0]

def ExistsIdiomsActionsByKey(key,dict):
    if(dict.keys().__contains__(key)):
        return True
    return False