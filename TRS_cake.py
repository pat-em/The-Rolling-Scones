class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

    def __init__(self, name, kind, taste, additives, filling):
            self.name = name
            self.kind = kind if kind in self.known_types else "other"
            self.taste = taste
            self.additives = additives
            self.filling = filling
    
def create_bake():
    nb_name = input("Name of the new bake: ")
    nb_kind = input("Kind: ")
    nb_taste = input("Taste: ")
    nb_additives = input("Additives: ")
    nb_filling = input("Filling: ")
    new_bake = Cake(nb_name, nb_kind, nb_taste, nb_additives, nb_filling)
    print("New bake:")
    print(f"""
    Name: {new_bake.name}
    Kind: {new_bake.kind}
    Taste: {new_bake.taste}
    Additives: {new_bake.additives}
    Filling: {new_bake.filling}
    Do you want to save the bake? (Y/N)""")
    answer = input("")
    if answer.upper() == "Y":
         save_bake(new_bake)

    
def save_bake():
    print("Saving the bake....")
    #TO DO: Create a file with the bakery offer and write a function that saves new cakes there
