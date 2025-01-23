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
    """
    This function allows the user to add a new room to the roomData dictionary.
    It prompts the user to enter details such as room number, type, price, and description.
    Various exceptions are handled to ensure data integrity and user-friendly error messages.
    """
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
        except SyntaxError as syntaxErr:
            print("Syntax Error:", syntaxErr)
            return
        except ValueError as valueErr:
            print("Value Error:", valueErr)
            return
        except ZeroDivisionError as zeroDivErr:
            print("Zero Division Error:", zeroDivErr)
            return
        except IndexError as indexErr:
            print("Index Error:", indexErr)
            return
        except NameError as nameErr:
            print("Name Error:", nameErr)
            return
        except TypeError as typeErr:
            print("Type Error:", typeErr)
            return
        except OverflowError as overflowErr:
            print("Overflow Error:", overflowErr)
            return
        except IOError as ioErr:
            print("IO Error:", ioErr)
            return
        except ImportError as importErr:
            print("Import Error:", importErr)
            return
        except EOFError as eofErr:
            print("EOF Error:", eofErr)
            return
        except FileNotFoundError as fileNotFoundErr:
            print("File Not Found Error:", fileNotFoundErr)
            return
        except KeyError as keyErr:
            print("Key Error:", keyErr)
            return
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
            return
        except Exception as err:
            print("An unexpected error occurred:", err)
            return


# Function to display rooms
def displayRooms():
    """
    This function displays a list of all available rooms stored in the roomData dictionary.
    It checks if there are any rooms available and prints their details such as room number, 
    type, price, status, and description. If no rooms are found, it notifies the user.
    """
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
    """
    This function allows the user to delete a room from the roomData dictionary.
    It first checks if the room exists and ensures that the room is not currently allocated.
    If the room is found and not allocated, it is removed from the roomData dictionary.
    Various exceptions are handled to provide meaningful error messages to the user.
    """
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
    except SyntaxError as syntaxErr:
        print("Syntax Error:", syntaxErr)
        return
    except ValueError as valueErr:
        print("Value Error:", valueErr)
        return
    except ZeroDivisionError as zeroDivErr:
        print("Zero Division Error:", zeroDivErr)
        return
    except IndexError as indexErr:
        print("Index Error:", indexErr)
        return
    except NameError as nameErr:
        print("Name Error:", nameErr)
        return
    except TypeError as typeErr:
        print("Type Error:", typeErr)
        return
    except OverflowError as overflowErr:
        print("Overflow Error:", overflowErr)
        return
    except IOError as ioErr:
        print("IO Error:", ioErr)
        return
    except ImportError as importErr:
        print("Import Error:", importErr)
        return
    except EOFError as eofErr:
        print("EOF Error:", eofErr)
        return
    except FileNotFoundError as fileNotFoundErr:
        print("File Not Found Error:", fileNotFoundErr)
        return
    except KeyError as keyErr:
        print("Key Error:", keyErr)
        return
    except AttributeError as attributeErr:
        print("Attribute Error:", attributeErr)
        return
    except Exception as err:
        print("An unexpected error occurred:", err)
        return

