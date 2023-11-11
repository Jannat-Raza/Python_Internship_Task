# Define arrays to store item code, description, and price
case= ["A1", "A2"]
case_desc= ["Copact", "Tower"]
case_price = [75.00, 150.00]

ram = ["B1", "B2", "B3"]
ram_desc = ["8GB", "16GB", "32GB"]
ram_price = [79.99, 149.99, 299.99]

mhdd = ["C1", "C2", "C3"]
mhdd_desc = ["1_TB_MHDD", "2_TB_MHDD", "3_TB_MHDD"]
mhdd_price = [49.99, 89.99, 129.99]

# Display the available items
print("Cases:")
for i in range(len(case)):
    print(case[i], case_desc[i], "$", case_price[i])
print("\nRAM:")
for i in range(len(ram)):
    print(ram[i], ram_desc[i], "$", ram_price[i])
print("\nHard Disk Drives:")
for i in range(len(mhdd)):
    print(mhdd[i], mhdd_desc[i], "$", mhdd_price[i])

# Get the customer's choices
chosen_case = input("\nChoose a case (enter code): ")
chosen_ram = input("Choose RAM (enter code): ")
chosen_hdd = input("Choose a Hard Disk Drive (enter code): ")

# Calculate the price of the computer
basic_price =  200.00  # price of basic set of components
total_price = basic_price + case_price[case.index(chosen_case)] + ram_price[ram.index(chosen_ram)] + mhdd_price[mhdd.index(chosen_hdd)]

# Output the chosen items and the price of the computer
print("\nChosen items:")
print(case_desc[case.index(chosen_case)])
print(ram_desc[ram.index(chosen_ram)])
print(mhdd_desc[mhdd.index(chosen_hdd)])
print("Total price: $", total_price)