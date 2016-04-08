__author__ = 'derrall, ani'

import sys
from collections import defaultdict
from random import randint
import random

def Load_NOC():
    filepath = '../datasets/veale_noc_improved.tsv'

    lines = open(filepath,'r').readlines()
    dict = defaultdict()

    #print len(lines)
    #print lines[0]

    for i,line in enumerate(lines):
        if i == 0:
            continue
        items = line.strip().split("\t")
        try:
            Character= items[0]
            Canonical_Name= items[1].split(',')
            Gender = items[2].split(',')
            Address_1 = items[3].split(',')
            Address_2 = items[4].split(',')
            Address_3 = items[5]
            Politics= items[6].strip().split(',')
            Marital_Status= items[7].split(',')
            Opponent= items[8].split(',')
            Typical_Activity= items[9].strip().split(',')
            Vehicle_of_Choice= items[10].strip().split(',')
            Weapon_of_Choice= items[11].split(',')
            Seen_Wearing= items[12].strip().split(',')
            Domains= items[13].strip().split(',')
            Genres= items[14].split(',')
            Fictive_Status= items[15].split(',')
            Portrayed_By= items[16].split(',')
            Creator= items[17].split(',')
            Creation= items[18].split(',')
            Group_Affiliation= items[19].split(',')
            Fictional_World= items[20].split(',')
            Category= items[21].lower().split(', ')
            Negative_Talking_Points= items[22].split(',')
            Positive_Talking_Points= items[23].split(',')
            Sentiment= items[24]

            dict[Character] = (Character,Canonical_Name,Gender,Address_1,Address_2,Address_3,Politics,Marital_Status,Opponent,Typical_Activity,Vehicle_of_Choice,Weapon_of_Choice,Seen_Wearing,Domains,Genres,Fictive_Status,Portrayed_By,Creator,Creation,Group_Affiliation,Fictional_World,Category,Negative_Talking_Points,Positive_Talking_Points,Sentiment)
        except:
            print(line)
    return dict

def GetActionScoreByKey(key, dict):
    return dict[key]


def GetPositiveCharacter(dict,domain=None):
    chars=[]
    for key in dict.keys():

        tuple=dict[key]
        # print(tuple[len(tuple)-1])
        if(domain!=None and not tuple[13].__contains__(domain)):
            continue
        if(int(tuple[len(tuple)-1])==1):
            chars.append(tuple[0])
    return chars[randint(0,len(chars)-1)]

def GetNegativeCharacter(dict,domain=None):
    chars=[]
    for key in dict.keys():
        tuple=dict[key]
        if(domain!=None and not tuple[13].__contains__(domain)):
            continue
        if(int(tuple[len(tuple)-1])==-1):
            chars.append(tuple[0])
    return chars[randint(0,len(chars)-1)]

def GetPositiveCharacterAndNegativeCharater(dict):
    pos_chars=[]
    neg_chars=[]
    for key in dict.keys():
        tuple=dict[key]
        # print(tuple[len(tuple)-1])
        if(int(tuple[len(tuple)-1])==1):
            pos_chars.append(tuple[0])
        if(int(tuple[len(tuple)-1])==-1):
            neg_chars.append(tuple[0])
    return random.choice(pos_chars),random.choice(neg_chars)


def getcharacter_activity(dict,name):
        tuple=dict[name]
        return tuple[9]

def getpositive_point(dict,name):
        tuple=dict[name]
        return tuple[22]
def getnegative_point(dict,name):
        tuple=dict[name]
        return tuple[23]

def getdomain(dict,name):
        tuple=dict[name]
        return tuple[13]

def getcategory(dict,name):
        tuple=dict[name]
        return tuple[21]
def getpeoplebycategory(dict,name):
    people=[]
    for key in dict.keys():
        tuple=dict[key]
        if(tuple[21].__contains__(name)):
            people.append(key)
    return people

def get_certain_field(dict,index):
    field=set()
    for key in dict.keys():
        tuple=dict[key]
        for x in tuple[index]:
            field.add(x)
    return field







# def GetOpponents(dict):
#     keys=dict.keys()
#     opponent=None
#     hero=None
#     while(opponent==None):
#         index=randint(0,len(keys)-1)
#         tuple = dict.get(keys[index])
#         if(tuple[8][0]!=''):
#             hero=keys[index]
#             opponent=tuple[8]
#     return hero, opponent[randint(0,len(opponent)-1)]
#


