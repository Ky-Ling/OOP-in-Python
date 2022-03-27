def create(description, cost, sale_price, condition):
    return {
        "description": description,
        "cost": cost,
        "sale_price": sale_price,
        "condition": condition,
        "sold": False
    }


def update_sale_price(bike, sale_price):
    if bike["sold"] == True:
        raise Exception("Action not allowed! This bike has already sold!")

    bike["sale_price"] = sale_price


def sell(bike, sold_for=None):
    if sold_for:
        update_sale_price(bike, sold_for)
    
    bike["sold"] = True
    price = bike["sale_price"] - bike["cost"]
    
    return price


    

bike1 = create("USA", cost=100, sale_price=300, condition=0.2)
update_sale_price(bike=bike1, sale_price=500)
print(sell(bike1))
