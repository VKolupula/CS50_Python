def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    try:
        #case_1
        if s[0:1].isalpha():
            case1 = True
        else:
            case1 = False
        #case_2
        if 2 <= len(s) <= 6:
            case2 = True
        else:
            case2 = False
        #case_3
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
        #case_4
        if s.isalnum():
            case4 = True
        else:
            case4 = False
        #is_valid
        if case1 and case2 and case3 and case4:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()