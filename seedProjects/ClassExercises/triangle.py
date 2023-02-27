user_input = int(input("how many triangle lines do you want"))

for i in range(user_input):
    for j in range(i):
        print("*  ",end="")
    print("\n")


