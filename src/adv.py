from room import Room
from player import Player
import textwrap
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item("bronchus","woof!"),Item("billting","rodondo?!")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("sword","sharp oh my!"),Item("boobrat","yo what dat?!")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item("sword","sharp oh my!"),Item("boobrat","yo what dat?!")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item("sword","sharp oh my!"),Item("boobrat","yo what dat?!")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Item("sword","sharp oh my!"),Item("boobrat","yo what dat?!")])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# room_link = {room['outside']:{"n":room['foyer']},
#             room['foyer']:{"s":room['outside'],"n":room['overlook'],"e":room['narrow']},
#             room['overlook']:{"s":room['foyer']},
#             room['narrow']:{"w":room['foyer'],"n":room['treasure']},
#             room['treasure']:{"s":room['narrow']}}


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


if __name__ == "__main__":

    p1 = Player(room['outside'])
    while True:
        print(p1.current_room)
        print("to see instructions, press h")
        lookup = input("What will it be? ").lower()
        if lookup == "q":
            break 
        elif lookup == "h":
            print("""
            In all rooms, you will be able to take the following actions:
            [n,s,e,w] - Cardinal direction options depend on room availability
            [i] - Look up what is in your inventory
            [r] - Look up what is in the room's inventory
            [p] - pick up item in room currenly not in your inventory
                [#] - pick up item by its number
            [d] - drop off item in room from your inventory
                [#] - drop off item by its number """)

        elif lookup == "i":
            p1.print_inventory()

        elif lookup == "r":
            p1.current_room.print_inventory()

        elif lookup == "p":
            item_id = input("which item do you want to pick up?")
            print(p1.current_room.items[int(item_id)].name,"picked up and removed from room")
            p1.get_item(p1.current_room.items[int(item_id)])
            # print(p1.items)
            p1.current_room.remove_item(p1.current_room.items[int(item_id)])
            
            
    
        # else:
        #     p1.travel(lookup)
