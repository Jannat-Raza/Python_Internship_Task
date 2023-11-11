# Ticket prices and discounts
single_ticket_price = 10.0
group_ticket_price = 8.0
group_discount_threshold = 5
group_discount_percentage = 0.1

# Ticket availability
available_tickets_up = 10
available_tickets_down = 10

# Initialize totals
total_tickets_sold = 0
total_revenue = 0.0

def purchase_tickets(num_tickets):
    global available_tickets_up, available_tickets_down, total_tickets_sold, total_revenue
    
    if num_tickets <= available_tickets_up and num_tickets <= available_tickets_down:
        available_tickets_up -= num_tickets
        available_tickets_down -= num_tickets
        total_tickets_sold += num_tickets

        if num_tickets >= group_discount_threshold:
            ticket_price = group_ticket_price * (1 - group_discount_percentage)
        else:
            ticket_price = single_ticket_price

        total_revenue += num_tickets * ticket_price

        print(f"{num_tickets} ticket(s) purchased successfully!")
    else:
        print("Sorry, not enough tickets available for the required train journeys.")

# Example usage
purchase_tickets(1)
purchase_tickets(4)

print("Total Tickets Sold:", total_tickets_sold)
print("Total Revenue:", total_revenue)