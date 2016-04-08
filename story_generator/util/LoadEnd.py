import sys
from collections import defaultdict

def LoadEnd():
    filepath = "../datasets/closing_bookend_actions.tsv"

    lines = open(filepath,'r').readlines()

    dict = defaultdict()

    for i,line in enumerate(lines):
        if i == 0:
            continue

        items = line.split("\t")

        key = items[0]
        stories = items[1]
        actions = items[2].strip().split(',')

        dict[key] = (stories, actions)


    return dict

def ExistsEndActionsByKey(key,dict):
    if(dict.keys().__contains__(key)):
        return True
    return False


def GetEndActionsByKey(key, dict):
    if key in dict:
        return dict[key][1]
    else:
        return []

def GetStoriesCountByKey(key, dict):
    return dict[key][0]