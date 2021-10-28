def num_check(question):

print()
print("****Area and Perimeter calculator")

keep_going = ""
while keep_going == "":
    

width = num_check("width: ")
height = num_check("height: ")
area = width * height
perimeter = 2 * (width + height)
print("Perimeter: {:.2f} units".format(perimeter))
print("Area: {:.2f} units".format(perimeter))

keep_going = input("Press <Enter> to keep going or any key to quit")
