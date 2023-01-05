from math import floor, ceil

def create_matching_half(fh):
    s = []
    for i in range(len(fh) - 1, -1, -1):
        s.append(str(10 - int(fh[i])))
    return "".join(s)

def create_from_first_half_only(fh):
    return fh + create_matching_half(fh)



def next_greatest_ud_num(base, add):
    if len(base) %2 == 0:
        # even digits
        # TODO: special case for thingy whatsit
        _first_half = base[:int(len(base)/2)]
        # print("First for", base, "is", _first_half)
        first_half = str(int(_first_half) + add)
        if first_half[-1] == "0":
            first_half = str(int(first_half) + 1)
        if len(first_half) != len(_first_half):
            # overflow
            #prin
            return first_half[:-1] + "5" + create_matching_half(first_half[:-1])
        return create_from_first_half_only(first_half)
    else:
        if len(base) == 1: return "19" # 5
        # odd digits
        _first_half = int(base[:floor(len(base)/2)]) if base[:floor(len(base)/2)] != "" else 0
        first_half = _first_half + 1
        if len(str(first_half)) != len(str(_first_half)):
            # oh no
            full = str(first_half + 1) + ("0" * len(str(first_half)))
            #print("FULL", full)
            return next_greatest_ud_num(full, 0)
        return str(first_half) + "5" + create_matching_half(str(first_half))
        # fh = str(first_half) + "0" * len(str(first_half - 1))
        # print("Catching", fh, "for", base)
        # return next_greatest_ud_num(fh, 0)
        inbetween = base[floor(len(base)/2)]
        _fh_plus_inb = first_half + inbetween
        fh_plus_inb = str(int(_fh_plus_inb) + 10)
        # overflow cant happen, five in middle always, so we need to +1 to the 10s col
        return fh_plus_inb + create_matching_half(fh_plus_inb[:-2])

def iter_until(count):
    last = "5"
    for i in range(count - 1):
        last = next_greatest_ud_num(last, 1)
        # print(last)
    return last

def main():
    print(iter_until(int(input().strip())))

if __name__ == "__main__":
    main()