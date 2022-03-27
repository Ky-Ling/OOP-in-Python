from enum import Enum
from datetime import datetime


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0) -> None:
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False
        print(f"New Bike: {self}")


    # def __del__(self):
    #     print(f"Deleting Bike: {self}")


    def update_sale_price(self, sale_price):
        if self.sold:
            return Exception('Action not allowed. Bike has already been sold')
        self.sale_price = sale_price


    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost

        return profit


    def service(self, spent, sale_price=None, condition=None):
        """
        Service the bike and update attributes
        """
        self.cost += spent
        if sale_price:
            self.update_sale_price(sale_price)
        if self.condition:
            self.condition = condition



    @property
    def profit(self):
        if self.sold is False:
            return None
        return self.sale_price - self.cost


    @staticmethod
    def age(year):
        current_year = datetime.now().year
        age = current_year - year
        if age < 1:
            return "New"
        elif age < 5:
            return "Recent"
        elif age < 40:
            return "Old"
        else:
            return "Vintage"

    



    @classmethod
    def get_default_bike(cls):
        return cls (
            description = "This is a default bike",
            condition = Condition.GOOD,
            sale_price = 100
        )


    # def __repr__(self) -> str:
    #     sold_or_price = "sold" if self.sold else f"${self.sale_price}"
        
    #     return f"Bike: {self.description} ({self.sold_or_price})"

    def __str__(self) -> str:
        return self.description


if __name__ == "__main__":
    bike = Bike.get_default_bike()
    bike.sell()
    print(bike.profit)

