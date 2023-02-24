itemlist = []
count = []

while True:
    comitemlist = count+itemlist
    try:
        item = input()
        item = item.strip().upper()

    except EOFError:
        comlist = {itemlist[i]: count[i] for i in range(len(itemlist))
            }
        sortedlist = sorted(comlist)
        for i in range(len(itemlist)):
            print(comlist[sortedlist[i]],sortedlist[i])
        break

    if item in itemlist:
        idx = itemlist.index(item)
        count[idx] = count[idx]+1

    else:
        itemlist.append(item)
        idx = itemlist.index(item)
        count.insert(idx,1)






