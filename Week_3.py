# Function to calculate and display cost for slab 1
def costSlab1():
    slab1_units = matrix[0]   
    total_cost = sum(slab1_units) * 10   
    print("Slab 1 Bill:")
    print("Total Units:", sum(slab1_units))
    print("Cost per Unit: Rs. 10")
    print("Total Cost: Rs.", total_cost)

# Function to calculate and display cost for slab 2
def costSlab2():
    slab2_units = matrix[1]   
    total_cost = sum(slab2_units) * 15   
    print("Slab 2 Bill:")
    print("Total Units:", sum(slab2_units))
    print("Cost per Unit: Rs. 15")
    print("Total Cost: Rs.", total_cost)
# Function to calculate and display cost for slab 3
def costSlab3():
    slab3_units = matrix[2]   
    total_cost = sum(slab3_units) * 20   
    print("Slab 3 Bill:")
    print("Total Units:", sum(slab3_units))
    print("Cost per Unit: Rs. 20")
    print("Total Cost: Rs.", total_cost)

# Main program
matrix = [
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240]
]

student_id = input("Enter Student ID: ")
print("Welcome, Student", student_id)

while True:
    print("\nMenu:")
    print("1. Display bill of slab 1 and slab 2")
    print("2. Display bill of slab 3")
    print("Press any other key to exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        break