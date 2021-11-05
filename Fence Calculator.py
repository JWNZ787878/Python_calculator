def num_check(question):
    valid = False
    num = 0

    while not valid:

        response = float(input(question))

        if response > 0:
            num = response
            valid = True 

        else:
            print("Please enter a Number that is more than zero")
            print()

    return num

   

# main program
keep_going = ""
while keep_going == "":
    

    width = num_check("Enter width of area: ")
    height = num_check("Enter height of area: ")
    cost = num_check("Enter cost of per meter: ")

    perimeter = 2 * (width * height)
    total_cost = cost * perimeter
    print("Total Cost per meter= ",total_cost )
    
    keep_going = input("Press <Enter> to keep going or any key to quit")