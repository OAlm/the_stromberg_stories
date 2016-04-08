import sys
from collections import defaultdict

def Load_Middle():
    filepath = '../datasets/script_midpoints.tsv'

    lines = open(filepath,'r').readlines()

    dict = defaultdict()

    for i,line in enumerate(lines):
        if i == 0:
            continue

        items = line.split("\t")

        beforemid = items[0].strip().split(',')
        midpoint = items[1].strip().split(',')
        aftermid = items[2].strip().split(',')
        exemplars = items[3].strip().split(":")

        for key in beforemid:
            if dict.__contains__(key):
                entry = dict.get(key)
                entry.append((midpoint, aftermid, exemplars))

            else:
                entry = list()
                entry.append((midpoint, aftermid, exemplars))
                dict[key] = entry

    #print dict['are_pushed_too_far_by']
    return dict

def GetActionsByKey(key, dict, midpoint=None, aftermidpoint=None):
    entry = dict.get(key)
    filtered_list=[]
    if(midpoint!=None):
        for (bm,am,es) in entry:
            if(bm.__contains__(midpoint)):
                filtered_list.append((bm,am,es))
        for (bm,am,es) in entry:
            if(bm.__contains__(aftermidpoint)):
                filtered_list.append((bm,am,es))

    print(filtered_list)
    return entry

def ExistsActionBykey(key,dict):
    if(dict.keys().__contains__(key)):
        return True
    return False

