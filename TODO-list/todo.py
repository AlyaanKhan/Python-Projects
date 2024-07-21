def to_do_list():
    print("Welcome to TO_DO_LIST")
    add_items = []
    while(True):
        choice = int(input(" Enter 1 to add item \n Enter 2 to remove item \n Enter 3 to view list \n Enter: "))
        if choice == 1:
            items = input("Enter Items to be added").split(',')
            add_items.extend(items)
            print(f"Item '{items}' added")
            print(" The new list is: ")
            print(add_items)
            use_again = input("Do you want to use again (Y/N) ").strip().upper()
            if use_again != 'Y':
                print("Thank you for using")
                return
        elif choice == 2:
            if len(add_items) == 0:
                print(" List is empty ")
            else:
                rem_items = input( "Enter items to be removed: ")
                for item in rem_items:
                    if item in add_items:
                        add_items.remove(item)
                        print(f"Item '{rem_items}' removed")
                        print(" The new list is: ")
                        print(add_items)
                        use_again = input("Do you want to use again (Y/N) ").strip().upper()
                        if use_again != 'Y':
                            print("Thank you for using")
                            return
                    else:
                        print("Error Occured")
        elif choice == 3:
            print(" The list is: \n", add_items)
            use_again = input("Do you want to use again (Y/N) ").strip().upper()
            if use_again != 'Y':
                print("Thank you for using")
                return
        else:
            print("Invalid Choice")
to_do_list()
