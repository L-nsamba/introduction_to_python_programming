#Function to create a price list

def price_calculator(cart):
    total = 0
    for items, cost in cart.items():
        total += cost
    return total

cart = {"orange": 5.00, "apple": 8.2, "avacado": 22.7, "mango": 6.97}

print(price_calculator(cart))