def action(p):
    if p['hostility'] < p['low_thresh']:
        return 'run', 0
    elif p['hostility'] < p['high_thresh']:
        return 'no action', 0
    else:
        mult = ((p['anger'] + p['hostility'])/2)
        return 'fight', mult