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

    def change_bake(self):
        #change bake attributes before entering in bakery offer
        att_set = ""
        print("""
Choose what you want to change:
N (name)
K (kind)
T (taste)
A (additives)
F (filling)
    """)
        while True:
            print("Enter N, K, T, A or F")
            att_set = input("")
            if att_set == "N":
                self.name = input("New name:")
                break
            if att_set == "K":
                self.kind = input("New kind:")
                break
            if att_set == "T":
                self.taste = input("New taste:")
                break
            if att_set == "A":
                self.additives = input("New additives:")
                break
            if att_set == "F":
                self.filling = input("New filling:")
                break

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

    def add_bake_to_order():
        #displaying the names of the cakes and entering the cakes entered by the customer into the "order.txt" file

        bake_list = []

        #creating the file 'bakery_offer.txt' if it doesn't exist:
        current_dir = os.getcwd()
        filename = 'order.txt'
        fullpath = os.path.join(current_dir, filename)

        if os.path.isfile(fullpath):
            print(f'File {filename} exist')
        else:
            open(fullpath, 'x').close()
            print('File {filename} created')

        
        print ("Choose which cake to add to the order:")

        with open('bakery_offer.txt', 'r') as file:
            bakery_offer = file.readlines()
            for line in bakery_offer:
                if "Name" in line:
                    bake_list.append(line)
        for bake in bake_list:
            print(bake[14:-1])

        bake_to_add = input()

        for i in range(len(bake_list)):
            bake_list[i] = bake_list[i].lower()

        for b in bake_list:
            if bake_to_add.lower() in b:
                #saving data to a file:
                file = open(fullpath, 'a')
                file.write(b)
                file.write('\n')
                file.close()
                print(f'{b[14:]} added to order')
   
                    

    def browse_offer():
        #displaying the contents of the file "bakery_offer.txt"

        with open("bakery_offer.txt", "r") as file:
            bakery_offer = file.read()
            print(bakery_offer)
