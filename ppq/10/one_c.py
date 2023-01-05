def is_anagram(s):
    ordered = sorted(s)
    possibilities = []

    for i in range(2, 10):
        q = str(int(s) * i)
        if sorted(q) == ordered:
            possibilities.append(i)
    
    return possibilities

def main():
    count = 0
    for i in range(100000, 1000000):
        if is_anagram(str(i)):
            # how to dedup digits
            s = str(i)
            valid = True
            for q in range(len(s)):
                if s[q] in s[q+ 1:]:
                    valid = False
                    break
            if valid:
                count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()