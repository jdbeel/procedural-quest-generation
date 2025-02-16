import os
import re
import shutil
import subprocess
from typing import Iterable

PPDL_DIR = "../ppdl"
PLANNER_DIR = "../fast-downward"


def plan(goal: str, agent_name: str) -> Iterable[str]:
    """Plans given a goal and an agent name, using the
    domain and initial state files present in `./ppdl`.

    This uses subprocess to call `fast-downward`, which needs
    to be built before it can be used. Follow these instructions:

    `cd ./fast-downward`
    `./build.py`.

    :param goal: The goal (as generated by randGoal or supplied).
    :param agent_name: The name of the agent to use.
    :returns: The plan in the form of a list of actions in PPDL format.
    """

    # Clear out the temp directory before populating it
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    # Recreate the temporary directory
    os.mkdir("temp")

    # Switch to the temporary directory to avoid extra content in strings
    # Then replace the "replace-with-" markers in the initial_state.ppdl
    os.chdir("temp")
    with open(PPDL_DIR + "/initial_state.ppdl", "r") as f:
        ppdl_str = f.read()

    ppdl_str = ppdl_str.replace("replace-with-agent", agent_name)
    ppdl_str = ppdl_str.replace("replace-with-goal", goal)

    with open("initial_state.ppdl", "w") as f:
        f.write(ppdl_str)

    # Run the planner
    with open(agent_name + ".soln", "w") as solution:
        calc = subprocess.call(
            [
                PLANNER_DIR +
                "/fast-downward.py",
                PPDL_DIR +
                "/domain.ppdl",
                "initial_state.ppdl",
                "--search",
                "astar(ipdb())"],
            stdout=solution)

    # Using a regex, pull the solution out of the output file
    soln_regex = r"([a-z ]+) \(\d\)$"
    soln = []
    with open(agent_name + ".soln", "r") as solution:
        for line in solution:
            if re.match(soln_regex, line.rstrip()):
                soln.append(line.rstrip())

    # Cleanup
    os.chdir("..")
    shutil.rmtree("temp")
    return soln


if __name__ == "__main__":
    print(
        plan(
            "(and (has Aladdin lamp) (captive you Aladdin) (used lamp))",
            "Aladdin"))
