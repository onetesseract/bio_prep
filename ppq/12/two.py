class Point:
    def __init__(self, is_flip, in_l, in_r, out):
        self.is_lazy = not is_flip
        self.in_l = in_l
        self.in_r = in_r
        self.out = out
        self.point = in_l
    
    def receive_train(self, src):
        if self.is_lazy:
            if src != self.out:
                # we need flip point
                self.point = src
                return self.out
            else:
                return self.point
        else:
            if src == self.out:
                # send it, then flip it
                output = self.point
                if self.point == self.in_l: self.point = self.in_r
                else: self.point = self.in_l

                return output
            else:
                return self.out

# oh, pain
def init_network(flips):
    net = {}
    net['A'] = Point('A' in flips, 'E', 'F', 'D')
    net['B'] = Point('B' in flips, 'G', 'H', 'C')
    net['C'] = Point('C' in flips, 'I', 'J', 'B')
    net['D'] = Point('D' in flips, 'K', 'L', 'A')
    net['E'] = Point('E' in flips, 'M', 'N', 'A')
    net['F'] = Point('F' in flips, 'N', 'O', 'A')
    net['G'] = Point('G' in flips, 'O', 'P', 'B')
    net['H'] = Point('H' in flips, 'P', 'Q', 'B')
    net['I'] = Point('I' in flips, 'Q', 'R', 'C')
    net['J'] = Point('J' in flips, 'R', 'S', 'C')
    net['K'] = Point('K' in flips, 'S', 'T', 'D')
    net['L'] = Point('L' in flips, 'T', 'M', 'D')
    net['M'] = Point('M' in flips, 'L', 'E', 'U')
    net['N'] = Point('N' in flips, 'E', 'F', 'U')
    net['O'] = Point('O' in flips, 'F', 'G', 'V')
    net['P'] = Point('P' in flips, 'G', 'H', 'V')
    net['Q'] = Point('Q' in flips, 'H', 'I', 'W')
    net['R'] = Point('R' in flips, 'I', 'J', 'W')
    net['S'] = Point('S' in flips, 'J', 'K', 'X')
    net['T'] = Point('T' in flips, 'K', 'L', 'X')
    net['U'] = Point('U' in flips, 'M', 'N', 'V')
    net['V'] = Point('V' in flips, 'O', 'P', 'U')
    net['W'] = Point('W' in flips, 'Q', 'R', 'X')
    net['X'] = Point('X' in flips, 'S', 'T', 'W')

    return net

def run(train_pos, next_point, net, i):
    for q in range(i):
        old_next = next_point
        point = net[next_point]
        next_point = point.receive_train(train_pos)
        # print("Train at", train_pos, "has travelled through", old_next, "and is now going to", next_point)
        train_pos = old_next
    
    return train_pos + next_point

def main():
    flips = input().strip()
    train_pos, next_point = [i for i in input().strip()]
    n = int(input().strip())
    print(run(train_pos, next_point, init_network(flips), n))
    

    
# VUMLDAEMUVP

"""
Since the network is cyclic, that is any train at the bottom will take four moves
to get up since the u-v-w-x row will always go to one of the
mno.. row which will go to efgh.. and then to abcd...
After one point, it'll be on the bottom row. after two back on the second bottom
set of links, the third the middle, fourth the second top, and fifth the top.
since 1,000,000,000,000,000,000 is divisible by 8, it'll always be able
to make a full cycle of the network,
so will end up somewhere on the PtoV set of links:
i.e it'll be at m-u, n-u, o-v, p-v, q-w. r-w, s-x, or t-x

"""




main()
    

    

