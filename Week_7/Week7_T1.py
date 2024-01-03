def donation_system():
    # Input charity names
    charity1 = input("Enter the name of the first charity: ")
    charity2 = input("Enter the name of the second charity: ")
    charity3 = input("Enter the name of the third charity: ")

    # Display charity names with numbers
    print("Charities:")
    print("1. ", charity1)
    print("2. ", charity2)
    print("3. ", charity3)

    # Initialize donation totals for each charity
    total_donation1 = 0
    total_donation2 = 0
    total_donation3 = 0

    while True:
        # Input customer's choice of charity
        choice = input("Choose a charity (1, 2, or 3): ")

        # Validate the choice
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        # Input customer's shopping bill
        shopping_bill = float(input("Enter the customer's shopping bill: "))

        # Calculate the donation
        donation = shopping_bill * 0.01

        # Update the total donation for the chosen charity
        if choice == '1':
            total_donation1 += donation
        elif choice == '2':
            total_donation2 += donation
        else:
            total_donation3 += donation

        # Display the donation amount for the chosen charity
        print("Donation of $", donation, "has been made to", end=" ")
        if choice == '1':
            print(charity1)
        elif choice == '2':
            print(charity2)
        else:
            print(charity3)

        # Prompt for another donation
        another_donation = input("Enter 'Y' to record another donation or any other key to exit: ")
        if another_donation != 'Y':
            break

    # Display the total donations for each charity
    print("Total donations:")
    print(charity1, ": $", total_donation1)
    print(charity2, ": $", total_donation2)
    print(charity3, ": $", total_donation3)


# Test the program
donation_system()