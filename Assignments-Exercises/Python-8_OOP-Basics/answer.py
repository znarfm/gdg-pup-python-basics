# Car class
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    # describe method
    def describe(self) -> str:
        return f"This car is a {self.year} {self.make} {self.model}."


# instantiate
car = Car("Toyota", "Corolla", 2020)

# call describe method
print(car.describe())
