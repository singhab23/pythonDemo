import os

os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix

weight = int(input("Weight: "))
metric = input("(L)bs or (K)g: ")

if metric.upper() == "L" :
    print(f"You are {weight * 0.454} kgs")
elif metric.upper() == "K" :
    print(f"You are {weight * 2.2} pounds")
else:
    print("Please enter a correct metric value.")
