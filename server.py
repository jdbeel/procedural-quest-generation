from flask import Flask, request, redirect
from flask import render_template
from main import create_quest

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
    return render_template('index.html', goal=goal, plan=plan)
