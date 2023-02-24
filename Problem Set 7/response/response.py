import validators

if validators.email(input('Email Id: ')):
    print("Valid")
else:
    print("Invalid")