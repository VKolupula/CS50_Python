def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def case1(s):
    case1 = s[0:1].isalpha()
    return case1

def case2(s):
    if 2 <= len(s) <= 6:
        case2 = True
    else:
        case2 = False
    return case2

def case3(s):

    nlist1 = []
    for i in reversed(range(len(s))):

        if s[i].isdecimal():
            nlist1.append(i)
    if len(nlist1)>0:
        if ((nlist1[0])-(nlist1[1])<=1) and ((nlist1[1])-(nlist1[1])<=2):
            seq = True
        else:
            seq = False

    if sorted(nlist1) != nlist1 and len(s)-1 in nlist1 and int(s[nlist1[-1]]) > 0 and seq==True:
        case3 = True
    elif int(len(nlist1)) == 0:
        case3 = True
    else:
        case3 = False

    return case3

def case4(s):
    if s.isalnum():
        case4 = True
    else:
        case4 = False
    return case4


def is_valid(s):
    if case1(s) and case2(s) and case3(s) and case4(s):
        return True
    else:
        return False



main()