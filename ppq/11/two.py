from copy import deepcopy
from collections import deque

class Card:
    def __init__(self, s):
        self.num = None
        if s[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]: 
            self.num = int(s[0])
        else:
            if s[0] == "A": self.num = 1
            if s[0] == "T": self.num = 10
            if s[0] == "J": self.num = 11
            if s[0] == "Q": self.num = 12
            if s[0] == "K": self.num = 13
        if self.num == None:
            print("no", s)      
        self.suit = s[1]
    
    def can_match(self, card):
        return card.num == self.num or card.suit == self.suit
    
    def render(self):
        s = ""
        if self.num > 1 and self.num < 10:
            s = str(self.num)
        else:
            if self.num == 1:
                s = "A"
            if self.num == 10: s = "T"
            if self.num == 11: s = "J"
            if self.num == 12: s = "Q"
            if self.num == 13: s = "K"
        s += self.suit

        return s

class Board:
    # piles = [[card, height]]
    piles = []

    def __init__(self, deck):
        for i in deck:
            self.piles.append([i, 1])

    def move_p1_onto_p2(self, p1, p2):
        _piles = deepcopy(self.piles)
        _, p2height = _piles[p2]
        top, p1height = _piles[p1]
        _piles[p2] = [top, p1height + p2height]
        del _piles[p1]
        return _piles

    def enumerate_moves(self, pile_index):
        if pile_index == 0: return ([], [])
        out = []
        targets = []
        if pile_index > 0:
            # print(pile_index, len(self.piles))
            if self.piles[pile_index - 1][0].can_match(self.piles[pile_index][0]):
                out.append(self.move_p1_onto_p2(pile_index, pile_index - 1))
                targets.append(pile_index - 1)
        if pile_index > 2:
            if self.piles[pile_index - 3][0].can_match(self.piles[pile_index][0]):
                out.append(self.move_p1_onto_p2(pile_index, pile_index - 3))
                targets.append(pile_index - 3)
        return (out, targets)
    
    def play_strat_1(self):
        for i in range(len(self.piles) - 1, -1, -1):
            moves, _ = self.enumerate_moves(i)
            if len(moves) != 0:
                # print("Made move:", moves[0])
                self.piles = moves[0]
                return True
        return False

    def find_max_height(self, _piles):
        max = -1
        for i in range(len(_piles)):
            _, height = _piles[i]
            if height > max:
                max = height
        return max
    
    def play_strat_2(self):
        max_height = -1
        out_piles = []
        for i in range(len(self.piles)):
            piles, targets = self.enumerate_moves(i)
            # print(piles)
            for i in range(len(piles) - 1, -1 -1):
                max_pile = self.find_max_height(piles[i])
                print("MAX:", max_pile)
                if max_pile >= max_height:
                    out_piles = piles
                    max_height = max_pile
        
        self.piles = out_piles
        print("s2", out_piles)
        return out_piles

    def count_moves(self, _piles):
        moves = 0
        b = Board([])
        b.piles = _piles
        for i in range(len(_piles)):
            out, targ = b.enumerate_moves(i)
            moves += len(out)
        return moves

    def play_strat_3(self):
        max_moves = -1
        out_piles = []
        for i in range(len(self.piles)):
            piles, targets = self.enumerate_moves(i)
            for i in range(len(piles) - 1, -1 -1):
                max_move = self.count_moves(piles[i])
                if max_move >= max_moves:
                    out_piles = piles
                    max_moves = max_move
        
        self.piles = out_piles
        return out_piles
    
    def is_gameover(self):
        return len(self.piles) == 1 or self.count_moves(self.piles) == 0

def original_stack():
    stack = []
    for suit in ["C", "H", "S", "D"]:
        for num in list("A23456789TJQK"):
            stack.append(Card((num + suit)))
    
    return stack

def shuffle(shuffling_numbers):
    stack = deque(original_stack())
    deck = []
    while len(stack) != 0:
        for i in shuffling_numbers:
            if len(stack) == 0:
                break
            for _ in range(i - 1):
                stack.append(stack.popleft())
            deck.append(stack.popleft())
    
    return deck

def main():
    shuffling_numbers = [int(i) for i in input().strip().split(" ")]
    deck = shuffle(shuffling_numbers)
    board = Board(deepcopy(deck))
    
    print(board.piles[0][0].render(), board.piles[-1][0].render())

    # strat 1
    while not board.is_gameover():
        board.play_strat_1()
        # print("Made a move")
    print(len(board.piles), board.piles[0][0].render())

    board = Board(deepcopy(deck))
    # strat 2
    while not board.is_gameover():
        board.play_strat_2()
        # print("Made a move")
    print(len(board.piles)) # , board.piles[0][0].render())

    board = Board(deepcopy(deck))
    # strat 3
    while not board.is_gameover():
        board.play_strat_3()
        # print("Made a move")
    print(len(board.piles), board.piles[0][0].render())

if __name__ == "__main__":
    main()