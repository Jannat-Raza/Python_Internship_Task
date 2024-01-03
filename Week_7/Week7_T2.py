def record_and_total_donation(charity_names, charity_totals):
   """Records and totals a donation for a customer's shopping bill."""

   while True:
       try:
           charity_choice = int(input("\nEnter your choice of charity (1, 2, or 3): "))
           if 1 <= charity_choice <= 3:
               break  # Valid choice
           else:
               print("Invalid choice. Please enter 1, 2, or 3.")
       except ValueError:
           print("Invalid input. Please enter a number between 1 and 3 for the charity choice.")

   while True:
       try:
           bill_value = float(input("Enter the value of the customer's shopping bill: "))
           if bill_value >= 0:  # Ensure bill value is not negative
               break
           else:
               print("Invalid bill value. Please enter a non-negative value.")
       except ValueError:
           print("Invalid input. Please enter a numerical value for the bill.")

   donation = bill_value * 0.01
   charity_totals[charity_choice - 1] += donation  # Add donation to the correct total

   print("\nDonation details:")
   print("Charity:", charity_names[charity_choice - 1])
   print("Donation amount: $", donation)


# Test the donation recording
charity_names = ["Charity A", "Charity B", "Charity C"]  # Example names
charity_totals = [0, 0, 0]
record_and_total_donation(charity_names, charity_totals)
print("\nUpdated charity totals:", charity_totals)
