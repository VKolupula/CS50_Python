import re

def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    s = s.strip().lower()
    if s == "um":
        count = 1
        return count
    elif re.search(r"\W?(um)\W?", s, re.IGNORECASE):
        s = s.split()
        for i in range(len(s)):
            if re.search(r"\W*(um)\W*", s[i], re.IGNORECASE):
                if re.search(r"[a-z].(um)?+[a-z]", s[i], re.IGNORECASE):
                    continue
                else:
                    count = count+1
        return count
    else:
        return count

if __name__ == "__main__":
    main()