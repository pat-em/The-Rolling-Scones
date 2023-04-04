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

    if action == "Create bake":
        cake.create_bake()

    if action == "Remove bake":
        print("Enter the name of the cake you want to delete")
        bake_to_remove = input()
        cake.remove_bake(bake_to_remove)

    #ask the user to continue
    print("Do you want to terminate the program? (Y/N)")
    if input("").upper().startswith("Y"):
        break
