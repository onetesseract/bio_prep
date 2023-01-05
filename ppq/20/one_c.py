roman_ns = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V": 5, "IV": 4, "I":1}

def to_roman_n(_n):
    n = _n
    out = []
    for k, v in roman_ns.items():
        while n >= v:
            n -= v
            # print(v, n)
            out.append(k)
    
    return "".join(out)
    
def look_and_say(s):
    i = 0
    out = []
    while i < len(s):
        k = 0
        while (i + k < len(s)) and s[i+k] == s[i]:
            k += 1
        # start and count
        # count needs to be romanized
        o = to_roman_n(k)
        o += s[i]
        out.append(o)

        i += k
    
    return "".join(out)

def main():
    out = set()
    for i in range(1, 4000):
        out.add(look_and_say(to_roman_n(i)))
    
    print(len(out))

if __name__ == "__main__":
    main()
