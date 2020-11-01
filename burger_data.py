class Burger:

    def __init__(self, restaurant_name, name, price):
        self.restaurant_name = restaurant_name
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} is ${self.price} at {self.restaurant_name}"

    def __eq__(self, other):
        return (self.restaurant_name.lower() == other.restaurant_name.lower()) and \
               (self.name.lower() == other.name.lower())

    def __lt__(self, other):
        if self.restaurant_name.lower() < other.restaurant_name.lower():
            return True
        elif self.restaurant_name == other.restaurant_name:
            return self.name < other.restaurant_name
        else:
            return False

    def print(self):
        print(str(self))