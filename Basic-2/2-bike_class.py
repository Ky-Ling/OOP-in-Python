from enum import Enum

class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass

class Bike:

    def __init__(self, description, sale_price, condition, cost=0):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition

        self.sold = False

        def __repr__(self):
            return f"{self.description} + {self.sale_price}"

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("It has been sold! You can not update it!")

        self.sale_price = new_sale_price

        return self.sale_price

    def sell(self):
        self.sold = True
        price = self.cost - self.sale_price

        return price

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost

        if new_sale_price:
            self.update_sale_price(new_sale_price)

        if new_condition:
            self.condition = new_condition
        


my_bike = Bike("Computer", 100, Condition.GOOD, 40)

print(my_bike.update_sale_price(400))

profit = my_bike.sell()
print(profit)