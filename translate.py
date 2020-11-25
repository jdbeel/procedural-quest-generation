

def translate_goal(goal):
    goal = goal[5:-1]
    goals = [g.replace("(", "") for g in goal.split(") (")]
    goals = [g.replace(")", "") for g in goals]
    
    return [translate_predicate(g) for g in goals]

def translate_predicate(predicate):
    predicate = predicate.split()
    if predicate[0] == "has":
        return f"{predicate[1]} has the {predicate[2]}."
    if predicate[0] == "captive":
        if predicate[1] == "you":
            return f"You have captured {predicate[2]}."
        else:
            return f"{predicate[1]} has captured {predicate[2]}."
    if predicate[0] == "used":
        return f"The {predicate[1]} has been used."
    elif predicate[0] == "sneaky":
        return f"{predicate[1]} is sneaky."
    elif predicate[0] == "experimented":
        return f"The {predicate[1]} has been experimented with."
    elif predicate[0] == "explored":
        return f"{predicate[1]} has been explored."
    elif predicate[0] == "defended":
        return f"{predicate[1]} has been defended."
    elif predicate[0] == "at":
        return f"{predicate[1]} is at the {predicate[2]}."
    elif predicate[0] == "cooperative":
        return f"{predicate[1]} is cooperative."
    elif predicate[0] == "wants":
        return f"{predicate[1]} wants the {predicate[2]}"
    elif predicate[0] == "dead":
        return f"{predicate[1]} is dead."
    elif predicate[0] == "damaged":
        return f"The {predicate[1]} is damaged."
    else:
        return " ".join(predicate)

def translate_action(action):
    


if __name__ == "__main__":
    translate_goal("(and (has Aladdin lamp) (captive you Aladdin) (used lamp))")
