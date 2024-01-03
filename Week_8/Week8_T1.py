def calculate_daily_profit():
    # Constants
    boat_cost_per_hour = 20
    boat_cost_per_half_hour = 12
    opening_hour = 10
    closing_hour = 17

    # Variables
    money_taken = 0
    total_hours_hired = 0
    boat_return_time = None

    # Input boat number
    boat_number = int(input("Enter the boat number (1-10): "))

    # Input hire start time
    start_hour = int(input("Enter the start hour (10-16): "))
    start_minute = int(input("Enter the start minute (0 or 30): "))

    # Validate start time
    if start_hour < opening_hour or start_hour >= closing_hour or (start_minute != 0 and start_minute != 30):
        print("Invalid start time. Boats can only be hired between 10:00 and 17:00 in half-hour intervals.")
        return

    # Input hire duration
    duration = int(input("Enter the duration in hours (1 or 0.5): "))

    # Validate duration
    if duration != 1 and duration != 0.5:
        print("Invalid duration. Boats can only be hired for 1 hour or 0.5 hours.")
        return

    # Calculate hire cost
    if duration == 1:
        hire_cost = boat_cost_per_hour
    else:
        hire_cost = boat_cost_per_half_hour

    # Calculate return time
    return_hour = start_hour + duration
    return_minute = start_minute
    if return_hour >= closing_hour:
        return_hour = closing_hour
        return_minute = 0

    # Update money taken and total hours hired
    money_taken += hire_cost
    total_hours_hired += duration

    # Format return time
    return_time = "{:02d}:{:02d}".format(return_hour, return_minute)

    # Output money taken and total hours hired
    print("Money taken for boat", boat_number, "today: $", money_taken)
    print("Total hours hired for boat", boat_number, "today:", total_hours_hired)
    print("Boat", boat_number, "must be returned by", return_time)


# Test the program
calculate_daily_profit()