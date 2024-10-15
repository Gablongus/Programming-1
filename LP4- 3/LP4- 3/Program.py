eggs = int(input("Enter amount of eggs purchased: "))
extras = eggs%12
dozens = eggs-extras/12
price = 0.50
if dozens>0 and dozens<4:
    price = int(0.50)
    
print"Final Price= " + str((price * dozens)+ extras * (1/12 * price))

input()