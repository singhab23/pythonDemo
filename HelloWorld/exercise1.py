weight = int(input("Weight: "))
metric = input("(L)bs or (K)g: ")

if metric.upper() == "L" :
    print(f"You are {weight * 0.454} kgs")
if metric.upper() == "K" :
    print(f"You are {weight * 2.2} pounds")
else:
    print("Please enter correct metric value.")

    #tried the git upload
