import random

PPDL_DIR = "ppdl"

def parse_goals(domain_str):
    """Processes possible actions to determine the domain of possible goals.
    
    :param domain_str: The initial domain, PPDL code in a string.
    """
    domain_list=domain_str.split(":")
    effects=[]
    for i in domain_list:
        if i[0:6]=="effect":
            for j in range(len(i)):
                if i[j:j+9]=="(increase":
                    break
                elif "))" in i[j:] and i[j:j+4]=="(not":
                    effects.append(i[j:i.index("))",j)+2])
                elif ")" in i[j:] and i[j]=="(" and i[j:j+4]!="(and":
                    effects.append(i[j:i.index(")",j)+1])
    return effects

def parse_world(initState_str, mapping):
    """Grabs a list of all possible objects that match a particular mapping.
    
    :param initState_str: The initial state of the game world, PPDL code in a string.
    :param mapping: The mapping to check against.
    """
    m = "("+mapping
    IS_list=initState_str.split('\n')
    objects=[]
    for i in IS_list:
        if i.split()[0]==m:
            objects.append(i.split()[1][:-1])
    return objects

def generate(seed=None):
    """Generates a random amount of goals in a range and assigns
    qualifiers (characters, items, locations, ...) to each placeholder.
    Currently, more common end goals appear more frequently.

    :param seed: The seed to use for random number generation, defaults to None
    :return: The goal string, which is the and of several predicates.
    """
    random.seed(seed)
    goalN = random.randint(3,6)

    with open(PPDL_DIR + "/domain.ppdl", "r") as f:
        domain_str = f.read()
    with open(PPDL_DIR + "/initial_state.ppdl", "r") as f:
        initState_str = f.read()

    goalSample = [goal for goal in parse_goals(domain_str) if goal.split()[0] != "(not"]
    if len(goalSample)==0:
        raise IndexError('No possible goals')
    
    goals=[]
    special=["captive","has"] # Unique goals, ask if curious
    mappings={"p":"player","c":"character","i":"item","l":"location","m":"monster","info":"information","d":"character","charB":"character","t":"location","f":"location"}
    for i in range(goalN):
        g = random.choice(goalSample)
        n=None
        if g[-2]==")":
            n=True
            g2=g[:-2].split()
        else:
            n=False
            g2=g[:-1].split()
        for j in range(len(g2)):
            if g2[j][0]=="?":
                mapping=None
                if g2[j][1:] in mappings.keys():
                    mapping=mappings[g2[j][1:]]
                elif g2[j][1:-1] in mappings.keys():
                    mapping=mappings[g2[j][1:-1]]
                if mapping==None:
                    raise IndexError('Parameter not hardcoded properly')
                mapSample = parse_world(initState_str,mapping)
                m = random.choice(mapSample)
                g2[j]=m
        g=" ".join(g2)+"))" if n else " ".join(g2)+")"
                
        # Eliminates duplicate or conflicting goals
        bad=False
        for j in goals:
            j2=j.split()
            g2=g.split()
            if g2[0]=="(not" and j2[0] == "(not": # For comparison, not doesnt matter if equal
                g2=g2[1:]
                j2=j2[1:]
            if g2[0]=="(not" and j2[0] != "(not": # Only bad if not 'g' and 'g'
                j2[-1]=j2[-1]+")"
                if g2[1:]==j2[0:]:
                    bad=True
            elif j2[0]=="(not" and g2[0] != "(not":
                g2[-1]=g2[-1]+")"
                if j2[1:]==g2[0:]:
                    bad=True
            elif g2[0][1:] not in special and j2[0:2]==g2[0:2]:
                bad=True
            elif g2[0][1:] in special and j2[0]==g2[0] and j2[2]==g2[2]:
                bad=True
        if bad==False:
            goals.append(g)
    goalStr="(and "+" ".join(goals)+")"
    return goalStr

if __name__ == "__main__":
    print(generate())
