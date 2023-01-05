from string import ascii_uppercase

# offset = 0
first_dial = ascii_uppercase

second_dial = []
second_stack = list(ascii_uppercase)

def gen_sec_dial(n):
    pos = -1
    while len(second_stack) != 0:
        pos += n
        pos = pos % len(second_stack)
        second_dial.append(second_stack[pos])
        del second_stack[pos]
        pos -= 1
    
    return second_dial

def encrypt(word):
    enc = ""
    offset = 0
    for i in word:
        pos_on_first_ring = first_dial.index(i)
        pos_on_first_ring += offset
        pos_on_first_ring = pos_on_first_ring % len(second_dial)
        out = second_dial[pos_on_first_ring]
        enc += out
        offset += 1
    
    return enc

n, word = input().strip().split(" ")
n = int(n)

gen_sec_dial(n)
print("".join(second_dial[:6]))
print(encrypt(word))