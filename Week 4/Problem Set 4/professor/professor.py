import random


def main():
    n = get_level()
    score = int(0)

    for _ in range(10):
        v1 = generate_integer(n)
        v2 = generate_integer(n)
        print(v1, "+", v2, "= ", end="")
        ans = input()
        if check_ans(ans, v1, v2):
            score = score + 1
        else:
            inco_ans = int(1)
            print("EEE")

            while True:
                print(v1, "+", v2, "= ", end="")
                ans = input()
                if check_ans(ans, v1, v2):
                    break
                elif inco_ans >= 2:
                    print(v1, "+", v2, "= ", (v1 + v2))
                    break
                else:
                    inco_ans = inco_ans + 1
                    print("EEE")

    print("score = ", score)


def check_ans(ans, v1, v2):
    try:
        ans = int(ans)
        if ans == (v1 + v2):
            return True
        else:
            return False
    except:
        return False


def get_level():
    while True:
        try:
            n = input("level: ")
            n = int(n)
        except ValueError:
            continue
        if n >= 1 and n <= 3:
            return n
        else:
            continue


def generate_integer(level):
    if level == 1:
        n = random.randrange(0, (10))
        return n
    elif level == 2:
        n = random.randrange(10, (100))
        return n
    elif level == 3:
        n = random.randrange(100, (1000))
        return n


if __name__ == "__main__":
    main()
