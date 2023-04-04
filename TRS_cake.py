import os

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

    
def save_bake(new_bake):
    print("Saving the bake....")
    
    current_dir = os.getcwd()
    filename = 'bakery_offer.txt'
    fullpath = os.path.join(current_dir, filename)

    #creating the file 'bakery_offer.txt' if it doesn't exist
    if os.path.isfile(fullpath):
        print(f'File {filename} exist')
        print(f'Path: {fullpath}')
    else:
        print('Creating a file {filename}h')
        open(fullpath, 'x').close()
        print('File {filename} created')

    file = open(fullpath, 'a')
    file.write(f"""
    Name: {new_bake.name}
    Kind: {new_bake.kind}
    Taste: {new_bake.taste}
    Additives: {new_bake.additives}
    Filling: {new_bake.filling}
    """)
    file.close()

    
def remove_bake(bake):
     
    with open("bakery_offer.txt", "r") as prev_file, open('new_offer.txt', 'w') as new_file:
        lines = prev_file.readlines()
        for x, line in enumerate(lines):
            if bake in line:
                first_line_to_del = x

        no_of_line = 0
        for line in lines:
            if no_of_line != first_line_to_del and no_of_line != first_line_to_del+1 and no_of_line != first_line_to_del+2 and no_of_line != first_line_to_del+3 and no_of_line != first_line_to_del+4 and no_of_line != first_line_to_del+5:
                new_file.write(line)
            no_of_line+=1

    os.remove('bakery_offer.txt')
    os.rename('new_offer.txt', 'bakery_offer.txt')



        

        
                

                
    
    # file = open('bakery_offer.txt', 'r+')
    # new_file = file.readlines()
    # file.seek(0)
    # for line in new_file:
    #      if bake not in line:
    #           file.write(line)
    # file.truncate()
    # file.close()