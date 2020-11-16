from pprint import pprint
import random
import time

from generation import generate
from planning import plan
from classification import classifier

AGENT_PREFERENCES = {
    "Aladdin": {"likes": ["Conquest", "Reputation"], "dislikes": ["Knowledge", "Comfort"]}
}

def get_plan(agent_name):
    plan_ = []
    goal = ""
    while plan_ == []:
        goal = generate(agent_name=agent_name)
        plan_ = plan(goal, agent_name)
    return goal, plan_

def create_quest(agent_name, method="random"):
    """Creates a quest for a given agent using the specified method.

    :param agent_name: The name of the agent to generate a quest for.
    :param method: The method to use, either random or guided.
    :return: (goal, list(actions))
    """

    if method == "random":
       goal, plan_ = get_plan(agent_name)
       return goal, plan_
    if method == "preference":
        prefs = AGENT_PREFERENCES[agent_name]
        bestgoal, bestplan = None, None
        bestscore = 0.
        for i in range(15):
            goal, plan_ = get_plan(agent_name)
            scores, label = classifier(plan_)
            if label in prefs["likes"]:
                if scores[label] > bestscore:
                    bestgoal = goal
                    bestplan = plan_

        return bestgoal, bestplan


if __name__ == "__main__":
    t0 = time.time()
    goal, plan_ = create_quest("Aladdin")
    print("Goal:", goal)
    pprint(plan_)
    print("=====")
    goal, plan_ = create_quest("Aladdin", "preference")
    print("Goal (preference):", goal)
    pprint(plan_)
    print(time.time() - t0)