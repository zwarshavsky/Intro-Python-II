
class Item:
    def __init__ (self,name,description):
        self.name = name
        self.description = description
    def __str__(self):
        # return_string = "\n"
        # return_string += "---------"
        # return_string = "\n"
        return_string = self.name
        return_string += "\n"
        return_string += self.description
        return return_string