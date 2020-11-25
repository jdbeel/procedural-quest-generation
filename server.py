from flask import Flask, request, redirect
from flask import render_template
from main import create_quest
from translate import translate_goal, translate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genQuest', methods=['POST'])
def genQuest():
    f = request.form
    agent_name = f['agentName']
    preferences = [key for key in f.keys() if key != 'agentName']
    preferences = {"likes": preferences}
    goal, plan = create_quest(agent_name, method="preference", preferences=preferences)
    goal = translate_goal(goal)
    plan = [translate(p[:-4]) for p in plan]
    return render_template('index.html', goal=goal, plan=plan)
