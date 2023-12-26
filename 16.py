from datetime import datetime, timedelta

class Room:
    def __init__(self, roomID, availability, capacity):
        self.roomID = roomID
        self.availability = availability
        self.capacity = capacity
    
    def is_available(self, room):
        if room.availability:
            return True
        return False

    def book_room(self, room, name):
        if room.is_available(room):
            print(f"{room.roomID} booked by {name}")
        else:
            print(f"Room not available")
    

class User:
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
    

def main():
    pass

if __name__=="__main__":
    main()