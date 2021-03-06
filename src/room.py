# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self,name,description,items=[]):
        self.name = name
        self.description = description 
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        # return_string = "---------"
        return_string = "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += f"{self.get_exits_string()}"
        return return_string
    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def print_inventory(self):
        print("---------")
        print("The room contains the following:")
        for index,item in enumerate(self.items): 
            print(index)
            print(item)
            print("---------")

    def add_items(self,item):
        pass

    def remove_item(self,item):
        self.items.remove(item)