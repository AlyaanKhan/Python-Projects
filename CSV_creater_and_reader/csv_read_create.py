import pandas as pd
details = []
while True:
    choice = int(input("Enter your choice: (1 to create CSV and 2 to read CSV): "))
    if choice == 1:
        while True:
            name = input("Enter your name (or 'done' to stop): ")
            if name.lower() == 'done':
                print("Thank you!")
                break
            age = int(input(f"Enter your age, {name}: "))
            phone_no = input(f"Enter your phone number, {name}: ")
            email = input(f"Enter your email, {name}: ")
            if age <= 0:
                print("Age cannot be zero or negative.")
                continue
            details.append({'Name': name, 'Age': age, 'Phone': phone_no, 'Email': email})
            csv_data = pd.DataFrame(details)
            csv_data.to_csv('user_details.csv', index=False)
            print("The file was created successfully.") 
    elif choice == 2:
        try:
            read_csv_file = pd.read_csv('user_details.csv')
            print(read_csv_file)
        except FileNotFoundError:
            print("The file does not EXISTS. Please create the CSV file first.")
    else:
        print("Invalid input. Please enter 1 or 2.")
    ask = input("Do you want to use the program again? (Y/N): ").strip().upper()
    if ask != 'Y':
        print("Thank you!")
        break
