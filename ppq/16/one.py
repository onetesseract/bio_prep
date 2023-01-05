class Frac:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    
    def combine(self, other):
        return Frac(self.top + other.top, self.bottom + other.bottom)

first_frac = Frac(1, 1)
before_most_recent_left = Frac(1, 0)
before_most_recent_right = Frac(0, 1)
current = first_frac

inst = input().strip()
if len(inst) == 0: 
    print("1 / 1")
    exit()
if inst[0] == "L":
    before_most_recent_left = first_frac
else:
    before_most_recent_right = first_frac

for instruction in range(len(inst)):
    # print("with l as", before_most_recent_left.top, before_most_recent_left.bottom, "and r", before_most_recent_right.top, before_most_recent_right.bottom)    
    if inst[instruction] == "L":
        before_most_recent_left = current
        current = before_most_recent_left.combine(before_most_recent_right)
        # before_most_recent_left = temp
    else:
        before_most_recent_right = current
        current = before_most_recent_left.combine(before_most_recent_right)
        # before_most_recent_right = temp
    # print("Value of", inst[:instruction + 1], inst[instruction], "is", current.top, current.bottom, "with l as", before_most_recent_left.top, before_most_recent_left.bottom, "and r", before_most_recent_right.top, before_most_recent_right.bottom)

print(current.top, "/", current.bottom)