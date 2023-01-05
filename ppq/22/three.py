from functools import lru_cache
from math import ceil

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

poss_space = []

@lru_cache(maxsize=None)
def sum_from(n):
    global poss_space
    total = 1
    for i in poss_space[n:]:
        total *= len(i)
    
    return total

def solns(arrangement):
    # eg arrangement = [1, 0, 3, 5, 8]
    prefs = []
    parked = [False for i in arrangement]
    prefs[0] = arrangement.index(0)
    parked[prefs[0]] = True
    for i in range(1, len(arrangement)):
        pass

#@lru_cache(maxsize=None)
def a(final_arr):
    # print("Called on index", curr_car_index, "with final_arr as", final_arr, "and current parked is", _curr_parked)
    curr_parked = [False for i in final_arr]
    # if not False in curr_parked: return 0 # maybe 1
    # if end_pos == 0: return 1 # only 1 way it can want to park

    car_pref_possibilities = [[] for i in final_arr]

    for car_num in range(len(final_arr)):

        end_pos = final_arr.index(car_num)
        curr_parked[end_pos] = True
        # theres a finite number of prefs to park in this is ez

        for i in range(end_pos, -1, -1):
            if not curr_parked[i]: break
            # the car could want to park at i, and itd be valid
            # so we put i as the car and park it
            # curr_prefs[curr_car_index] = i
            car_pref_possibilities[car_num].append(i)
        
        # now we know how many possibilities this car can work on
        
        # find the next set for the next car

    return car_pref_possibilities

def extract_possibility_from_posss(final_arr, target_index):
    possibilities = a(final_arr)
    global poss_space
    poss_space = possibilities

    # lets say its [[1], [2, 1], [0], [3, 2, 1, 0]]

    # we find there are sum_from(0) possibilities initially

    # refinement search?
    choices = []
    current = target_index
    for i in range(len(possibilities)):
        possibs = sum_from(i + 1)
        # lowest multiple higher than target i think or something
        something = ceil(current / possibs)
        # we need the somethingth-minus-one-th-index
        something -= 1
        choices.append(possibilities[i][-1 - something])
        # find the diff i think
        current -= possibs * something # is how many we've cut off
        if current < 0: print("Gone Wrong")
    
    return choices


def main():
    s, target = input().strip().split(" ")
    target = int(target)
    s = list(s)
    s = [alpha.index(i) for i in s]
    # print(s, target)

    for i in extract_possibility_from_posss(s, target):
        print(alpha[i].upper(), end="")
    print()

if __name__ == "__main__":
    main()