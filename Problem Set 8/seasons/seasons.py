from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        print(convert_age_minutes(date.fromisoformat(input("Date of Birth: "))))
    except ValueError:
        sys.exit("Value Error")

def convert_age_minutes(b_date):
        age_min = int((date.today()-b_date).total_seconds()/60)
        age_min_word = p.number_to_words(age_min, andword="").capitalize()
        return age_min_word + " minutes"

if __name__ == "__main__":
    main()