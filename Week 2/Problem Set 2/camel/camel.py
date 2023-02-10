def main():
    camel = input("Type here: ")
    re = findupper(camel)

    if re == False:
        print(camel)

    else:
        for j in range(len(re)):
            if j <= len(re):
                camel = camel.replace(re[j], "_" + re[j])
        print(camel.lower())

def findupper(camel):
    uppercase = []

    for i in range(len(camel)):
        if camel[i].isupper():
            uppercase.append(camel[i])

    if(len(uppercase) > 0):
        return "".join(uppercase)
    else:
        return False


main()