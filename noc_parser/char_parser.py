__author__ = 'alm'
# parsing the knowledge noc_parser for Tony's NOC file

from datasets_pattern_code import noc
from pattern.text.en import referenced
import random
import logging
import sys

log = logging.getLogger('char_parser')

roles_file = '../datasets_pattern_code/role_classification_olli.xlsx'
adjectives_file = '../datasets_pattern_code/adjective_classification_olli.xlsx'

class FIELD:
    NAME = 'Character'
    POSITIVE = 'Positive Talking Points'
    NEGATIVE = 'Negative Talking Points'
    GENDER = 'Gender'
    POLITICS = 'Politics'
    MARRIED = 'Marital Status'
    FICTION = 'Fictive Status'
    CATEGORY = 'Category'
    OPPONENT = 'Opponent'

class KB_parser:

    def __init__(self):
        self.persons = noc.parse_rows(noc.NOC)
        self.roles = noc.parse_rows(roles_file)

        adj_sets = self._init_adjectives()
        self.weak_adjs = adj_sets[0]
        self.strong_adjs = adj_sets[1]

    def _init_adjectives(self):
        weak_adjs = []
        strong_adjs = []
        for row in noc.parse_rows(adjectives_file): # parse weak-strong lists
            if row['Weak']:
                weak_adjs.append(row['Adjective'])
            elif row['Strong']:
                strong_adjs.append(row['Adjective'])
        return weak_adjs, strong_adjs


    def get_people_from_kb(self):
        return self.persons

    def get_person(self, name):
        for person in self.persons:
            if person[FIELD.NAME] == name:
                return person
        return {'Character':'NOT FOUND'}


    def get_feature_of(self, name, field_):
        """ Get value of a given person & field
        get_value_of('Daniel Day-Lewis', FIELD.POSITIVE)
        """
        return self.get_person(name)[field_]

    def get_random_fictional_character_name(self):
        result = []
        for person in self.persons:
            if person[FIELD.FICTION]=='fictional':
                result.append(person)

        return random.choice(result)[FIELD.NAME]

    def get_random_fictional_character(self):
        result = []
        for person in self.persons:
            if person[FIELD.FICTION]=='fictional':
                result.append(person)

        return random.choice(result)

    def get_opponent_of(self, name):
        """Get oppononent, if multiple, return randomly one"""
        log.debug('Opponent for '+name)
        opponent = self.get_feature_of(name, FIELD.OPPONENT)
        if not opponent:
            log.debug('--> opponent undefined')
        if ',' in opponent:
            log.debug('return random opponent from '+opponent)
            return random.choice(opponent.split(',')).strip()
        return opponent.strip()

    def prefer_weak_emphathetic_features(self, pos_arr, max):
        """ try to pick adjectives that emphasize weakness of the hero
            if not find, take rest randomly
        """
        log.debug(pos_arr)
        for pos_feature in pos_arr:
            log.debug('loop pos feature \''+pos_feature+'\'')
            result = []
            if pos_feature in self.weak_adjs:
                log.debug('--> GOT WEAK MATCH')
                result.append(pos_feature)

        if len(result) > max:
            log.debug('Got enough items')
            return result[:max]
        else:
            for pos_feature in pos_arr:
                if pos_feature not in result:
                    if  pos_feature in self.strong_adjs:
                        log.debug('Ignored '+pos_feature+' as a strong one')
                    else:
                        pos_arr.remove(pos_feature)
                        result.append(pos_feature)
                if len(result) >= max:
                    return result
        return result

    def prefer_strong_negative_features(self, neg_arr, max):
        """ try to pick adjectives that emphasize weakness of the hero
            if not find, take rest randomly
        """
        log.debug(neg_arr)
        for neg_feature in neg_arr:
            log.debug('loop neg feature \''+neg_feature+'\'')
            result = []
            if neg_feature in self.strong_adjs:
                log.debug('--> GOT STRONG MATCH')
                result.append(neg_feature)

        if len(result) > max:
            log.debug('Got enough items')
            return result[:max]
        else:
            for neg_feature in neg_arr:
                if neg_feature not in result:
                    if  neg_feature in self.weak_adjs:
                        log.debug('Ignored '+neg_feature+' as a weak one')
                    else:
                        neg_arr.remove(neg_feature)
                        result.append(neg_feature)
                if len(result) >= max:
                    return result
        return result


    def add_article(self, word_seq_str):
        return referenced(word_seq_str)

    def positive_story_about(self, name):
        log.debug('CHARACTER: '+name)
        person_data = self.get_person(name)
        log.debug('POS: '+person_data[FIELD.POSITIVE])
        log.debug('NEG: '+person_data[FIELD.NEGATIVE])
        print 'This is a story about '+name+', '
        pos_feat = [x.strip() for x in person_data[FIELD.POSITIVE].split(',')]
        pos_weak = ', '.join(self.prefer_weak_emphathetic_features(pos_feat,2))
        married = person_data[FIELD.MARRIED].split(' ')[0]

        gender = person_data[FIELD.GENDER]
        if gender == 'male':
            gender = random.choice(['guy','male','man'])
        elif gender == 'female':
            gender = random.choice(['lady','female','woman'])


        print self.add_article(pos_weak)+', '+married+' '+gender

    def negative_story_about(self, name):
        log.debug('CHARACTER: '+name)
        person_data = self.get_person(name)
        log.debug('POS: '+person_data[FIELD.POSITIVE])
        log.debug('NEG: '+person_data[FIELD.NEGATIVE])
        print 'This is a story about '+name+', '
        pos_feat = [x.strip() for x in person_data[FIELD.NEGATIVE].split(',')]
        pos_weak = ', '.join(self.prefer_weak_emphathetic_features(pos_feat,2))
        married = person_data[FIELD.MARRIED].split(' ')[0]

        gender = person_data[FIELD.GENDER]
        if gender == 'male':
            gender = random.choice(['guy','male','man'])
        elif gender == 'female':
            gender = random.choice(['lady','female','woman'])


        print self.add_article(pos_weak)+', '+married+' '+gender









        #print person_data[FIELD.CATEGORY]



if __name__ == "__main__":
    # TODO:
    # DESCRIPTION OF CHARACTERS
    logging.basicConfig(level=logging.DEBUG)
    k = KB_parser()
    #print k.get_opponent_of('Darth Vader')
    #k.positive_story_about(k.get_random_fictional_character_name())
    k.positive_story_about('Darth Vader')
    k.positive_story_about('Clark Kent')
    #k.negative_story_about(k.get_random_fictional_character_name())
    #k.positive_story_about('Darth Vader')
    #print k.get_opponent_of(k.get_random_fictional_character_name())
    #
    #print k.get_people_from_kb()
    #print k.get_feature_of('Daniel Day-Lewis', FIELD.POSITIVE)
    #print k.get_feature_of('Daniel Day-Lewis', FIELD.NEGATIVE)
    #print k.get_feature_of('Darth Vader', FIELD.POSITIVE)
    #print k.get_feature_of('Darth Vader', FIELD.NEGATIVE)

