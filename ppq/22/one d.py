alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(s):
    out = []
    out.append(s[0])
    for i in range(1, len(s)):
        out.append(alpha[(alpha.index(s[i]) - alpha.index(s[i - 1])) % 26])
    
    return "".join(out)

def encrypt(s):
    out = []
    out.append(s[0])
    for i in range(1, len(s)):
        out.append((s[i] + out[-1]) % 26)
    
    return out

def main():
    print(encrypt(input().strip()))

def find_lowest_loop(s):
    count = 1
    q = encrypt(s)
    while q != s:
        q = encrypt(q)
        count += 1
        print("count", count)
    return count

def for_every_3_letter_s():
    s = [1, 1, 1]
    count = 0
    while s[0] != 27:

        print(s)

        loop = find_lowest_loop(s)

        print(loop)

        if 999999999999 % loop == 0:
            count += 1

        # do some testing
        s[2] += 1
        if s[2] > 26:
            s[2] = 1
            s[1] += 1
            if s[1] > 26:
                s[0] += 1
                s[1] = 1

    return count
if __name__ == "__main__":
    
    print(for_every_3_letter_s())