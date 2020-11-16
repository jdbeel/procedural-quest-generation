from pprint import pprint

from generation import generate
from planning import plan

def create_quest(agent_name, method="random"):
    """Creates a quest for a given agent using the specified method.

    :param agent_name: The name of the agent to generate a quest for.
    :param method: The method to use, either random or guided.
    :return: (goal, list(actions))
    """

    if method == "random":
        goal = generate()
        plan_ = plan(goal, agent_name)
        return goal, plan_

if __name__ == "__main__":
    goal, plan_ = create_quest("Aladdin")
    print("Goal:", goal)
    pprint(plan_)