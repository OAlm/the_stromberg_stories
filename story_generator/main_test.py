__author__ = 'all'

import logging

import story_generator as t
from datasets_pattern_code import noc
import loadNOC


def action_relations():
    action_relations = noc.parse_rows('../datasets/ActionRelation2.xlsx')
    result = {}
    for ar in action_relations:
        tuple_ = int(ar['A'].replace('v','')), int(ar['B'].replace('v',''))
        result[ar['Action']] = tuple_
    return result

def parse_actions():
    actions= noc.parse_rows('../datasets/idiomatic_actions.xlsx')
    ar_dict = action_relations()
    result = {}
    for action in actions:
        action['sentiment'] = ar_dict[action['Action']]
        result[action['Action']] = action

    return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    actions = parse_actions()
    #print actions

    A = 'Joker'
    B = 'Batman'


    nocs = loadNOC.Load_NOC()
    #print actions

    A = 'The Joker'
    B = 'Batman'

    BB,AA = loadNOC.GetPositiveCharacterAndNegativeCharater(nocs)

    print AA
    print BB

    sentiment_arr = [(0,0),(-1,0),(-2,0),(1,-1),(2,-2),(2,0)]

    #t.get_story(A, B, actions, no_of_sentences=6, key='marry')

    #sent_arr =

    t.get_story_with_sentiment(A, B, actions, sentiment_flow_array=sentiment_arr)









