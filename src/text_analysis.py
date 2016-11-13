import indicoio
from json import load

PARAMS = load(open('config.json', 'r'))

indicoio.config.api_key = PARAMS['indico_api_key']

def text_vector(s):
    return indicoio.text_features(s)