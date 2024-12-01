import datetime
from utility.constant import RoomType, RoomStatus

# Check input command
def InputCommand(inputString):
    while True: 
        string = input(inputString)
        try:
            if len(string) == 0:
                raise ValueError('Command invalid')
            newInteger = int(string)
            if newInteger < 0 or newInteger > 9:
                raise ValueError('Command invalid')
            else:
                return string
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input number of room
def InputNumberOfRoom(inputString):
    while True: 
        string = input(inputString)
        try:
            if len(string) == 0:
                raise ValueError('Number of room cannot be empty')
            newInteger = int(string)
            if newInteger > 3:
                newInteger = 3
            return newInteger
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input price
def InputFloat(inputString):
    while True: 
        string = input(inputString)
        try:
            if len(string) == 0:
                raise ValueError('Price cannot be empty')
            newFloat = float(string)
            if newFloat <= 0:
                raise ValueError('Price must be greater than 0')
            return newFloat
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input datetime
def InputDateTime(inputString):
    while True: 
        string = input(inputString)
        # check checkin time is greater than check out time and current time

        try:
            if len(string) == 0:
                raise ValueError('Datetime cannot be empty')
            newDateTime = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M')
            return newDateTime
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input check in and check out time
def InputCheckInOutDate(checkinString, checkoutString):
    while True:
        try:
            if len(checkinString) == 0 or len(checkoutString) == 0:
                raise ValueError('Check in and check out time cannot be empty')
            checkinTime = input(checkinString)
            checkin = datetime.datetime.strptime(checkinTime, '%Y-%m-%d %H:%M')
            checkoutTime = input(checkoutString)
            checkout = datetime.datetime.strptime(checkoutTime, '%Y-%m-%d %H:%M')

            if checkin < datetime.datetime.now():
                raise ValueError('Check in time must be greater than current time')
            if checkout <= checkin:
                raise ValueError('Check out time must be greater than check in time')

            return checkin, checkout
    
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

#     Check input room number
def InputRoomNumber(inputString):
    while True: 
        string = input(inputString)
        try:
            if len(string) != 3 and len(string) != 4:
                raise ValueError('Room number must be 3 or 4 characters long')
            else:
                return string
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input room type
def InputRoomType(inputString):
    while True: 
        string = input(inputString)
        try:
            if string not in [RoomType.SINGLE, RoomType.DOUBLE, RoomType.SUITE]:
                return RoomType.SINGLE
            else: 
                return string
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)

# Check input room status
def InputRoomStatus(inputString):
    while True: 
        string = input(inputString)
        try:
            if string not in [RoomStatus.AVAILABLE, RoomStatus.OCCUPIED, RoomStatus.UNAVAILABLE]:
                raise ValueError('Room status must be Available, Occupied, or Unavailable')
            else: 
                return string
        except TypeError as typeErr:
            print("Type Error:", typeErr)
        except ValueError as valueErr:
            print('Value Error: ', valueErr)
        except AttributeError as attributeErr:
            print("Attribute Error:", attributeErr)
        except NameError as nameErr:
            print("Name Error:", nameErr)
        except KeyError as keyErr:
            print("Key Error:", keyErr)
        except Exception as err:
            print("An unexpected error occurred:", err)