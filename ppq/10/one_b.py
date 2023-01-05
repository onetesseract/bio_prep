def is_anagram(s):
    ordered = sorted(s)
    possibilities = []

    for i in range(2, 10):
        q = str(int(s) * i)
        if sorted(q) == ordered:
            possibilities.append(i)
    
    return possibilities

def main():
    num = 85247910
    for i in range(2, 10):
        if int(num) % i == 0:
            if is_anagram(str(int(num / i))):
                print(num / i)

    
if __name__ == "__main__":
    main()