class Employee:
    def __init__(self, name, employe_id, salary, position):
        self.name = name
        self.employe_id = employe_id
        self.salary = salary
        self.position = position
    def get_details(self):
        return{
            'name': self.name,
            'employe_id': self.employe_id,
            'salary': self.salary,
            'position' : self.position
        }
    def update_position(self, latest_position):
        self.position = latest_position
    def update_salary(self, latest_salary):
        self.salary = latest_salary
def menu():
    added_employee = []
    while True:
        print("Menu")
        print(""" Press 1 to Add new employee
            Press 2 to Update employess position
            Press 3 to Update employees salary 
            Press 4 to View employees
            Press 5 to Exit """)
        choice = int(input("Enter your desired opertion (1, 2, 3, 4 and 5 (to exit))"))
        if choice == 1:
            name = input("Enter your name: ")
            employe_id = input(f"Enter {name}'s employee_id: ")
            salary = int(input(f"Enter {name}'s salary: "))
            position = input(f"Emter {name}'s position: ")
            storing_data = Employee(name, employe_id, salary, position)
            added_employee.append(storing_data)
            print("Employee has been added Succesfully!")
        elif choice == 2:
            employe_id = input("Enter the employe_id to update position: ")
            for e_id in added_employee:
                if e_id.employe_id == employe_id:
                    new_pos = input("Enter the new position: ")
                    e_id.update_position(new_pos)
                    print(f"The position for {employe_id} is updated to {new_pos}")
                    break
                else:
                    print(f"No employee found against {employe_id}")
        elif choice == 3:
            salary = input("Enter the employe_id to update salary: ")
            for e_id in added_employee:
                if e_id.employe_id == employe_id:
                    new_sal = int(input("Enter the new salary: "))
                    e_id.update_salary(new_sal)
                    print(f"The salary for {employe_id} is updated to {new_sal}")
                    break
                else:
                    print(f"No employee found against {employe_id}")
        elif choice == 4:
            if added_employee:
                for detail in added_employee:
                    print("Following are the employess: ")
                    print(detail.get_details())
            else:
                print("No data found! ")
        elif choice == 5:
            print("Exiting the System")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    menu()
