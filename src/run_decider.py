from sklearn.ensemble import RandomForestClassifier as rfc
from json import load
import pickle

PARAMS = load(open('config.json', 'r'))

def build_training_set():
    data = eval(open(PARAMS['run_dataset'], 'r').read())
    X = []
    y = []
    for ex in data:
        x = []
        for key in PARAMS['feature_order']:
            x += [ex[key]]
        X += [x]
        y += [ex['choice']]
    return X, y

def train_and_save():
    X, y = build_training_set()
    clf = rfc()
    clf.fit(X, y)
    pickle.dump(clf, open(PARAMS['run_model'], 'wb'))
    
def classify(p):
    x = [[]]
    for key in PARAMS['feature_order']:
        x[0] += [p[key]]
    clf = pickle.load(open(PARAMS['run_model'], 'rb'))
    return clf.predict(x)[0]

def main(p):
    decision = classify(p)
    if decision == 1:
        h_delta = ((p['count']-1)/p['count'])*(0.1*p['anger'])+(((p['agree']+p['timid'])/2)*0.1)
        return 'fight', h_delta
    else:
        return 'end event', 0