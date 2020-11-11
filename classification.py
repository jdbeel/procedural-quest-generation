from planning import plan

KNOWLEDGE_LIST = [
    ['getfromloaction', 'move', 'giveto'], 
    ['spy'], 
    ['move', 'listen', 'move', 'report'], 
    ['getfromlocation', 'move', 'use', 'move', 'giveto']
]
COMFORT_LIST = [
    ['getfromlocation', 'move', 'giveto'], 
    ['move', 'damage', 'move', 'report']
]
REPUTATION_LIST = [
    ['getfromlocation', 'move', 'giveto'],
    ['move', 'kill', 'move','report'], 
    ['move', 'move', 'report']
]
SERENITY_LIST = [
    ['move', 'damage'], 
    ['getfromlocation', 'move', 'use', 'move', 'giveto'], 
    ['getfromloaction', 'move', 'use', 'capture', 'move', 'giveto'], 
    ['move', 'listen', 'move', 'report'], 
    ['move', 'take', 'move', 'giveto'], 
    ['getfromloaction', 'move', 'giveto'], 
    ['move', 'damage', 'escort', 'move', 'report']
]
PROTECTION_LIST = [
    ['move', 'damage', 'move', 'report'], 
    ['getfromlocation', 'move', 'use'], 
    ['move', 'repair'], 
    ['getfromlocation', 'move', 'use'], 
    ['move', 'damage'], 
    ['move', 'repair'], 
    ['move', 'defend']
]
CONQUEST_LIST = [
    ['move','damage'], 
    ['move','steal','move','giveto']
]
WEALTH_LIST = [
    ['move','getfromlocation'],
    ['move','stealth'],['repair']
]
ABILITY_LIST = [
    ['repair','use'], 
    ['getfromlocation','use'],
    ['use'],
    ['damage'],
    ['use'],
    ['getfromlocation','use'],
    ['getfromlocation','experiment']
]
EQUIPMENT_LIST = [
    ['repair'], 
    ['getfromlocation', 'move', 'giveto'], 
    ['stealth'], 
    ['move', 'exchange']
]

MOTIVATION_DICT = {
    'Knowledge': KNOWLEDGE_LIST, 
    'Comfort':COMFORT_LIST, 
    'Reputation': REPUTATION_LIST, 
    'Serenity': SERENITY_LIST, 
    'Protection':PROTECTION_LIST, 
    'Conquest': CONQUEST_LIST, 
    'Wealth': WEALTH_LIST, 
    'Ability':ABILITY_LIST, 
    'Equipment': EQUIPMENT_LIST
}

def is_subsequence(strat, actions):
    """Determines whether or not strat is a subsequence of plan.

    :param strat: Strategy, i.e. one of the keys of MOTIVATION_DICT.
    :param actions: A sequence of actions.
    :return: True if strat is subsequence of actions.
    """

    flag = True
    for s in strat:
        if s in actions:
            flag *= True
        else:
            flag *= False
    return bool(flag)

def lcs(strategy, actions, m, n):
    """Computes the length of the longest common subsequence between strategy
    actions.

    :param strategy: The strategy.
    :param actions: sequence of actions.
    :param m: len(strategy)
    :param n: len(actions)
    :return: length of longest common subsequence
    """
    if m == 0 or n == 0:
       return 0
    elif strategy[m-1] == actions[n-1]:
       return 1 + lcs(strategy, actions, m-1, n-1)
    else:
       return max(lcs(strategy, actions, m, n-1), lcs(strategy, actions, m-1, n))

def classifier(quest):
    """Assigns the given quest a score for each motivation, which
    is the number of occurences of sequences associated with that
    strategy in the plan divided by the number of sequences associated
    with that strategy.

    :param quest: given the quest generated from planning.py
    :return: the motivation which gets the largest score
    """
    sequence = [string.split(' ')[0] for string in quest]
    scores = {}
    for motivation in MOTIVATION_DICT:
        scores[motivation] = 0
        n = len(MOTIVATION_DICT[motivation])
        for strategy in MOTIVATION_DICT[motivation]:
            if is_subsequence(strategy, sequence):
                scores[motivation] += 1/n
            else:
                scores[motivation] += 1/(n*len(strategy)) * lcs(strategy, sequence, len(strategy), len(sequence))
    label = sorted(scores, key=scores.get, reverse=True)[0]
    return scores, label

def test():
    quest = plan("(and (has Aladdin lamp) (captive you Aladdin) (used lamp))", "Aladdin")
    scores = classifier(quest)[0]
    label = classifier(quest)[1]
    print(scores)
    print(label)

if __name__ == '__main__':
    test()