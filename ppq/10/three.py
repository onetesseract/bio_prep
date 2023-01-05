from collections import defaultdict, deque

distances = defaultdict(lambda: 9999999)

def empty(jugs, index):
    j = jugs.copy()
    j[index] = 0

    return j

def fill(jugs, index, caps):
    j = jugs.copy()
    j[index] = caps[index]

    return j

def pour_into_another(jugs, src, dst, caps):
    j = jugs.copy()
    j[dst] += j[src]
    j[src] = 0

    if j[dst] > caps[dst]:
        j[src] = j[dst] - caps[dst]
        j[dst] = caps[dst]
    
    return j

def main():
    count, target = [int(i) for i in input().strip().split(" ")]
    capacities = [int (i) for i in input().strip().split(" ")]
    # print(capacities)

    # distance, state
    to_explore = deque()
    to_explore.append([0, [0 for i in range(count)]])

    shortest = 99999999

    while len(to_explore) != 0:
        dist, state = to_explore.popleft()
        t_state = tuple(state)
        if distances[t_state] <= dist:
            # theres another equally efficient or better method been here before, not worth exploring again
            continue
        else:
            distances[t_state] = dist
        
        for jug in state:
            if jug == target:
                if dist < shortest:
                    shortest = dist
                break

        for jug_index in range(count):
            if state[jug_index] == 0:
                # only viable thing is fill
                to_explore.append([dist + 1, fill(state, jug_index, capacities)])
            else:
                to_explore.append([dist + 1, empty(state, jug_index)])

                if state[jug_index] != capacities[jug_index]:
                    to_explore.append([dist + 1, fill(state, jug_index, capacities)])

                for potential_target in range(count):
                    if potential_target == jug_index or state[potential_target] == capacities[potential_target]: continue # jug is at cap
                    to_explore.append([dist + 1, pour_into_another(state, jug_index, potential_target, capacities)])
    
    return shortest

if __name__ == "__main__":
    print(main())