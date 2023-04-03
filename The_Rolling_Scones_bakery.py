import TRS_cake as cake
#TO DO: creating a list of cakes, creating variables for the entered cakes and adding them to the list
#import globals
#   for i in range(100):
#       globals()[f"cake_{i+1}"] = cake.Cake(nb_name, nb_kind, nb_taste, nb_additives, nb_filling)


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

if user_profile == "Bakery worker":
    print("""Choose what you want to do:
    1. Create a new bake
    2. Change an existing bake
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
            action = "Change bake"
            print("Change bake")
            break

if user_profile == "Customer":
    print("""Choose what you want to do:
    1. Submit your order
    2. Browse the offer
    3. Browse favorites""")

if action == "Create bake":
    cake.create_bake()
