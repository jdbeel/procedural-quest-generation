

def translate_goal(goal):
    goal = goal[5:-1]
    goals = [g.replace("(", "") for g in goal.split(") (")]
    goals = [g.replace(")", "") for g in goals]
    
    return [translate_predicate(g) for g in goals]

def translate_predicate(predicate):
    predicate = predicate.split()
    if predicate[0] == "has":
        if predicate[1] == "you":
           return f"You have the {predicate[2]}."
        else:
            return f"{predicate[1]} has the {predicate[2]}."
        
    if predicate[0] == "captive":
        if predicate[1] == "you":
            return f"You have captured {predicate[2]}."
        else:
            return f"{predicate[1]} has captured {predicate[2]}."
    if predicate[0] == "used":
        return f"The {predicate[1]} has been used."
    elif predicate[0] == "sneaky":
        if predicate[1] == "you":
            return "You are sneaky."
        else:
            return f"{predicate[1]} is sneaky."
    elif predicate[0] == "experimented":
        return f"The {predicate[1]} has been experimented with."
    elif predicate[0] == "explored":
        return f"{predicate[1]} has been explored."
    elif predicate[0] == "defended":
        return f"{predicate[1]} has been defended."
    elif predicate[0] == "at":
        if predicate[1] == "you":
            return f"You are at the {predicate[2]}."
        else:
            return f"{predicate[1]} is at the {predicate[2]}."
    elif predicate[0] == "cooperative":
        if predicate[1] == "you":
            return f"{predicate[1]} are cooperative."
        else:
            return f"{predicate[1]} is cooperative."
    elif predicate[0] == "wants":
        if predicate[1] == "you":
            return f"You want the {predicate[2]}."
        else:
            return f"{predicate[1]} wants the {predicate[2]}."
    elif predicate[0] == "dead":
        if predicate[1] == "you":
            return "You are dead."
        else:
            return f"{predicate[1]} is dead."
    elif predicate[0] == "damaged":
        return f"The {predicate[1]} is damaged."
    else:
        return " ".join(predicate)

def translate_action(action):
    action = action.split()
    if action[0] == "capture":
        return f"Capture {action[2]} from the {action[3]}."
    elif action[0] == "damage":
        return f"Damage the {action[2]} at the {action[3]} using the {action[4]}."
    elif action[0] == "defend":
        if action[1][0].isupper():
            return f"Defend {action[2]} at the {action[3]}."
        else:
            return f"Defend the {action[2]} at the {action[3]}."
    elif action[0] == "escort":
        return f"Escort {action[2]} from the {action[3]} to the {action[4]}."
    elif action[0] == "exchange":
        return f"Exchange the {action[4]} for the {action[3]} with {action[2]} at the {action[5]}."
    elif action[0] == "experiment":
        return f"Experiment with the {action[2]}."
    elif action[0] == "explore":
        return f"Travel to the {action[3]} from the {action[2]} and explore it."
    elif action[0] == "getfromlocation":
        return f"Get the {action[3]} from the {action[2]}."
    elif action[0] == "giveto":
        return f"Give the {action[3]} to {action[2]} at the {action[4]}."
    elif action[0] == "move":
        return f"Move from the {action[3]} to the {action[2]}."
    elif action[0] == "kill":
        return f"Kill {action[2]} with the undamaged {action[5]} at the {action[4]} to get the {action[3]}."
    elif action[0] == "listen":
        return f"Get information by listening to {action[3]} at the {action[4]}."
    elif action[0] == "read":
        return f"Get information by reading the {action[3]} at the {action[2]}."
    elif action[0] == "repair":
        return f"Repair the {action[3]} at the {action[2]}."
    elif action[0] == "report":
        return f"Report the information to {action[2]} at the {action[4]}."
    elif action[0] == "spy":
        return f"Get information by spying on {action[2]} at the {action[3]}."
    elif action[0] == "stealth":
        return f"Stealth."
    elif action[0] == "take":
        if action[2] == "dragon":
            return f"Take the {action[2]} from the {action[2]} at the {action[4]}."
        else:
            return f"Take the {action[2]} from {action[2]} at the {action[4]}."
    elif action[0] == "use":
        return f"Use the {action[2]}."
    else:
        return " ".join(action)
    


if __name__ == "__main__":
    translate_goal("(and (has Aladdin lamp) (captive you Aladdin) (used lamp))")
