alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(s):
    out = []
    out.append(s[0])
    for i in range(1, len(s)):
        out.append(alpha[(alpha.index(s[i]) - alpha.index(s[i - 1])) % 26])
    
    return "".join(out)

def main():
    print(decrypt(input().strip()))

if __name__ == "__main__":
    main()