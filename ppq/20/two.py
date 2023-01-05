from string import ascii_uppercase

def st_tuple(t):
    k, v = t
    return k

class Room:
    def __init__(self, _name):
        self.exits = dict()
        self.counter = 0
        self.name = _name
        if len(_name) != 1:
            print("Broken")
    
    def link_to(self, other):
        # print(self, other)
        other.exits[self] = 0
        self.exits[other] = 0
        self.exits = {k:v for k, v in sorted(self.exits.items(), key=lambda q: st_tuple(q).name)}
        other.exits = {k:v for k, v in sorted(other.exits.items(), key=lambda q: st_tuple(q).name)}
    
    def __repr__(self):
        return f"Room: (name: {self.name}, exits: {self.exits})"
    
def build_graph(plan, r):
    rooms = {}
    chosen = []
    count = -1
    for i in plan:
        count += 1
        room = ''
        for j in ascii_uppercase[:r]:
            if j not in plan[count:] and j not in chosen:
                # j is the room
                room = j
                chosen.append(j)
                break
        
        if room == '':
            print("much brok")
        
        if j not in rooms.keys():
            rooms[j] = Room(j)
        
        if i not in rooms.keys():
            rooms[i] = Room(i)
        
        rooms[j].link_to(rooms[i])
    
    # two rooms havent been chosen
    unchosen = []
    for i in ascii_uppercase[:r]:
        if i not in chosen:
            unchosen.append(i)
        
    if len(unchosen) != 2:
        print("Borkend")
    
    if unchosen[0] not in rooms.keys():
        rooms[unchosen[0]] = Room(unchosen[0])
    
    if unchosen[1] not in rooms.keys():
        rooms[unchosen[1]] = Room(unchosen[1])
    
    # link the two last

    rooms[unchosen[0]].link_to(rooms[unchosen[1]])
    
    return rooms

def move(graph, pos):
    current_room = graph[pos]
    if current_room.counter % 2 == 1:
        # odd count
        #for (k, v) in current_room.exits.items():
        #    if v % 2 == 1:
        
        #        new_pos = list()
        new_pos = list(current_room.exits.keys())[0].name
    
    else:
        # even count
        out = None
        use_next = False
        for (k, v) in current_room.exits.items():
            if v % 2 == 1:
                if k == list(current_room.exits.keys())[-1]: # last one
                    out = k.name
                    break
                else:
                    use_next == True
                
                if use_next:# use this one
                    out = k.name
                    break
        if out == None:
            out = list(current_room.exits.keys())[0].name
        
        new_pos = out
    
    graph[new_pos].counter += 1
    
    return new_pos
    
def main():
    plan, p, q = input().strip().split(" ")
    p, q = int(p), int(q)

    _graph = build_graph(plan, len(plan) + 2)

    graph = {k:_graph[k] for k in sorted(_graph.keys())}

    for (k, v) in graph.items():
        print("".join([room.name for room in v.exits]))
    
    # we visit A once
    graph["A"].counter = 1

    pos = "A"

    for i in range(p):
        pos = move(graph, pos)
    
    print(pos, end="")

    for i in range(q - p):
        pos = move(graph, pos)
    print(pos)

if __name__ == "__main__":
    main()