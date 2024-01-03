def check_sack():
    # Prompt for weight and contents
    weight = float(input("Enter the weight of the sack in kilograms: "))
    contents = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ")

    # Check weight
    if contents == 'C':
        if not (24.9 < weight < 25.1):
            print("Rejected: Cement sack weight should be between 24.9 and 25.1 kilograms.")
            return
    elif contents in ['G', 'S']:
        if not (49.9 < weight < 50.1):
            print("Rejected: Gravel or sand sack weight should be between 49.9 and 50.1 kilograms.")
            return
    else:
        print("Rejected: Invalid contents. Only C, G, or S are allowed.")
        return

    # Output accepted sack details
    print("Accepted sack:")
    print("Weight:", weight, "kilograms")
    print("Contents:", contents)


# Test the program
check_sack()