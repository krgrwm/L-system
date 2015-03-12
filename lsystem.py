from itertools import chain

def flatten(l):
    return list(chain.from_iterable(l))

def apply_rule(l, rule):
    return [rule.get(i, i) for i in l]

def _step(l, rule):
    return flatten(apply_rule(l, rule))

def step(model, n):
    for i in range(n):
        model.l = _step(model.l, model.rule)
