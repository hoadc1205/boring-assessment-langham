import sys
from room.room import addRoom, displayRooms, deleteRoom
from allocation.allocation import addRoomAllocation, displayRoomAllocations, roomDeallocation, saveRoomAllocationData, showRoomAllocationData, backupRoomAllocationData
from utility.helper import InputCommand, InputNumberOfRoom, InputDateTime, InputFloat


def main():
    # Menu
    print("********************************************************************************")
    print("                 LANGHAM HOTEL MANAGEMENT SYSTEM                  ")
    print("                            MENU                                 ")
    print("********************************************************************************")
    print("0. Exit")
    print("1. Add Rooms")
    print("2. Display Rooms")
    print("3. Delete Rooms")
    print("4. Allocate Rooms")
    print("5. Display Room Allocation Details")
    print("6. De-allocate Rooms and Billing")
    print("7. Save the Room Allocations To a File")
    print("8. Show the Room Allocations From a File")
    print("9. Backup")
    print("********************************************************************************")

    while True:
        # Get user input
        cmd = InputCommand("Enter Your Choice Number Here (0-9): ")

        match cmd:
            case '1':
                roomNumber = InputNumberOfRoom("Enter number of rooms to add (max=3): ")
                for i in range(roomNumber):
                    addRoom()
            case '2':
                displayRooms()
            case '3':
                deleteRoom()
            case '4':
                allocationNumber = InputNumberOfRoom("Enter number of allocations to add (max=3): ")
                for i in range(allocationNumber):
                    addRoomAllocation()    
            case '5':
                displayRoomAllocations()
            case '6':
                roomDeallocation()
            case '7':
                saveRoomAllocationData()
            case '8':
                showRoomAllocationData()
            case '9':
                backupRoomAllocationData()
            case '0':
                print("Goodbye!")
                sys.exit()
            case _:
                print("Invalid command")
            
# Main
if __name__ == "__main__":
    main()