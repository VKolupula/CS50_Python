list1 = ['a','e','i','o','u','A','E','I','O','U']
twttr = input("Type here: ")
twttr = twttr

for j in range(len(twttr)):

    if twttr[j] in list1:
        twttr = twttr.replace(twttr[j],"*")

twttr = twttr.replace("*", "")
print(twttr)

