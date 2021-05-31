import numpy as np
from utils import add_sets, extract_stg1_cases_counter
from collections import Counter
from scipy.optimize import minimize

def calculate_loss_combinations(slot, air_state=1):
    """
    Calculates the possible plane loss for a given slot
    """
    res = []
    sweep = range(air_state + 1)
    for a in sweep:
        for b in sweep:
            res.append(int(slot * (0.035 * a + 0.065 * b)))

    return Counter(res)

def calculate_ship_combinations(slot_sizes, air_state=1):
    c = Counter()
    for slot in slot_sizes:
        possibiltiies = calculate_loss_combinations(slot)
        c = sum_possibilities(c, possibiltiies)

    return c

def calculate_fleet_combinations(fleet, air_state=1):
    c =  Counter()
    for ship in fleet:
        possibiltiies = calculate_ship_combinations(ship)
        c = sum_possibilities(c, possibiltiies)

    return c

def sum_possibilities(c1, c2):
    c = Counter()
    if len(c1) == 0:
        return c2
    if len(c2) == 0:
        return c1
    for key, value in c1.items():
        for key2, value2 in c2.items():
            loss = key + key2
            val = value * value2
            c.update({loss: val})
    return c

def calc_expectation(c):
    num = 0
    denom = sum(c.values())
    for key, value in c.items():
        num += key * value / denom
    return num

def obj(x, *args):
    guess = calculate_ship_combinations(x)
    existing = args[0]
    expc_actual = args[1]
    c = sum_possibilities(guess, existing)
    expc_estimate = calc_expectation(c)
    return abs(expc_estimate - expc_actual)

if __name__ == "__main__":
    guess = [24, 24, 24, 24]
    airstrike = [12, 12, 8, 4]
    existing = calculate_fleet_combinations([])
    real = extract_stg1_cases_counter("./data/1682,1650,1650.json")
    expc_real = calc_expectation(real)
    
    res = minimize(obj, guess, args=(existing, expc_real), method='COBYLA', options={'rhobeg': 1.0,})
    print(res)
    
