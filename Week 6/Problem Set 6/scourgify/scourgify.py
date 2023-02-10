import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if file1[-4:] != ".csv" and file2[-4:] != ".csv":
        sys.exit("Not a CSV file")

    elif file1[-4:] == ".csv" and file2[-4:] == ".csv":
        try:
            first = []
            last = []
            house = []
            with open(sys.argv[1]) as file1:
                reader = csv.DictReader(file1)
                for row in reader:
                    name = row["name"]
                    house.append(row["house"])
                    lastname,firstname = name.split(",")
                    first.append(firstname.strip())
                    lastname = lastname
                    last.append(lastname)

            with open(file2,"w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
                writer.writeheader()
                i = 0
                for row in first:
                    writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
                    writer.writerow({"first": first[i],"last": last[i],"house": house[i]})
                    i = i+1
        except FileNotFoundError:
           sys.exit(f"Could not read {sys.argv[1]}")
else:
    print("Unknown Condition")
