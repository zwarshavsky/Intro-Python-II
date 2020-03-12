from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room_link = {room['outside']:{"n":room['foyer']},
            room['foyer']:{"s":room['outside'],"n":room['overlook'],"e":room['narrow']},
            room['overlook']:{"s":room['foyer']},
            room['narrow']:{"w":room['foyer'],"n":room['treasure']},
            room['treasure']:{"s":room['narrow']}}


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
        print("\n Current Room Name: ",p1.current_room.name,"\n")
        print("\n Current Room Description: \n")
        my_wrap = textwrap.TextWrapper(width = 40) 
        wrap_list = my_wrap.wrap(text=p1.current_room.description)
        for line in wrap_list:
            print(line)
        print("\n")
        new_direction = input("Where do you want to go? ").lower()
        if new_direction == "q":
            break 
        else:
            try:
                p1.current_room = room_link[p1.current_room][new_direction]
            except:
                print(f"{p1.current_room.name} is the furthest you can go in the {new_direction} direction. Try again!")