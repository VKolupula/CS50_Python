def main():
     time = input("What time is it? ")
     time24 = convert(time)

     if 7.0 <= time24 and time24 <= 8.0:
        print("breakfast time")
     elif 12.0 <= time24 and time24 <= 13.0:
        print("lunch time")
     elif 18.0 <= time24 and time24 <= 19.0:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        hours_minutes, am_pm = time.split()
        hours, minutes = hours_minutes.split(":")
        if am_pm == "p.m." and int(hours) != 12:
            hours = int(hours) + 12
    else:
        hours, minutes = time.split(":")

    hours = float(hours) + (float(minutes)/60)
    return hours

if __name__ == "__main__":
    main()