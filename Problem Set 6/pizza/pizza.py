import sys
import csv
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    file = sys.argv[1]

    if file[-4:] != ".csv":
        sys.exit("Not a CSV file")
    elif file[-4:] == ".csv":
        try:
            table = []
            header = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                i = 0
                for line in reader:
                    if i==0:
                        header = line
                        i = i+1
                    else:
                        table.append(line)
            from tabulate import tabulate
            print(tabulate(table, header, tablefmt="grid"))

        except FileNotFoundError:
           sys.exit("File does not exist")
else:
    print("Unknown Condition")
