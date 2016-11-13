from sklearn.ensemble import RandomForestClassifier as rfc
from json import load
import pickle
from text_analysis import text_vector
import math

PARAMS = load(open('config.json', 'r'))

def change_h(p):
    
    maxThresh_pos = 0.20
    minThresh_pos = 0.07
    
    maxThresh_neg = -0.07
    minThresh_neg = -0.20
    
    delH = ((-1)**(1+(-p['d']))) * (math.tan((0.1*p['hostility']*p['count'])) * ((((p['agree']+p['timid'])/2)+p['anger']))/2)
    
    if delH > maxThresh_pos:
        delH = maxThresh_pos
    elif delH < minThresh_pos and p['d'] == 1:
        delH = minThresh_pos
    elif delH > maxThresh_neg and p['d'] == 0:
        delH = maxThresh_neg
    elif delH < minThresh_neg:
        delH = minThresh_neg
    else:
        pass
    
    p['hostility'] += delH
    del p['d']
    del p['sentence']
    return p

def build_training_set():
    data = eval(open(PARAMS['talk_dataset'], 'r').read())
    X = []
    y = []
    for ex in data:
        x = []
        for key in PARAMS['feature_order']:
            x += [ex[key]]
        x += text_vector(ex['sentence'])
        X += [x]
        y += [ex['choice']]
    return X, y

def train_and_save():
    X, y = build_training_set()
    clf = rfc(n_estimators=100)
    clf.fit(X, y)
    pickle.dump(clf, open(PARAMS['talk_model'], 'wb'))
    
def main(p):
    x = [[]]
    for key in PARAMS['feature_order']:
        x[0] += [p[key]]
    x[0] += text_vector(p['sentence'])
    clf = pickle.load(open(PARAMS['talk_model'], 'rb'))
    p['d'] = clf.predict(x)[0]
    return change_h(p)