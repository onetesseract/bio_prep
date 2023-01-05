def match_to_list(lst, s):
    q = 0
    for i in s:
        if i == lst[q]:
            q += 1
        if q == len(lst):
            return True
    
    return False

def main():
    digits = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}
    s = input()
    for i in digits:
        if match_to_list(list(i), s):
            print(digits[i])
            exit(0)
    
    print("NO")

if __name__ == "__main__":
    main()