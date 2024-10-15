weight = int(input("Enter package weight in kilograms: "))
length = int(input("Enter package length in centimeters: "))
width  = int(input("Enter package width in centimeters: "))
height = int(input("Enter package height in centimeters: "))
if weight >= 27:
    if length * width * height > 100000:
        print("Too heavy and too large")
    else:
        print("Too heavy")
elif length * width * height > 100000:
    print("Too large")
    
input()