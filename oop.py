# exercise : Create a Bus class that inherits from the Vehicle class.
# Define a property that must have the same value for every class instance.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare() + 0.1*super().fare()
        return total_fare


model = Bus("das",200,20,50)
# exercise : Write a line to determine which class a given Bus object belongs to.
print(type(object))
# exercise : Determine if model is also an instance of the Vehicle class
print(isinstance(model,Vehicle))