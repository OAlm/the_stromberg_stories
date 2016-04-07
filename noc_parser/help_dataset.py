__author__ = 'alm'

from datasets_pattern_code import noc

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

def character_role_extractor():
    result = []
    for person in noc.parse_rows(noc.NOC):
        if person[FIELD.CATEGORY]:
            val = person[FIELD.CATEGORY]
            if ',' in val:
                for v in val.split(','):
                    result.append(v.strip())
            else:
                result.append(val.strip())
    return sorted(list(set(result)))

def character_feature_extractor():
    result = []
    for person in noc.parse_rows(noc.NOC):
        if person[FIELD.POSITIVE]:
            val = person[FIELD.POSITIVE]
            if ',' in val:
                for v in val.split(','):
                    result.append(v.strip())
            else:
                result.append(val.strip())
        if person[FIELD.NEGATIVE]:
            val = person[FIELD.NEGATIVE]
            if ',' in val:
                for v in val.split(','):
                    result.append(v.strip())
            else:
                result.append(val.strip())

    return sorted(list(set(result)))


if __name__ == '__main__':
    for line in character_feature_extractor():
        print line

