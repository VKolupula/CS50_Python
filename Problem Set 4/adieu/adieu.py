namelist = []
while True:
    try:
        name = input("")
        name = name.strip()
        namelist.append(name)

    except EOFError:
        print("Adieu, adieu, to ",end = "")

        if len(namelist) == 1:
            print(namelist[0])
            break
        elif len(namelist) == 2:
            for j in range(len(namelist)-1):
                print(namelist[j],end = " ")
            print("and", namelist[-1])
            break
        else:
            for j in range(len(namelist)-1):
                print(namelist[j],end = ", ")
            print("and", namelist[-1])
            break

