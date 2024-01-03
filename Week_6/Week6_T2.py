def check_sack(contents, weight):
    # Constants for weight limits
    CEMENT_MIN_WEIGHT = 24.9
    CEMENT_MAX_WEIGHT = 25.1
    GRAVEL_SAND_MIN_WEIGHT = 49.9
    GRAVEL_SAND_MAX_WEIGHT = 50.1

    if contents == 'C':
        if not (CEMENT_MIN_WEIGHT <= weight <= CEMENT_MAX_WEIGHT):
            return False
    elif contents in ['G', 'S']:
        if not (GRAVEL_SAND_MIN_WEIGHT <= weight <= GRAVEL_SAND_MAX_WEIGHT):
            return False
    else:
        return False

    return True

def check_order():
    total_weight = 0
    rejected_sacks = 0

    # Input data for the order
    num_cement_sacks = int(input("Enter the number of cement sacks: "))
    num_gravel_sacks = int(input("Enter the number of gravel sacks: "))
    num_sand_sacks = int(input("Enter the number of sand sacks: "))

    # Check and process cement sacks
    for _ in range(num_cement_sacks):
        contents = 'C'
        weight = float(input(f"Enter the weight of cement sack {_ + 1} in kilograms: "))
        
        if not check_sack(contents, weight):
            print(f"Rejected: Incorrect weight for cement sack {_ + 1}. Weight should be between 24.9 and 25.1 kilograms.")
            rejected_sacks += 1
        else:
            total_weight += weight

    # Check and process gravel sacks
    for _ in range(num_gravel_sacks):
        contents = input(f"Enter the contents of gravel sack {_ + 1} (G for gravel, S for sand): ").upper()
        weight = float(input(f"Enter the weight of gravel sack {_ + 1} in kilograms: "))

        if contents not in ['G', 'S'] or not check_sack(contents, weight):
            print(f"Rejected: Incorrect weight or contents for gravel sack {_ + 1}. Weight should be between 49.9 and 50.1 kilograms.")
            rejected_sacks += 1
        else:
            total_weight += weight

    # Check and process sand sacks
    for _ in range(num_sand_sacks):
        contents = input(f"Enter the contents of sand sack {_ + 1} (G for gravel, S for sand): ").upper()
        weight = float(input(f"Enter the weight of sand sack {_ + 1} in kilograms: "))

        if contents not in ['G', 'S'] or not check_sack(contents, weight):
            print(f"Rejected: Incorrect weight or contents for sand sack {_ + 1}. Weight should be between 49.9 and 50.1 kilograms.")
            rejected_sacks += 1
        else:
            total_weight += weight

    # Output order details
    print("\nOrder details:")
    print("Total weight:", total_weight, "kilograms")
    print("Number of rejected sacks:", rejected_sacks)

# Task 1 - Check a single sack
print("Task 1 - Check a single sack:")
contents_single_sack = input("Enter contents of the sack (C for cement, G for gravel, S for sand): ").upper()
weight_single_sack = float(input("Enter weight of the sack in kilograms: "))
if check_sack(contents_single_sack, weight_single_sack):
    print("Accepted: Sack with contents '{contents_single_sack}' and weight {weight_single_sack} kilograms.")
else:
    print("Rejected: Incorrect sack. Check contents and weight.")

# Task 2 - Check a customer's order for delivery
print("\nTask 2 - Check a customer's order for delivery:")
check_order()
