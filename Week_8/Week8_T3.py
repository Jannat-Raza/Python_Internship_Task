def calculate_daily_profit_all_boats():
    # Constants
    boat_cost_per_hour = 20
    boat_cost_per_half_hour = 12
    opening_hour = 10
    closing_hour = 17

    # Variables
    money_taken = 0
    total_hours_hired = 0
    boats_not_used = []
    boat_usage = {}

    # Calculate daily profit for each boat
    for boat_number in range(1, 11):
        # Input hire start time
        start_hour = int(input("Enter the start hour for boat {} (10-16): ".format(boat_number)))
        start_minute = int(input("Enter the start minute for boat {} (0 or 30): ".format(boat_number)))

        # Validate start time
        if start_hour < opening_hour or start_hour >= closing_hour or (start_minute != 0 and start_minute != 30):
            print("Invalid start time for boat {}. Boats can only be hired between 10:00 and 17:00 in half-hour intervals.".format(boat_number))
            continue

        # Input hire duration
        duration = int(input("Enter the duration in hours for boat {} (1 or 0.5): ".format(boat_number)))

        # Validate duration
        if duration != 1 and duration != 0.5:
            print("Invalid duration for boat {}. Boats can only be hired for 1 hour or 0.5 hours.".format(boat_number))
            continue

        # Calculate hire cost
        if duration == 1:
            hire_cost = boat_cost_per_hour
        else:
            hire_cost = boat_cost_per_half_hour

        # Update money taken and total hours hired
        money_taken += hire_cost
        total_hours_hired += duration

        # Update boat usage dictionary
        if boat_number in boat_usage:
            boat_usage[boat_number] += duration
        else:
            boat_usage[boat_number] = duration

    # Calculate boats not used
    for boat_number in range(1, 11):
        if boat_number not in boat_usage:
            boats_not_used.append(boat_number)

    # Find boat used the most
    if boat_usage:
        max_usage_boat = max(boat_usage, key=boat_usage.get)
    else:
        max_usage_boat = None

    # Generate report
    print("----- Daily Profit Report -----")
    print("Total money taken for all boats today: $", money_taken)
    print("Total hours hired for all boats today:", total_hours_hired)
    print("Boats not used today:", boats_not_used)
    if max_usage_boat:
        print("Boat used the most today: Boat", max_usage_boat)
    else:
        print("No boats were used today.")


# Test the program
calculate_daily_profit_all_boats()