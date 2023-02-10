bank = input("Greeting: ")

bank = bank.strip().lower()
firstword = bank[0:5]
firstletter = bank[0]

if firstword == "hello":
    print("$0")
elif firstletter == "h":
    print("$20")
else:
    print("$100")
