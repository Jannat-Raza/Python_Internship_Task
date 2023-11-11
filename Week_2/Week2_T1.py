# Constants
NUM_JOURNEYS = 4
NUM_COACHES = 6
SEATS_PER_COACH = 80
TICKET_PRICE = 25

# Initialize data structures for passengers and revenue
passengers_up = [0] * NUM_JOURNEYS
passengers_down = [0] * NUM_JOURNEYS
revenue_up = [0] * NUM_JOURNEYS
revenue_down = [0] * NUM_JOURNEYS

# Function to display the screen
def display_screen():
    print("Train Schedule:")
    print("---------------")
    for journey in range(NUM_JOURNEYS):
        print(f"Journey {journey+1}: {passengers_up[journey]} passengers up | {passengers_down[journey]} passengers down")
    print()
    for journey in range(NUM_JOURNEYS):
        print(f"Journey {journey+1}: ${revenue_up[journey]} revenue up | ${revenue_down[journey]} revenue down")

# Set up the screen display for the start of the day
display_screen()