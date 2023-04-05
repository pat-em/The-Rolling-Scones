import os


class Cake:
    
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

    def __init__(self, name, kind, taste, additives, filling):
            self.name = name
            self.kind = kind if kind in self.known_types else "other"
            self.taste = taste
            self.additives = additives
            self.filling = filling
    
    def save_bake(self):
        #saving a new bake in file bakery_offer.txt

        print("Saving the bake....")
        current_dir = os.getcwd()
        filename = 'bakery_offer.txt'
        fullpath = os.path.join(current_dir, filename)

        #creating the file 'bakery_offer.txt' if it doesn't exist:
        if os.path.isfile(fullpath):
            print(f'File {filename} exist')
            print(f'Path: {fullpath}')
        else:
            print('Creating a file {filename}h')
            open(fullpath, 'x').close()
            print('File {filename} created')

        #saving data to a file:
        file = open(fullpath, 'a')
        file.write(f"""
        Name: {self.name}
        Kind: {self.kind}
        Taste: {self.taste}
        Additives: {self.additives}
        Filling: {self.filling}
        """)
        file.close()
 
    def remove_bake(bake):
        #remove bake with given name from file
        
        with open("bakery_offer.txt", "r") as prev_file, open('new_offer.txt', 'w') as new_file:
            lines = prev_file.readlines()
            for x, line in enumerate(lines):
                if bake in line:
                    first_line_to_del = x

        #deleting the line with the name of the baking and the next 5 lines:
            no_of_line = 0
            for line in lines:
                if first_line_to_del:
                    if no_of_line != first_line_to_del and no_of_line != first_line_to_del+1 and no_of_line != first_line_to_del+2 and no_of_line != first_line_to_del+3 and no_of_line != first_line_to_del+4 and no_of_line != first_line_to_del+5:
                        new_file.write(line)
                else:
                    new_file.write(line)
                no_of_line+=1

        os.remove('bakery_offer.txt')
        os.rename('new_offer.txt', 'bakery_offer.txt')