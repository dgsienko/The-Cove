import bot_manager
import run_decider
import talk_decider
import fight_decider
import trade_decider
from json import load, dumps
from flask import Flask, request

app = Flask(__name__)

PARAMS = load(open('config.json', 'r'))

@app.route('/new_bot', methods=['GET'])
def new_bot():
    bot_manager.generate_bot()
    p = bot_manager.load_bot()
    return dumps(dict(call='new_bot',
                      hostility=p['hostility'],
                      mult=0))
    
@app.route('/begin_interact', methods=['GET'])
def begin_interact():
    p = bot_manager.load_bot()
    p['count'] += 1
    bot_manager.save_bot(p)
    mult = ((p['anger']+p['hostility'])/2)
    return dumps(dict(call='begin_interact',
                      mult=mult,
                      hostility=p['hostility']))

@app.route('/run_interact', methods=['GET'])
def run_interact():
    p = bot_manager.load_bot()
    action, h_delta = run_decider.main(p)
    p['hostility'] += h_delta
    bot_manager.save_bot(p)
    mult = 0
    if action == 'fight':
        mult = ((p['anger']+p['hostility'])/2)
    return dumps(dict(call='run_interact',
                      action=action, 
                      mult=mult, 
                      hostility=p['hostility']))

@app.route('/talk_interact', methods=['GET', 'POST'])
def talk_interact():
    sentence = request.json['sentence']
    p = bot_manager.load_bot()
    p['sentence'] = sentence
    p_new = talk_decider.main(p)
    bot_manager.save_bot(p_new)
    action, mult = fight_decider.action(p)
    return dumps(dict(call='talk_interact',
                      action=action, 
                      mult=mult, 
                      hostility=p['hostility']))

@app.route('/fight_interact', methods=['GET'])
def fight_interact():
    p = bot_manager.load_bot()
    action, mult = 'run', ((p['anger']+p['hostility'])/2)
    if mult > PARAMS['avg_fight']:
        action = 'fight'
    else:
        p['hostility'] = 1
        bot_manager.save_bot(p)
    return dumps(dict(call='fight_interact',
                      action=action,
                      mult=mult, 
                      hostility=p['hostility']))

@app.route('/trade_interact', methods=['GET'])
def trade_interact():
    p = bot_manager.load_bot()
    action, p_new = trade_decider.trade(p)
    mult = 0
    bot_manager.save_bot(p_new)
    if action == 'fight':
        mult = ((p['anger']+p['hostility'])/2)
    return dumps(dict(action=action,
                      mult=mult, 
                      hostility=p['hostility']))
    
app.run(host='0.0.0.0')