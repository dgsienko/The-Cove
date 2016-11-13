from random import random
from json import load
from talk_decider import change_h

PARAMS = load(open('config.json', 'r'))

def trade(p):
    probs = PARAMS['trade_probs']
    rv = random()
    if rv < probs[0]:
        return 'win', p
    elif rv < probs[1]:
        p['sentence'] = 'N/A'
        p['d'] = 0
        new_p = change_h(p)
        return 'success', new_p
    elif rv < probs[2]:
        return 'run', p
    else:
        p['sentence'] = 'N/A'
        p['d'] = 1
        new_p = change_h(p)
        return 'fight', new_p