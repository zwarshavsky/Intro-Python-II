# # Write a class to hold player information, e.g. what room they are in
# # currently.

class Player:
    def __init__ (self,current_room,items=[]):
        self.current_room = current_room
        self.items = items
    
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    
    def print_inventory(self):
        print("---------")
        print("You own the following items:")
        for index,item in enumerate(self.items): 
            print(index)
            print(item)
            print("---------")
    
    def get_item(self,new_item):
        self.items.append(new_item)

    def drop_item(self,old_item):
        self.items.remove(old_item)

    def add_item_to_room(self,existing_item):
        self.current_room.items.append(existing_item)



