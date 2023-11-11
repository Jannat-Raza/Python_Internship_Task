# Arrays to store item code, description, and price
item_codes = ['CASE1', 'CASE2', 'CASE3']
descriptions = ['Case A', 'Case B', 'Case C']
prices = [50.0, 60.0, 70.0]

# Function to display available items
def display_items():
    print("Available Items:")
    print("----------------")
    for i in range(len(item_codes)):
        print(f"{i+1}. {descriptions[i]} (Code: {item_codes[i]}) - ${prices[i]}")

# Function to calculate the total price
def calculate_price(case_index, ram_price, hdd_price, additional_prices):
    basic_set_price = 100.0
    case_price = prices[case_index]
    total_price = basic_set_price + case_price + ram_price + hdd_price + sum(additional_prices)
    return total_price

# Display available items
display_items()

# Get user's choice for case
case_choice = int(input("\nEnter the index of your chosen case: ")) - 1
if case_choice < 0 or case_choice >= len(item_codes):
    print("Invalid choice!")
    exit()

# Get user's choice for RAM
ram_price = float(input("Enter the price of the chosen RAM: "))

# Get user's choice for Main Hard Disk Drive
hdd_price = float(input("Enter the price of the chosen Main Hard Disk Drive: "))

# Empty list to store additional item prices
additional_prices = []

# Prompt the user for additional items
additional_choice = input("\nDo you want to purchase any items from other categories? (yes/no): ").lower()

while additional_choice == "yes":
    display_items()
    item_choice = int(input("Enter the index of the additional item you want to purchase: ")) - 1
    if item_choice < 0 or item_choice >= len(item_codes):
        print("Invalid choice!")
        continue
    item_price = float(input("Enter the price of the chosen additional item: "))
    additional_prices.append(item_price)
    additional_choice = input("\nDo you want to purchase any more items from other categories? (yes/no): ").lower()

# Calculate the total price
total_price = calculate_price(case_choice, ram_price, hdd_price, additional_prices)

# Output the chosen items and the price of the computer
print("\nChosen Items:")
print("-------------")
print(f"Case: {descriptions[case_choice]} (Code: {item_codes[case_choice]})")
print(f"RAM Price: ${ram_price}")
print(f"Main Hard Disk Drive Price: ${hdd_price}")

if additional_prices:
    print("\nAdditional Items:")
    print("-----------------")
    for i in range(len(additional_prices)):
        print(f"Item {i+1} Price: ${additional_prices[i]}")

print(f"\nTotal Price of the Computer: ${total_price}")