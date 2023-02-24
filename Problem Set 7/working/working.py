import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        s = s.strip()
        if match := re.search(
            r"(\d+) ([AM|PM].) to (\d+) ([AM|PM].)", s, re.IGNORECASE
        ):
            h1 = int(match.group(1))
            h2 = int(match.group(3))
            t1 = match.group(2)
            t2 = match.group(4)
            if (h1 and h2 <= 12) and (h1 and h2 > 0):
                h1 = hour(h1, t1)
                h2 = hour(h2, t2)
                formatted = f"{h1}:00 to {h2}:00"
                return formatted
            else:
                raise ValueError()

        elif match := re.search(
            r"(\d+):(\d+) ([AM|PM].) to (\d+):(\d+) ([AM|PM].)", s, re.IGNORECASE
        ):
            h1 = int(match.group(1))
            h2 = int(match.group(4))
            m1 = int(match.group(2))
            m2 = int(match.group(5))
            t1 = match.group(3)
            t2 = match.group(6)
            if (h1 and h2 <= 12) and (h1 and h2 > 0) and (m1 < 60 > m2):
                h1 = hour(h1, t1)
                h2 = hour(h2, t2)
                formatted = f"{h1}:{m1:02d} to {h2}:{m2:02d}"
                return formatted
            else:
                raise ValueError()
        else:
            raise ValueError()
    except ValueError:
        raise ValueError()


def hour(h, t):
    if h == 12 and t == "AM":
        h = 00
        return f"{h:02d}"
    elif t == "AM":
        return f"{h:02d}"
    elif h == 12 and t == "PM":
        return f"{h:02d}"
    else:
        return f"{(h+12):02d}"


if __name__ == "__main__":
    main()
