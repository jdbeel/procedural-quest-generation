# procedural-quest-generation
This is a working demo for our Game AI project, which aims to perform procedural quest generation. 

## Build

Before running the code, `fast-downward` must be built. Change to the `fast-downward` directory and run `./build.py`.

## Running the Code

### main.py
Ties the entire workflow together. Use the `create_quest` function to create a quest, which will be returned in PPDL.

### planning.py 
Given a goal, which is one or more predicates joined with an AND, and an agent name,
use fast-downward to plan a quest for a given agent.

### classification.py
Given a plan, which is a sequence of actions, we will classify the sequence into respective motivation category based on highest score. There are 9 motivations, which are "Knowledge",
"Comfort", "Reputation", "Serenity", "Protection", "Conquest", "Wealth", "Ability", and "Equipment".  

### generation.py
Generates goals for other parts of the workflow. `generate` takes a random seed and an agent name and returns the goal string, the AND of several predicates.

### server.py
Can be run using Flask. This is done by setting the `FLASK_APP` environment variable to point to `server.py` and then doing `flask run`.

## translate.py
Translates quests from PPDL to natural(ish) English.