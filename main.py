import numpy as np
from utils import add_sets
import copy

def calculate_loss_combinations(slot, air_state=1):
    """
    Calculates the possible plane loss for a given slot
    """
    res = set()
    sweep = range(air_state + 1)
    for a in sweep:
        for b in sweep:
            res.add(int(slot * (0.035 * a + 0.065 * b)))

    return res

def calculate_total_combinations(array):
    res = set([0])
    for comb in array:
        res = add_sets(res, comb)
    return res

def calculate_ship_combinations(slot_sizes, air_state=1):
    array = [calculate_loss_combinations(slot, air_state) for slot in slot_sizes]
    return calculate_total_combinations(array)

def objective(guess, existing_combinations, actual, air_state=1):
    guess_loss = calculate_ship_combinations(guess, air_state)
    print(guess_loss)
    estimate = add_sets(guess_loss, existing_combinations)
    if estimate == actual:
        return True
    else:
        return False

if __name__ == "__main__":
    enemycomp = []
    target_id = 1501
    total_planes = 96
    num_slots = 4
    num_enemies = 1
    air_state = 1

    actual = set([0, 1, 2, 3, 4, 5, 6, 7, 8])
    slot_sizes = [12, 12, 8, 4]
    #fleet = [slot_sizes, slot_sizes]
    fleet = []
    print(calculate_ship_combinations(slot_sizes))
    existing_combinations = calculate_total_combinations([calculate_ship_combinations(ship) for ship in fleet])
    res = []

    def slotter(array, rem, idx):
        array = copy.copy(array)
        if rem == 0:
            res.append(array)
            return
        if idx == len(array) - 1:
            array[idx] = rem
            res.append(array)
            return
        for rem_slot in reversed(range(1, rem + 1)):
            array[idx] = rem_slot
            slotter(array, rem - rem_slot, idx + 1)

    guess = np.zeros(num_slots)
    #slotter(guess, total_planes, 0)
    print(objective([24, 24, 24, 24], existing_combinations, actual))
    ''' objective_lambda = lambda x: objective(x, existing_combinations, actual, air_state)
    result = filter(objective_lambda, res)
    print(result) '''

    

    


