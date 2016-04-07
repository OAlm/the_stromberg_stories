from ani.data.LoadInitial import Load_Initial, GetPreambleActionsByKey
from ani.data.LoadMiddle import Load_Middle, GetActionsByKey, ExistsActionBykey
from ani.data.LoadEnd import LoadEnd,GetEndActionsByKey, ExistsEndActionsByKey
from ani.data.LoadIdioms import Load_Idioms, GetIdiomsActionsByKey, ExistsIdiomsActionsByKey
import random

from pattern.text.en import tag

import sys

initial = Load_Initial()
midpoint = Load_Middle()
end=LoadEnd()
idioms=Load_Idioms()
import logging
log = logging.getLogger('transition_initial_midpoint_end')

def get_mid_action_for_key(key, actions):
    key = key.strip()
    if key in actions:
        record = actions[key]
        sentences = record['Idiomatic Forms']
        sentence = random.choice(sentences.split(','))
        return sentence.strip()

    return '---INVALID MID-SENTENCE---'

def fill_A_and_B(sentence, a, b):
    result = []
    for word,pos in tag(sentence, tokenize=True):
        if word == 'A':
            result.append(a)
        elif word == 'B':
            result.append(b)
        else:
            result.append(word)

    return ' '.join(result)

def fill_A_and_B_arr(sentences, a,b):
    result = []
    for s in sentences:
        result.append(fill_A_and_B(s,a,b))
    return result

def get_story(a, b, actions, no_of_sentences=3, key='work_for'):
    log.debug('key: '+key+', action: '+key)

    count = 1
    if no_of_sentences < 3:
        log.error('give enough counts')
        return
    starts = get_starts(key)
    #print starts
    start = random.choice(starts)
    mids = []
    end = 'END_UNDEFINED'
    while(True):
        next_alternatives = get_mid(key)
        next_mid = random.choice(next_alternatives)
        print next_mid
        action_id = random.choice(next_mid[0])
        mid_sentence = get_mid_action_for_key(action_id, actions)

        mids.append(mid_sentence)
        count += 1
        if count >= no_of_sentences-1:
            print
            print 'end will be \''+random.choice(next_mid[1])+'\''
            end_candidate = get_end(random.choice(next_mid[1]))
            if end_candidate:
                end = random.choice(end_candidate)
                break
            else:
                count -= 1

    print 'start: '+fill_A_and_B(start, a, b)
    print 'mid  : '+str(fill_A_and_B_arr(mids, a, b))
    print 'end  : '+str(fill_A_and_B(end, a, b))


def detect_sentiment(sentence_candidates, actions):
    print sentence_candidates
    print len(sentence_candidates)
    print actions
    sys.exit(0)

def get_actions_by_sentiment(actions, tuple_a_b):
    result = []
    for action in actions:
        if actions[action]['sentiment'] == tuple_a_b:
            #print actions[action]['Idiomatic Forms']
            result.append(action)
    return result

def get_story_with_sentiment(a, b, actions, sentiment_flow_array):
    log.debug('get_story_with_sentiment')

    no_of_sentences = len(sentiment_flow_array)

    count = 1
    if no_of_sentences < 3:
        log.error('give enough counts')
        return

    ### TESTTEST
    #print sentiment_flow_array
    start_actions = get_actions_by_sentiment(actions,sentiment_flow_array[0])
    key = random.choice(start_actions)
    start = random.choice(get_starts(key))

    mids = []
    end = 'END_UNDEFINED'
    while(True):
        next_alternatives = get_mid(key)
        next_mid = random.choice(next_alternatives)
        print next_mid
        action_id = random.choice(next_mid[0])
        mid_sentence = get_mid_action_for_key(action_id, actions)

        mids.append(mid_sentence)
        count += 1
        if count >= no_of_sentences-1:
            print
            print 'end will be \''+random.choice(next_mid[1])+'\''
            end_candidate = get_end(random.choice(next_mid[1]))
            if end_candidate:
                end = random.choice(end_candidate)
                break
            else:
                count -= 1
        sys.exit(0)

    print 'start: '+fill_A_and_B(start, a, b)
    print 'mid  : '+str(fill_A_and_B_arr(mids, a, b))
    print 'end  : '+str(fill_A_and_B(end, a, b))





def get_starts(key):
    log.debug('key: '+key)
    preamble_list = GetPreambleActionsByKey(key,initial)
    return preamble_list

def get_mid(key):
    midpoints_triples=GetActionsByKey(key, midpoint)
    return midpoints_triples

def get_end(key):
    log.debug('get_end with key '+key)
    key = key.strip()
    return GetEndActionsByKey(key, end)
