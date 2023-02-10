import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n < 1:
        continue
    else:
        randomnum = random.randrange(1, n+1)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess == randomnum:
                print("Just right!")
                break
            elif guess >= 0 and guess < randomnum:
                print("Too small!")
            elif guess > randomnum:
                print("Too large!")
            else:
                continue
    break