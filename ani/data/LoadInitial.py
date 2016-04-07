import sys
from collections import defaultdict

def Load_Initial():
    filepath = "../resource/skelatrics/Veale's initial bookend actions.tsv"

    lines = open(filepath,'r').readlines()
    dict = defaultdict()

    for i,line in enumerate(lines):
        if i == 0:
            continue

        items = line.split("\t")

        key = items[0]
        uses = items[1]
        stories = items[2]
        actions = items[3].strip().split(',')
        dict[key] = (uses,stories, actions)
    return dict

def GetPreambleActionsByKey(key, dict):
    return dict[key][2]

def GetStoriesCountByKey(key, dict):
    return dict[key][1]

def GetUsesCountByKey(key, dict):
    return dict[key][0]

