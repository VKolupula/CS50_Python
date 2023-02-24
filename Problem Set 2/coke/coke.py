
ac = [25,10,5]
while True:
    ac = [25,10,5]
    coin = int(input("Insert Coin: "))
    if coin in ac:
        break
    else:
        print("Amount Due: 50")

due = int(50 - coin)

while True:
    if due <= 0:
        print("Change Owed: " + str(abs(due)))
        break
    else:
        print("Amount Due: " + str(abs(due)))

        while True:
            newcoin = int(input("Insert Coin: "))
            if newcoin in ac:
                break
    due = due - newcoin





