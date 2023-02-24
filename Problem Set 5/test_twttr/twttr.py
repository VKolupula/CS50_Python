def main():
    word = input("Type here: ")
    word = shorten(word)
    print(word)

def shorten(word):
    list1 = ['a','e','i','o','u','A','E','I','O','U']
    word1 = word
    for j in range(len(word)):
        if word[j] in list1:
            word1 = word1.replace(word[j],"")
    return word1

if __name__ == "__main__":
    main()