print("""Choose a profile:
1. Bakery worker
2. Customer""")

user_profile = ""

while user_profile != "1" or user_profile != "2":
    print("Select 1 or 2:")
    user_profile = input()
    if user_profile == "1":
        user_profile == "Bakery worker"
        print("Bakery worker profile")
        break
    if user_profile == "2":
        user_profile == "Customer"
        print("Customer profile")
        break
