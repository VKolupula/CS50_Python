import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(
        r"\"https?://(?:www\.)?youtube.com/embed/(\w+)\"", s, re.IGNORECASE
    ):
        link = f"https://youtu.be/{match.group(1)}"
        return link
    else:
        return None


if __name__ == "__main__":
    main()
