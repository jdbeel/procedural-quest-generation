from planning import *

knowledge_list = [['getfromloaction', 'move', 'giveto'], ['spy'], ['move', 'listen', 'move', 'report'], ['getfromlocation', 'move', 'use', 'move', 'giveto']]
comfort_list = [['getfromlocation', 'move', 'giveto'], ['move', 'damage', 'move', 'report']]
reputation_list = [['getfromlocation', 'move', 'giveto'], ['move', 'kill', 'move','report'], ['move', 'move', 'report']]
serenity_list = [['move', 'damage'], ['getfromlocation', 'move', 'use', 'move', 'giveto'], ['getfromloaction', 'move', 'use', 'capture', 'move', 'giveto'], ['move', 'listen', 'move', 'report'], ['move', 'take', 'move', 'giveto'], ['getfromloaction', 'move', 'giveto'], ['move', 'damage', 'escort', 'move', 'report']]
protection_list = [['move', 'damage', 'move', 'report'], ['getfromlocation', 'move', 'use'], ['move', 'repair'], ['getfromlocation', 'move', 'use'], ['move', 'damage'], ['move', 'repair'], ['move', 'defend']]
conquest_list = [['move','damage'], ['move','steal','move','giveto']]
wealth_list = [['move','getfromlocation'],['move','stealth'],['repair']]
ability_list = [['repair','use'], ['getfromlocation','use'],['use'],['damage'],['use'],['getfromlocation','use'],['getfromlocation','experiment']]
equipment_list = [['repair'], ['getfromlocation', 'move', 'giveto'], ['stealth'], ['move', 'exchange']]

motivation_dict = {'Knowledge': knowledge_list, 'Comfort':comfort_list, 'Reputation': reputation_list, 'Serenity': serenity_list, 'Protection':protection_list, 'Conquest': conquest_list, 'Wealth': wealth_list, 'Ability':ability_list, 'Equipment': equipment_list}

def is_subsequence(x, y):
    '''
    :param x: strategy
    :param y: sequence of actions
    :return: true if x is subsequence of y
    '''

    flag = True
    for s in x:
        if s in y:
            flag *= True
        else:
            flag *= False
    return bool(flag)

def lcs(x, y, m, n):
    '''
    :param x: strategy
    :param y: sequence of actions
    :param m: len(strategy)
    :param n: len(sequence)
    :return: length of longest common subsequence
    '''
    if m == 0 or n == 0:
       return 0
    elif x[m-1] == y[n-1]:
       return 1 + lcs(x, y, m-1, n-1)
    else:
       return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))
def classifier(quest):
    '''
    :param quest: given the quest generated from planning.py
    :return: the motivation which gets the largest score
    '''
    sequence = [string.split(' ')[0] for string in quest]
    # print(sequence)
    scores = {}
    # print(motivation_dict)
    for motivation in motivation_dict:
        scores[motivation] = 0
        n = len(motivation_dict[motivation])
        for strategy in motivation_dict[motivation]:
            if is_subsequence(strategy, sequence):
                # scores[motivation] += 1/(n*len(strategy))
                scores[motivation] += 1/n
            else:
                scores[motivation] += 1/(n*len(strategy)) * lcs(strategy, sequence, len(strategy), len(sequence))
                # print('hahahahah')
    label = sorted(scores, key=scores.get, reverse=True)[0]
    return scores, label

def main():
    quest = plan("(and (has Aladdin lamp) (captive you Aladdin) (used lamp))", "Aladdin")
    # print(quest)
    scores = classifier(quest)[0]
    label = classifier(quest)[1]
    print(scores)
    print(label)
if __name__ == '__main__':
    main()