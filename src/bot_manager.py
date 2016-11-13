from random import random, choice
from json import load

PARAMS = load(open('config.json', 'r'))

def generate_bot(show=False):
    timid, agree, hostile = random(), random(), None
    r1, r2 = PARAMS['anger_delta_min'], PARAMS['anger_delta_max']
    anger = (1-timid) + choice([x*.01 for x in range(r1,r2+1) if \
                                0 < (1-timid + x*.01) < 1])
    if agree < anger:
        hostile = min(PARAMS['hostility_max'], anger + anger*.1)
    else:
        hostile = max(PARAMS['hostility_min'], anger - anger*.1)
    p = dict(timid=timid,
             anger=anger,
             agree=agree,
             hostility=hostile,
             count=0)
    p['low_thresh'] = p['hostility']*((p['anger']+p['timid']+p['agree'])/3)
    p['high_thresh'] = 1 - p['low_thresh']
    save_bot(p)
    if show:
        return p
    
def save_bot(p):
    for key in p:
        p[key] = float('%.2f' % p[key])
    open(PARAMS['bot_file'], 'w').write(str(p))
    
def load_bot():
    p = eval(open(PARAMS['bot_file'], 'r').read())
    p['hostility'] = min(.99, p['hostility'])
    return p