class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

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
    print(new_bake.name)