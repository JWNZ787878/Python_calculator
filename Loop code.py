valid = False
while not valid:

    response = float(input("Enter a Number"))

    if response > 0:
        valid = True 

    else:
        print("Please enter a Number that is more than zero")
        print()
