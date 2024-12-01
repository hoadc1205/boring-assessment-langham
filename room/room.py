from utility.helper import InputCommand, InputFloat, InputDateTime, InputRoomType, InputRoomNumber
from utility.constant import RoomType, RoomStatus

# Global variable to store room data
roomData = {}

# Global variable to store room allocation data
roomAllocationData = {}

class Room:
    
    def __init__(self, type: str, price: float, status: str, description: str):
        self.type = type
        self.price = price
        self.status = status
        self.description = description

    def __repr__(self):
        return f"{self.type}, {self.price}, {self.status}, {self.description}"
    
# Test data
roomData['403'] = Room(RoomType.SINGLE, 100.0, RoomStatus.OCCUPIED, 'Testing Data')

# Function to add room
def addRoom():
    while True:
        try:
            roomNumber = InputRoomNumber("Enter room number: ")
            if roomNumber in roomData:
                raise ValueError(f'Room {roomNumber} already exists, please choose another room number')
            type = InputRoomType("Enter room type (single/double/suite): ")
            price = InputFloat("Enter room price: ")
            description = input("Enter room description: ")
            
            room = Room(type, price, RoomStatus.AVAILABLE, description)
            roomData[roomNumber] = room
            print(f'room {roomNumber} added')
            return
        except TypeError as typeErr:
            print("Type Error:", typeErr)
            return
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
            return
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
            return
        except NameError as nameErr:
            print("Name Error:", nameErr)
            return
        except KeyError as keyErr:
            print("Key Error:", keyErr)
            return
        except Exception as err:
            print("An unexpected error occurred:", err)
            return

# Function to display rooms
def displayRooms():
    if len(roomData) == 0:
        print('No rooms found')
    else:
        print('********************************************************')
        for roomNumber, room in roomData.items():
            print(f'Room Number: {roomNumber} --- Type: {room.type}, Price: {room.price}, Status: {room.status}, Description: {room.description}')
        print('********************************************************')
    return

# Function to delete room
def deleteRoom():
    try:
        roomNumber = InputRoomNumber("Enter room number you want to delete: ")
        if roomNumber not in roomData:
            raise ValueError(f'Room {roomNumber} does not exist')
        if roomNumber in roomAllocationData:
            raise ValueError(f'Room {roomNumber} release room before deleting')
        #if roomAllocationData[roomNumber] is not None:
        #    raise ValueError(f'Room {roomNumber} release room before deleting')
        del roomData[roomNumber]
        print(f'Room {roomNumber} deleted')
        return
    except TypeError as typeErr:
        print("Type Error:", typeErr)
        return
    except ValueError as valueErr:
        print('Value Error: ', valueErr)
        return
    except AttributeError as attributeErr:
        print("Attribute Error:", attributeErr)
        return
    except NameError as nameErr:
        print("Name Error:", nameErr)
        return
    except KeyError as keyErr:
        print("Key Error:", keyErr)
        return
    except Exception as err:
        print("An unexpected error occurred:", err)
        return
