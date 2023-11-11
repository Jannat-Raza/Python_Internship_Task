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

# Initialize journey data
journey_data = {
    'up': {'passengers': 0, 'revenue': 0.0},
    'down': {'passengers': 0, 'revenue': 0.0}
}

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

        return ticket_price
    else:
        return None

# Example usage
ticket_prices = []
ticket_prices.append(purchase_tickets(2))
ticket_prices.append(purchase_tickets(4))
ticket_prices.append(purchase_tickets(5))

journey_data['up']['passengers'] = ticket_prices.count(single_ticket_price)
journey_data['up']['revenue'] = ticket_prices.count(single_ticket_price) * single_ticket_price

journey_data['down']['passengers'] = ticket_prices.count(group_ticket_price * (1 - group_discount_percentage))
journey_data['down']['revenue'] = ticket_prices.count(group_ticket_price * (1 - group_discount_percentage)) * (group_ticket_price * (1 - group_discount_percentage))

total_passengers = journey_data['up']['passengers'] + journey_data['down']['passengers']
total_money_taken = journey_data['up']['revenue'] + journey_data['down']['revenue']

journey_with_most_passengers = max(journey_data, key=lambda x: journey_data[x]['passengers'])

print("Number of passengers for each train journey:")
print("Up Journey:", journey_data['up']['passengers'])
print("Down Journey:", journey_data['down']['passengers'])
print("Total number of passengers:", total_passengers)
print("Total money taken for each train journey:")
print("Up Journey:", journey_data['up']['revenue'])
print("Down Journey:", journey_data['down']['revenue'])
print("Total amount of money taken for the day:", total_money_taken)
print("Train journey with the most passengers:", journey_with_most_passengers)