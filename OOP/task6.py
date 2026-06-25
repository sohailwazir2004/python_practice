# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any 
# vehicle is seating capacity * 100. If Vehicle is Bus instance, 
# we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final 
# fare amount should be 5500. You need to override the fare() 
# method of a Vehicle class in Bus class.

class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
    def fare(self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare(self):
        base_fare =  super().fare()
        return base_fare +  (base_fare*0.1)
bus = Bus(20)
print(bus.fare())

