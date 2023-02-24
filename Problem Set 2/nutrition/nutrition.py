nut = input("Item: ")
nut = nut.strip().lower().title()
itemlist = {
    "Apple": "130",
    "Avocado": "50",
    "Avocado California": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew": "50",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet": "100",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80",
}

while True:
    if nut in itemlist:
        print("Calories: " + itemlist[nut])
        break
    else:
        break


