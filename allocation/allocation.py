import os # Importing OS module for interacting with the operating system (e.g., file operations)
import datetime # Importing datetime module for handling date and time
from room.room import roomData, RoomStatus, roomAllocationData
from utility.helper import InputCommand, InputFloat, InputDateTime, InputCheckInOutDate, InputRoomNumber



roomAllocationFilePath = 'LHMS_850001677.txt'
roomAllocationBackupFilePath = 'LHMS_850001677_Backup_Date_Time.txt'

class RoomAllocation:
    def __init__(self, customerName: str, checkInDate: datetime, checkOutDate: datetime, description: str, price: float, fee: float):
        self.customerName = customerName
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.description = description
        self.price = price
        self.fee = fee

    def __repr__(self):
        return f"{self.customerName}, {self.checkInDate}, {self.checkOutDate}, {self.description}, {self.price}, {self.fee}"

# Test data
roomAllocationData['403'] = RoomAllocation("rackal", datetime.datetime.strptime('2024-11-15 20:00', '%Y-%m-%d %H:%M'), datetime.datetime.strptime('2024-11-16 20:00', '%Y-%m-%d %H:%M'), 'Testing Data', 100, 10)

# Function to add room allocation
def addRoomAllocation():
    """
    Adds a new room allocation after verifying availability and user input.

    The function displays available rooms, prompts the user for room details,
    and updates the room allocation data accordingly.
    """
    print('********************************************************')
    print('AVAILABLE ROOMS')
    totalAvailableRooms = 0
    for roomNumber, room in roomData.items():
            if room.status == RoomStatus.AVAILABLE:
                totalAvailableRooms += 1
                print(f'Room Number: {roomNumber} --- Type: {room.type}, Price: {room.price}, Status: {room.status}, Description: {room.description}')
    if totalAvailableRooms == 0:
        print('No available rooms')
        return            
    print('********************************************************')
    while True:
        try:
            roomNumber = InputRoomNumber("Enter room number: ")
            if roomNumber not in roomData:
                raise ValueError(f'Room {roomNumber} does not exist')
            if roomData[roomNumber].status == RoomStatus.OCCUPIED:
                raise ValueError(f'Room {roomNumber} is occupied')
            customerName = input("Enter customer name: ")
            checkin, checkout = InputCheckInOutDate("Enter check in date (format: 2024-11-10 20:10): ", "Enter check out date (format: 2024-11-10 20:10): ")
            fee = InputFloat("Enter extra fee: ")
            description = input("Enter description: ")

            roomAllocation = RoomAllocation(customerName, checkin, checkout, description, roomData[roomNumber].price, fee)
            roomAllocationData[roomNumber] = roomAllocation
            roomData[roomNumber].status = RoomStatus.OCCUPIED
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

# Function to display room allocations
def displayRoomAllocations():
    """
    Displays the current room allocation data.

    If no room allocations are available, it informs the user.
    Otherwise, it prints the details of each allocated room in a formatted manner.
    """
    if len(roomAllocationData) == 0:
        print("No room allocations found")
    else:
        print('********************************************************')
        for roomNumber, roomAllocation in roomAllocationData.items():
            print(f'Room Number: {roomNumber} --- Customer Name: {roomAllocation.customerName}, Check In Date: {roomAllocation.checkInDate}, Check Out Date: {roomAllocation.checkOutDate}, Description: {roomAllocation.description}')
        print('********************************************************')
    return

# Function to deallocate a room
def roomDeallocation():
    """
    This function handles the deallocation of a room by releasing it and calculating the billing.
    It checks the room's occupancy status, allows updates to checkout date and extra fees,
    and calculates the total cost based on stay duration and additional charges.
    """
    try:
        roomNumber = InputRoomNumber("Enter room number: ")
        if roomNumber not in roomData:
            raise ValueError(f'Room {roomNumber} does not exist')
        if roomData[roomNumber].status != RoomStatus.OCCUPIED:
            raise ValueError(f'Room {roomNumber} is not occupied')
        
        updateCheckoutDate = input("Do you want to update check out date? (yes/no): ")
        if updateCheckoutDate == "yes":
            while True:
                checkout = InputDateTime("Enter check out date (format: 2024-11-10 20:10): ")
                if checkout <= roomAllocationData[roomNumber].checkInDate:
                    print("Check out date must be greater than check in date")
                else:
                    roomAllocationData[roomNumber].checkOutDate = checkout
                    break
        
        extraFee = input("Do you want to update extra fee? (yes/no): ")
        if extraFee == "yes":
            while True:
                fee = InputFloat("Enter fee: ")
                if fee <= 0:
                    print("Fee must be greater than 0")
                else:
                    roomAllocationData[roomNumber].fee = fee
                    break
        
        difference = roomAllocationData[roomNumber].checkOutDate - roomAllocationData[roomNumber].checkInDate
        cost = difference.days * roomAllocationData[roomNumber].price + roomAllocationData[roomNumber].fee
        print(f'Billing for customer {roomAllocationData[roomNumber].customerName}: {cost}')
        print(f'Room {roomNumber} released')

        roomData[roomNumber].status = RoomStatus.AVAILABLE
        del roomAllocationData[roomNumber]

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

# Function to save room allocation data
def saveRoomAllocationData():
    """
    This function saves the room allocation data to a file.
    It iterates over the room allocation dictionary and writes the details to the specified file.
    Exception handling is included to catch any unexpected errors during file operations.
    """
    try:
        with open(roomAllocationFilePath, 'w') as f:
            for key, roomAllocation in roomAllocationData.items():
                f.write(f'Room Number: {key} --- Customer Name: {roomAllocation.customerName}, Check In Date: {roomAllocation.checkInDate}, Check Out Date: {roomAllocation.checkOutDate}, Description: {roomAllocation.description}')
            print(f'Room allocation data saved to {roomAllocationFilePath}')

        f.close()
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

# Function to show room allocation data
def showRoomAllocationData():
    """
    This function reads and displays the content of the room allocation file.
    It handles multiple types of exceptions to ensure the program does not crash due to unexpected errors.
    """
    try:
        with open(roomAllocationFilePath, 'r') as f:
            print(f.read())
        f.close()
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


# Function to backup room allocation data
def backupRoomAllocationData():
    """
    This function creates a backup of the room allocation data by copying 
    the contents of the original file to a backup file with a timestamp.
    After the backup is created, the original file is cleared to prepare for new data.
    Various exceptions are handled to ensure robustness and provide meaningful error messages.
    """
    try:
        # Read data from the original file
        with open(roomAllocationFilePath, 'r') as original_file:
            data = original_file.read() 

        # Append data to the backup file
        with open(roomAllocationBackupFilePath, 'a') as backup_file:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            backup_file.write("**********************\n")
            backup_file.write(f"Backup created at: {current_time}\n")
            backup_file.write(data)
            backup_file.write("**********************\n")

        # Clear the original file
        with open(roomAllocationFilePath, 'w') as original_file:
            original_file.write('')

        print(f'Room allocation data saved to {roomAllocationBackupFilePath}')
        original_file.close()
        backup_file.close()
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
