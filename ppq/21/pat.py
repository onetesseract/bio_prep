def max_alpha_char(string):
    max = chr(0)
    for i in string:
        if ord(i) > ord(max):
            max = i
    return max

def min_alpha_char(string):
    min = chr(255)
    for i in string:
        if ord(i) < ord(min):
            min = i
    return min

def is_pat(string):
    if len(string) == 1: return True
    for i in range(len(string) - 1):
        # print("Trying", string[0:i+1], "and", string[i+1:])
        if min_alpha_char(string[0:i+1]) > max_alpha_char(string[i+1:]):
            if is_pat(string[0:i+1][::-1]) and is_pat(string[i+1:][::-1]): return True
    return False

def main():
    inpt = input().split(" ")
    p1 = inpt[0]
    p2 = inpt[1]
    if is_pat(p1):
        print("YES")
    else:
        print("NO")
    if is_pat(p2):
        print("YES")
    else:
        print("NO")
    if is_pat(p1 + p2):
        print("YES")
    else:
        print("NO")

def permute(string):
    if len(string) == 1:
        return [string]
    out = []
    for i in range(len(string)):
        remnant = string[:i] + string[i+1:]
        for j in permute(remnant):
            out.append(string[i] + j)

    return out

for i in permute("ABCD"):
    if is_pat(i):
        print(i, "ispat")


if __name__ == "__main__":
    main()
