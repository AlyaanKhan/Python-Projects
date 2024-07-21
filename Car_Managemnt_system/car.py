class CarDetails:
    def __init__(self, car_name, car_id, car_condition, car_color, car_price):
        self.car_name = car_name
        self.car_id = car_id
        self.car_condition = car_condition
        self.car_color = car_color
        self.car_price = car_price
    def car_information(self):
        return {
            'Car_Name': self.car_name,
            'Car_Id': self.car_id,
            'Car_condition': self.car_condition,
            'Car_Color': self.car_color,
            'Car_Price': self.car_price
        }
    def updated_price(self, updateprice):
        self.car_price = updateprice
def saving_car_details():
    car_details = []
    output = 'Car_details.txt'
    while True:
        choice = int(input("Press 1 for Add car or 2 for Update car price and 3 to exit"))
        if choice == 1:
            car_name = input("Enter Car name: ")
            car_id = input(f"Enter {car_name} identification number: ")
            car_con = []
            while True:
                line = input("Enter Car condition:")
                if line.strip() == "":
                    break
                car_con.append(line)
            car_condition = "\n".join(car_con)
            car_color = input(f"Enter {car_name} color: ")
            car_price = int(input(f"Enter {car_name} price: "))
            details = CarDetails(car_name, car_id, car_condition, car_color, car_price)
            car_details.append(details)
            with open (output, 'w') as file:
                for car in car_details:
                    file.write(str(car.car_information()) + "\n")
            print("File Created successfully!")
        elif choice == 2:
            car_id = input("Enter id of car to update Price")
            for c_id in car_details:
                if c_id.car_id == car_id:
                    new_price = int(input("Enter the new Price: "))
                    c_id.updated_price(new_price)
                    print("The Price updated succesfully! ") 
                    with open (output, 'w') as file:
                        file.write(str(new_price))
                    print("File Updated Succesfully!")
                else:
                    print(f"No car found against {car_id}")                   
        elif choice == 3:
            print("Exiting.......")
            print("Exit with success!")
            break
        else:
            print("Invalid Input!")
if __name__ == "__main__":
    saving_car_details()
