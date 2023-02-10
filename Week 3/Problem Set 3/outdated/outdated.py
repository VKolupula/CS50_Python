months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input(":")
        formating = date.strip().split()
    except EOFError:
        print()
        break

    if formating[0] in months:
        month,date,year = date.split()
        if date.find(",") < 0:
            continue
        date = int(date.replace(",",""))
        month = int(months.index(month)+1)
        if date > 31 and 0 < month <= 12:
            continue
        year = f"{year:04}"
        date = f"{date:02}"
        month = f"{month:02}"

        print(year,"-",month,"-",date, sep ="")
        break

    else:
        try:
            month,date,year = date.split("/")
            date = int(date)
            month = int(month)
            year = year.strip()
            if date > 31 or month >= 12 or month <=0:
                continue
            year = f"{year:04}"
            date = f"{date:02}"
            month = f"{month:02}"
            print(year,"-",month,"-",date, sep ="")
            break
        except ValueError:
            continue
