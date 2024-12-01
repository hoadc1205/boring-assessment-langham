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
roomAllocationData['403'] = RoomAllocation("rackal", datetime.datetime.strptime('2024-11-15 20:00', '%Y-%m-%d %H:%M'), datetime.datetime.strptime('2024-11-16 20:00', '%Y-%m-%d %H:%M'), 'hehe', 100, 10)

# Function to add room allocation
def addRoomAllocation():
    print('********************************************************')
    print('AVAILABLE ROOMS')
    for roomNumber, room in roomData.items():
            if room.status == RoomStatus.AVAILABLE:
                print(f'Room Number: {roomNumber} --- Type: {room.type}, Price: {room.price}, Status: {room.status}, Description: {room.description}')
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

# Function to display room allocations
def displayRoomAllocations():
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

# Function to save room allocation data
def saveRoomAllocationData():
    try:
        with open(roomAllocationFilePath, 'w') as f:
            for key, roomAllocation in roomAllocationData.items():
                f.write(f'Room Number: {key} --- Customer Name: {roomAllocation.customerName}, Check In Date: {roomAllocation.checkInDate}, Check Out Date: {roomAllocation.checkOutDate}, Description: {roomAllocation.description}')
            print(f'Room allocation data saved to {roomAllocationFilePath}')

        f.close()
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
    except FileNotFoundError as fileNotFoundErr:
        print("File Not Found Error:", fileNotFoundErr)
        return
    except Exception as err:
        print("An unexpected error occurred:", err)
        return

# Function to show room allocation data
def showRoomAllocationData():
    try:
        with open(roomAllocationFilePath, 'r') as f:
            print(f.read())
        f.close()
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
    except FileNotFoundError as fileNotFoundErr:
        print("File Not Found Error:", fileNotFoundErr)
        return
    except Exception as err:
        print("An unexpected error occurred:", err)
        return

# Function to backup room allocation data
def backupRoomAllocationData():
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
    except FileNotFoundError as fileNotFoundErr:
        print("File Not Found Error:", fileNotFoundErr)
        return
    except Exception as err:
        print("An unexpected error occurred:", err)
        return