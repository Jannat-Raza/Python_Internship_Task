def check_sack(weight, contents):
    # Constants for weight limits
    CEMENT_MIN_WEIGHT = 24.9
    CEMENT_MAX_WEIGHT = 25.1
    GRAVEL_SAND_MIN_WEIGHT = 49.9
    GRAVEL_SAND_MAX_WEIGHT = 50.1

    # Check weight
    if contents == 'C':
        if not (CEMENT_MIN_WEIGHT < weight < CEMENT_MAX_WEIGHT):
            return False, "Cement sack weight should be between 24.9 and 25.1 kilograms."
    elif contents in ['G', 'S']:
        if not (GRAVEL_SAND_MIN_WEIGHT < weight < GRAVEL_SAND_MAX_WEIGHT):
            return False, "Gravel or sand sack weight should be between 49.9 and 50.1 kilograms."
    else:
        return False, "Invalid contents. Only C, G, or S are allowed."

    return True, "Accepted"


def calculate_price(cement_sacks, gravel_sacks, sand_sacks):
    # Constants for prices
    REGULAR_PRICE_CEMENT = 3
    REGULAR_PRICE_GRAVEL = 2
    REGULAR_PRICE_SAND = 2
    SPECIAL_PACK_PRICE = 10

    # Variables to track order details
    total_weight = 0
    rejected_sacks = 0
    total_price = 0
    special_packs = 0

    # Check cement sacks
    for _ in range(cement_sacks):
        print("Checking cement sack", _ + 1)
        weight = float(input("Enter the weight of the cement sack in kilograms: "))
        contents = 'C'
        is_accepted, rejection_reason = check_sack(weight, contents)

        if not is_accepted:
            rejected_sacks += 1
            print("Rejected:", rejection_reason)
        else:
            total_weight += weight
            total_price += REGULAR_PRICE_CEMENT

    # Check gravel sacks
    for _ in range(gravel_sacks):
        print("Checking gravel sack", _ + 1)
        weight = float(input("Enter the weight of the gravel sack in kilograms: "))
        contents = 'G'
        is_accepted, rejection_reason = check_sack(weight, contents)

        if not is_accepted:
            rejected_sacks += 1
            print("Rejected:", rejection_reason)
        else:
            total_weight += weight
            total_price += REGULAR_PRICE_GRAVEL

    # Check sand sacks
    for _ in range(sand_sacks):
        print("Checking sand sack", _ + 1)
        weight = float(input("Enter the weight of the sand sack in kilograms: "))
        contents = 'S'
        is_accepted, rejection_reason = check_sack(weight, contents)

        if not is_accepted:
            rejected_sacks += 1
            print("Rejected:", rejection_reason)
        else:
            total_weight += weight
            total_price += REGULAR_PRICE_SAND

    # Calculate special packs
    special_packs = min(cement_sacks, sand_sacks // 2, gravel_sacks // 2)
    total_price -= special_packs * (REGULAR_PRICE_CEMENT + 2 * REGULAR_PRICE_SAND + 2 * REGULAR_PRICE_GRAVEL)
    total_price += special_packs * SPECIAL_PACK_PRICE

    # Output order details
    print("Order details:")
    print("Total weight:", total_weight, "kilograms")
    print("Number of rejected sacks:", rejected_sacks)
    print("Regular price for the order: $", total_price + (rejected_sacks * REGULAR_PRICE_CEMENT))
    if special_packs > 0:
        amount_saved = special_packs * ((REGULAR_PRICE_CEMENT + 2 * REGULAR_PRICE_SAND + 2 * REGULAR_PRICE_GRAVEL) - SPECIAL_PACK_PRICE)
        print("Special packs applied:", special_packs)
        print("Discounted price for the order: $", total_price + (rejected_sacks * REGULAR_PRICE_CEMENT))
        print("Amount saved: $", amount_saved)


# Test the program
cement_sacks = int(input("Enter the number of cement sacks: "))
gravel_sacks = int(input("Enter the number of gravel sacks: "))
sand_sacks = int(input("Enter the number of sand sacks: "))

calculate_price(cement_sacks, gravel_sacks, sand_sacks)