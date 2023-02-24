deep = input("Type here: ")
deep = deep.lower().strip()

match deep:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
