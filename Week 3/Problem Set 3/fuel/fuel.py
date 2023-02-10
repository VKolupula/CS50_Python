def main():
    fl = fuellevel()
    if fl <= 1:
        print("E")
    elif 99 <= fl <= 100:
        print("F")
    else:
        print(fl, "%", sep="")


def fuellevel():
    while True:
        try:
            XY = input("What is X/Y?: ")
            XY = XY.strip()
            X,Y = XY.split("/")
            X = int(X)
            Y = int(Y)
            n = ((X/Y*100))
            n = round(n)
            if n > 100:
                print("X>Y!")
                continue
        except ZeroDivisionError:
            print("Division Error!")
        except ValueError:
            print("Invalid Input!")
        else:
            return n

main()