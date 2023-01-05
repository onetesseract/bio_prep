def is_anagram(s):
    ordered = sorted(s)
    possibilities = []

    for i in range(2, 10):
        q = str(int(s) * i)
        if sorted(q) == ordered:
            possibilities.append(i)
    
    return possibilities

def main():
    num = input().strip()
    out = is_anagram(num)

    if len(out) == 0:
        print("NO")
    else:
        for i in out:
            print(i, end=" ")
        print()
    
if __name__ == "__main__":
    main()