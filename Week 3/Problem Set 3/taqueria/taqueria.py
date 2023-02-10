itemlist = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

orderlist = []
i = 0
while True:
        try:
            cusorder = input("item: ")
            cusorder = cusorder.strip().title()
            i = i+1
        except EOFError:
            print()
            break
        if cusorder in itemlist:
                orderlist.append(itemlist[cusorder])
                total = float(sum(orderlist))
                print("Total: $%.2f" % total, sep = "")
        elif len(orderlist)>0:
            print("Total $", total, sep = "")
        elif i >= 5:
            print("loop")
            break










