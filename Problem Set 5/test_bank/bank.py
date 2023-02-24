def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().lower()
    firstword = greeting[0:5]
    firstletter = greeting[0]

    if firstword == "hello":
        due = int(0)
        return due
    elif firstletter == "h":
        due = int(20)
        return due
    else:
        due = int(100)
        return due

if __name__ == "__main__":
    main()

