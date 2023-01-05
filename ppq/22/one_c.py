alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(s):
    out = []
    out.append(s[0])
    for i in range(1, len(s)):
        out.append(alpha[(alpha.index(s[i]) - alpha.index(s[i - 1])) % 26])
    
    return "".join(out)

def main():
    s = "OLYMPIAD"
    q = decrypt(s)
    count = 1
    while q != s:
        q = decrypt(q)
        count += 1
    
    print(count)

if __name__ == "__main__":
    main()