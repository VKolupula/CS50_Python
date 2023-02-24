import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = response.json()["bpi"]["USD"]["rate"]
    rate = rate.replace(",", "")
    rate = float(rate)

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            input = float(sys.argv[1])
            con = input * rate
            print("$", end="")
            print("{:,}".format(con))

        except ValueError:
            sys.exit("Command-line argument is not a number")

except requests.RequestException:
    print("RequestException")
