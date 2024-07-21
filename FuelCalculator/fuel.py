def petrol_station():
    petrol = 269.66
    diesel = 277.45
    cng = 190
    type_of_fuel = input("Enter the type of fuel:").strip().upper()
    if type_of_fuel == 'PETROL':
        liters = int(input("Enter the amount (in liters) of fuel:"))
        total_price_petrol = liters * petrol
        print("You have filled up", liters , "liters petrol")
        print("The total cost is:", "RS.", total_price_petrol)
    elif type_of_fuel == 'DIESEL':
        liters = int(input("Enter the amount (in liters) of fuel:"))
        total_price_diesel = liters * diesel
        print("You have filled up", liters , "liters diesel")
        print("The total cost is:", "RS.", total_price_diesel)
    elif type_of_fuel == 'CNG':
        liters = int(input("Enter the amount (in liters) of cng:"))
        total_price_cng = liters * cng
        print("You have filled up", liters , "liters cng")
        print("The total cost is:", "RS.", total_price_cng)
    else:
        print("Invalid Input")
petrol_station()
