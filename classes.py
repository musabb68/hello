class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self,names):
        if not self.open_seats():
            return False
        self.passengers.append(names)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

names=["musabbir","afsath","papi","shahida"]

for name in names:
    if flight.add_passengers(name):
        print(f"Added {name} to Fkight succesfully")
    else:
        print(f"no available seats for {name}")


