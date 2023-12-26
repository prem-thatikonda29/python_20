from datetime import datetime, timedelta
from time import sleep

class Room:
    def __init__(self, roomID, availability, capacity):
        self.roomID = roomID
        self.availability = availability
        self.capacity = capacity
    
    def is_available(self):
        return self.availability
    
    def book_room(self, user):
        if self.is_available():
            print(f"Room {self.roomID} booked by {user.name}")
            self.availability = False
        else:
            print("Room not available")
    

class User:
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
    
class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def book_room(self, room):
        room.availability = "Unavailable"

    def check_availability(self):
        available_rooms = [room for room in self.rooms if room.availability=="Available"]
        print("Fetching available rooms...")
        sleep(1.5)
        print("Available rooms:")
        for room in available_rooms:
            print(f"Room {room.roomID}, Capacity: {room.capacity}")

    def find_room(self, roomID):
        for room in self.rooms:
            if room.roomID == roomID:
                return room
        return None


def main():
    room1 = Room(101, "Available",30)
    room2 = Room(102, "Available",25)
    room3 = Room(103, "Available",25)
    room4 = Room(104, "Available",30)
    room5 = Room(105, "Available",50)

    hotel = Hotel()
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)
    hotel.add_room(room4)
    hotel.add_room(room5)

    print("Enter name: ", end="")
    name = input("")
    user1 = User(name, 1234)

    print("Welcome to Trivago!")
    while True:
        print("\n1)Check available rooms")
        print("2)Book room")
        print("3)Exit")
        cmd = input("\nPlease enter your command (or 'q' to quit): ")
        if cmd == '1':
            hotel.check_availability()
        
        elif cmd == '2':
            print("\nEnter the room number you want to book: ", end='')
            rid = int(input())
            roomToBook = hotel.find_room(rid)
            if roomToBook is not None:
                print("Booking room...")
                sleep(1)
                roomToBook.book_room(user1)
                hotel.book_room(roomToBook)
            else:
                print("Room unavailable")

        elif cmd == '3':
            print("Exiting. Thank you!")
            break


if __name__=="__main__":
    main()