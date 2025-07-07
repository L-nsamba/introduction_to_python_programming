class Car:
    def __init__(self, Model, Price, Color, Build_Year):
        self.Model = Model
        self.Price = Price
        self.Color = Color
        self.Build_Year = Build_Year

        #Instance Method
    def description(self):
        return f"""
        Your model is {self.Model}
        the price of your car is USD {self.Price}
        the color of your car is {self.Color}
        and the build year of the car is {self.Build_Year}."""


Car_1 = Car("AAA", 2000, "blue", 2012)
Car_2 = Car("UJJJ", 3000, "yellow", 2019 )
Car_3 = Car("TTXX", 4700, "green", 2009)

print(Car_1.description())
print(Car_2.description())
print(Car_3.description())
print()
