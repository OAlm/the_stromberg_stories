import sys
from collections import defaultdict

def LoadCharProfiles():
    filepath = "../datasets/inter_category_Relationships.tsv"

    lines = open(filepath,'r').readlines()

    dict = defaultdict()

    for i,line in enumerate(lines):
        if i == 0:
            continue

        items = line.split("\t")
        labels = items[0].strip().split(":")
        subject = items[1]
        actions = items[2].strip().split(',')
        object = items[3].strip()

        for action in actions:
            if(dict.__contains__(action)):
                dict.get(action).append((labels[0],labels[1],subject,object))
            else:
                l=list()
                l.append((labels[0],labels[1],subject,object))
                dict[action] = l
    return dict

def ExistsCharActionsByKey(key,dict):
    if(dict.keys().__contains__(key)):
        return True
    return False

def GetCharByAction(key, dict, subject_label=None, object_label=None):
    result=dict[key]
    filtered_result=[]
    if(subject_label != None and object_label==None):
        for (ls,lo,subject,object) in result:
            if(subject_label==ls):
                filtered_result.append((ls,lo,subject,object))
        return filtered_result

    if(object_label != None and subject_label==None):
        for (ls,lo,subject,object) in result:
            if(object_label==lo):
                filtered_result.append((ls,lo,subject,object))
        return filtered_result

    if(object_label != None and subject_label!=None):
        for (ls,lo,subject,object) in result:
            if(object_label==lo and subject_label==ls):
                filtered_result.append((ls,lo,subject,object))
        return filtered_result
