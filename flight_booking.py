 #Problem Statement: Write a Python program that creates a Passenger class and a Flight class. The Flight class should manage a list of Passenger objects and block further bookings when the seat capacity is reached.

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number, seat_capacity):
        self.seat_capacity = seat_capacity
        self.flight_number = flight_number
        self.passengers = []

    def book_flight(self, passenger):
        if len(self.passengers) < self.seat_capacity :
            self.passengers.append(passenger)
            print(f"You have successfully booked a flight {passenger.name}!")
        
        else:
            print(f"Sorry, Flight {self.flight_number} is fully booked.")


p1 = Passenger("George")
p2 = Passenger("Amelia")
p3 = Passenger("chubbycheeks")
first_flight = Flight("ZU243", 2)
first_flight.book_flight(p3)
first_flight.book_flight(p1)
first_flight.book_flight(p2)
