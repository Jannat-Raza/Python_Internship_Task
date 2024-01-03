from datetime import datetime, timedelta

# Constants
BOAT_COUNT = 10
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_TIME = 10
CLOSING_TIME = 17

# Data structure to store boat information
boats = [{"hours_hired": 0, "return_time": None} for _ in range(BOAT_COUNT)]

# Function to calculate money taken for one boat in a day (Task 1)
def calculate_money_for_one_boat(boat_index, hours):
    if OPENING_TIME <= hours <= CLOSING_TIME:
        if boats[boat_index]["return_time"] is None or datetime.now() >= boats[boat_index]["return_time"]:
            # Calculate the cost based on the time hired
            if hours % 1 == 0:  # Whole hours
                cost = hours * HOURLY_RATE
            else:  # Half-hour increments
                cost = (hours // 0.5) * HALF_HOUR_RATE

            # Update boat information
            boats[boat_index]["hours_hired"] += hours
            boats[boat_index]["return_time"] = datetime.now() + timedelta(hours=hours)

            return cost
        else:
            return "Boat not available until {}".format(boats[boat_index]["return_time"].strftime("%H:%M"))
    else:
        return "Boat can only be hired between {} and {}".format(OPENING_TIME, CLOSING_TIME)

# Function to find the next available boat (Task 2)
def find_next_available_boat():
    current_time = datetime.now()
    available_boats = []

    for i, boat in enumerate(boats, start=1):
        if boat["return_time"] is None or current_time >= boat["return_time"]:
            available_boats.append(i)
    
    if available_boats:
        return f"Available boats: {', '.join(map(str, available_boats))}"
    else:
        earliest_return_time = min(boat["return_time"] for boat in boats)
        return f"No available boats. Next available time: {earliest_return_time.strftime('%H:%M')}"

# Test Task 1 for one boat
boat_index = 0
hours_hired = float(input("Enter the hours to hire the boat: "))
result = calculate_money_for_one_boat(boat_index, hours_hired)
print(result)

# Test Task 2 for all boats
result_task2 = find_next_available_boat()
print(result_task2)
