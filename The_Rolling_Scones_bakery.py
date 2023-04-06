import TRS_cake as cake


#---    user profile selection  ---
print("""Choose a profile:
1. Bakery worker
2. Customer""")

user_profile = ""

while user_profile != "1" or user_profile != "2":
    print("Select 1 or 2:")
    user_profile = input()
    if user_profile == "1":
        user_profile = "Bakery worker"
        print("Bakery worker profile")
        break
    if user_profile == "2":
        user_profile = "Customer"
        print("Customer profile")
        break

#---    main loop   ---

while True:

# selecting a user profile:
    if user_profile == "Bakery worker":
        print("""Choose what you want to do:
        1. Create a new bake
        2. Remove the bake from the offer
        """)
        action = ""
        while action != "1" or action != "2":
            print("Select 1 or 2:")
            action = input()
            if action == "1":
                action = "Create bake"
                print("Create a new bake")
                break
            if action == "2":
                action = "Remove bake"
                print("Remove the bake from the offer")
                break

    if user_profile == "Customer":
        print("""Choose what you want to do:
        1. Submit your order
        2. Browse the offer
        3. Browse favorites""")

# actions for the user Bakery worker:
    if action == "Create bake":
        new_bake_name = input("Name of the new bake: ")
        naw_bake_kind = input("Kind: ")
        new_bake_taste = input("Taste: ")
        new_bake_additives = input("Additives: ")
        new_bake_filling = input("Filling: ")
        new_bake = cake.Cake(new_bake_name, naw_bake_kind, new_bake_taste, new_bake_additives, new_bake_filling)
        
        
        answer = ""
        while True:
            print("Do you want to save the bake?")
            answer = input("")
            if answer.upper() == "Y":
                cake.Cake.save_bake(new_bake)
                break
            if answer.upper() == "N":
                bake_answer = ""
                print("""
Do you want to change the data or delete all entered data?
enter "C" for data change
enter "D" to clear all inputs""")
                while True:
                    bake_answer = input("")
                    if bake_answer.upper() == "C":
                        cake.Cake.change_bake(new_bake)
                        break
                    if bake_answer.upper() == "D":
                        print("Changes have not been saved.")
                        break 
                    else:
                        print("Select C(change) or D(delete).")                 
            else:
                print("Select Y(yes) or N(not).")

    if action == "Remove bake":
        print("Enter the name of the cake you want to delete")
        bake_to_remove = input()
        cake.Cake.remove_bake(bake_to_remove)

# actions for the user Bakery worker:
    if action == "Submit your order":
        pass

    if action == "Browse the offer":
        pass

    if action == "Browse favorites":
        pass  

    
# ask the user to continue
    print("Do you want to terminate the program? (Y/N)")
    if input("").upper().startswith("Y"):
        break