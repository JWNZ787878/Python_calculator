def num_check(question):
    valid = False

    while not valid:
        response = float(input(question))

    if response > 0:
        valid = True 

    else:
        print("Please enter a Number that is more than zero")
        print()

keep_going = ""
while keep_going == "":
    

    width = num_check("width: ")
    height = num_check("height: ")
    
    area = width * height
    perimeter = 2 * (width + height)

    print("Perimeter: {:.2f} units".format(perimeter))
    print("Area: {:.2f} units".format(perimeter))

keep_going = input("Press <Enter> to keep going or any key to quit")

