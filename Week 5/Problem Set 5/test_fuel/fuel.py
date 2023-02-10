def main():
    XY = input("What is X/Y?: ")
    fl = convert(XY)
    print(gauge(fl))

def convert(fraction):
    X, Y = fraction.split("/")
    try:
        X = int(X)
        Y = int(Y)
        return (X / Y)*100
    except (ZeroDivisionError,ValueError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage > 1 and percentage < 99:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
