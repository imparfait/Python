class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return False

    def __add__(self, passengers):
        if not isinstance(passengers, int):
            raise ValueError("Passengers count must be an integer.")
        new_count = self.current_passengers + passengers
        if new_count > self.max_passengers:
            raise ValueError("Exceeds maximum passenger capacity!")
        return Airplane(self.airplane_type, self.max_passengers, new_count)

    def __sub__(self, passengers):
        if not isinstance(passengers, int):
            raise ValueError("Passengers count must be an integer.")
        new_count = self.current_passengers - passengers
        if new_count < 0:
            raise ValueError("Passenger count cannot be negative!")
        return Airplane(self.airplane_type, self.max_passengers, new_count)

    def __iadd__(self, passengers):
        if not isinstance(passengers, int):
            raise ValueError("Passengers count must be an integer.")
        self.current_passengers += passengers
        if self.current_passengers > self.max_passengers:
            raise ValueError("Exceeds maximum passenger capacity!")
        return self

    def __isub__(self, passengers):
        if not isinstance(passengers, int):
            raise ValueError("Passengers count must be an integer.")
        self.current_passengers -= passengers
        if self.current_passengers < 0:
            raise ValueError("Passenger count cannot be negative!")
        return self

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __repr__(self):
        return ("=================\n"
                f"Type: {self.airplane_type} \n"
                f"Max passengers: {self.max_passengers} \n"
                f"Current passengers count: {self.current_passengers}\n"
                "=================")

plane1 = Airplane("Boeing 737", 200, 50)
plane2 = Airplane("Airbus A320", 180, 100)

print(plane1 == plane2)
plane1 += 30
print(plane1)  
plane2 -= 20
print(plane2) 
print(plane1 > plane2)  
print(plane1 <= plane2) 
plane3 = plane1 + 50
print(plane3) 