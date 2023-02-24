import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    file = sys.argv[1]
    if file[-2:] != "py":
        sys.exit("Not a Python file")
    elif file[-2:] == "py":
        No_lines = 0
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip()
                    if not line.startswith("#") and line != "":
                        No_lines = No_lines+1

            print(No_lines)
        except FileNotFoundError:
            print("File does not exist")
else:
    print("Unknown Condition")
