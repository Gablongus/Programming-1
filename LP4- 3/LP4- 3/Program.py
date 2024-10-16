eggs = input("Enter amount of eggs purchased: ")
extras = eggs%12
dozens = eggs//12
price = 0.0
if dozens>0 and dozens<4:
    price = 0.50
if dozens>=4 and dozens<6:
    price = 0.45
if dozens>=6 and dozens<11:
    price = 0.40
if dozens>=11:
    price = 0.35

dozencost = price * dozens
extracost = extras * round(price/12,3)
finalcost = dozencost + extracost
print ("Final Price = " + str(round(finalcost,2)))


input()