# Joe Irvine


class colors:  # Class to add color to text
    bold = "\033[01m"
    disable = "\033[02m"
    green = "\033[92m"
    yellow = "\033[93m"
    cyan = "\033[96m"
    reset = "\033[0m"


# Define functions to be used in the game.


def instructions():  # Function to print game instructions
    print(
        f"You're objective is to navigate all the rooms collecting{colors.bold}{colors.yellow} all 6 chapters{colors.reset} of the Necronomicon"
    )
    print("You must have a complete book before confronting the evil spirit in the basement")
    print(f"You can move {colors.bold}{colors.green}North, South, East, or West{colors.reset} to the next room")
    print("Type the direction you want to move in")
    print(f"Type {colors.bold}{colors.green}get{colors.reset} to pick up an item")
    print(f"Type {colors.bold}{colors.green}help{colors.reset} to see these instructions again")
    print(f"Type {colors.bold}{colors.green}look{colors.reset} to print and describe the current room")


def print_location(dict):  # Function to print the current room
    global current_items  # Access global variable
    directions = []  # Create list to store directions
    for key, value in dict.items():
        if key == current_room:
            for k, v in dict[current_room].items():
                if k == "North" or k == "South" or k == "East" or k == "West":
                    directions.append(k)
            string = dict[current_room]["desc"]
            print(f"{string}\n")
            # Check if there are items in the room and if they have already been picked up
            if dict[current_room]["items"] not in current_items and dict[current_room]["items"] != "none":
                print(f"You see a stack of papers in the room\n")
    # Print directions you can move from the current room
    directions = " ".join(directions)
    print(f"You can move {colors.bold}{colors.green}{directions}{colors.reset}")
    print(f"-------------------")


def get_item(dict):  # Function to add items to inventory
    global current_items  # Access global variable
    # check if there are items in the room and if they have already been picked up
    if dict[current_room]["items"] != "none" and dict[current_room]["items"] not in current_items:
        print(
            f'{colors.bold}{colors.yellow}{dict[current_room]["items"]}{colors.reset} has been added to your inventory'
        )
        current_items.append(dict[current_room]["items"])
    else:
        print("There are no items in this room")


def game_status_check():  # Function to check game status each time a move is made
    global game_status  # Access global variable
    if current_room == "Basement":  # If cunrrent room is the basement check if player has all chapters
        if len(current_items) == 6:
            print(f"Congraulations! You win")
            game_status = "n"
            return False
        else:
            print(f"You were devoured by the evil spirit")
            print(f"Game Over")
            return False
    else:
        return True


def command(cmd, rooms):  # Function to add additional commands to gameplay
    # Access global variables
    global game_status
    global current_items
    if cmd.lower() == "help":  # print instructions
        instructions()
    if cmd.lower() == "look":  # print what room you're in
        print_location(rooms)
    if cmd.lower() == "quit":  # exit game
        game_status = "n"
    if cmd.lower() == "inventory":  # print inventory
        current_items.sort()
        print(
            f"You currently have {colors.green}{len(current_items)}{colors.reset} of {colors.yellow}6{colors.reset} chapters"
        )
        print(f"{colors.yellow}{current_items}{colors.reset}")
        print(f"-------------------")
    if cmd.lower() == "get":  # get item in room and add to inventory
        get_item(rooms)
        print(f"-------------------")


current_items = []  # Initialize inventory list
current_room = "Main Hall"  # Set starting room
commands = [
    "Help",
    "Look",
    "Get",
    "Quit",
    "Inventory",
]  # A list with additional commands for the command to check against
game_status = "n"  # Set initial game status


def main():  # Main function to run game
    # Access global variables
    global game_status
    global current_items
    global current_room
    # Print welcome message and ask if player wants to play
    print("\nWelcome Forest Hills Manor.\n")
    print(
        "The only way to escape to this house is to collect all chapters of the Necronomimcon before you face the evil spirit."
    )
    print(f"{colors.bold}{colors.cyan}Do you want to play?{colors.green} (y/n){colors.reset}")

    game_status = input()
    # Check input and start game or exit
    if game_status == "y":
        print(f"Let's begin. You're currently in {colors.bold}{colors.green}{current_room}{colors.reset}")
        print(f"Type {colors.yellow}{colors.bold}Help{colors.reset} for instructions at any time")
        print(f"-------------------")
    elif game_status == "n":
        print("Goodbye")
        return False
    else:
        print("Invalid input. Goodbye")

    ## Setup dictionary of rooms and the directions you can move from each room. Each room also contains a item to be picked up and description of room.
    rooms = {
        "Main Hall": {
            "South": "Dining Room",
            "East": "Parlor Room",
            "North": "Guest Bedroom",
            "items": "none",
            "desc": "A large open hall with very little furniture.",
        },
        "Guest Bedroom": {
            "South": "Main Hall",
            "East": "Master Bedroom",
            "items": "Chapter 2",
            "desc": "A small bedroom with two twin sized beds that have mattresses missing. There's a wooden cabinent in the corner that is still full of childrens clothes.",
        },
        "Master Bedroom": {
            "West": "Guest Bedroom",
            "East": "Balcony",
            "items": "Chapter 6",
            "desc": "A large bedroom with a king sized bed. There is a large chandlier covered in cobwebs.",
        },
        "Balcony": {
            "West": "Master Bedroom",
            "items": "none",
            "desc": "A small dilapidated balcony with a view of the forest",
        },
        "Parlor Room": {
            "East": "Library",
            "West": "Main Hall",
            "items": "Chapter 3",
            "desc": "There's a pool table missing one leg and several old slot machines lined against the wall",
        },
        "Library": {
            "West": "Parlor Room",
            "items": "Chapter 5",
            "desc": "What once have been a great library is not just a room with empty selves and a few books on the floor",
        },
        "Dining Room": {
            "North": "Main Hall",
            "East": "Kitchen",
            "items": "Chapter 1",
            "desc": "A large dining room with a long table and a few chairs. There is a large painting of a family on the wall",
        },
        "Kitchen": {
            "West": "Dining Room",
            "East": "Basement",
            "items": "Chapter 4",
            "desc": "A large kitchen with a large stove and several cabinets. There is a large hole in the floor with a ladder leading down",
        },
        "Basement": {
            "West": "Kitchen",
            "items": "none",
            "desc": "A large basement with a large hole in the floor. There is a large shadow in the corner of the room",
        },
    }
    while (
        game_status == "y" and game_status_check()
    ):  # While game status is "y" and game status check is true, continue game
        direction = str(input(f"{colors.bold}{colors.cyan}What do you want to do? {colors.reset}"))  # Get user input
        keys = rooms[current_room].keys()
        if direction.capitalize() in commands:
            command(direction, rooms)
        else:
            for index, key in enumerate(keys):
                if direction.capitalize() == key:  # Check if direction is in keys
                    current_room = rooms[current_room][key]
                    print(f"You are in the {colors.bold}{colors.green}{current_room}{colors.reset}")
                    print(f"-------------------")
                    break
                elif (
                    direction.capitalize() != key and index < len(keys) - 1
                ):  # If direction is not in keys and index is less than length of keys minus 1, continue
                    continue
                else:
                    print("Invalid Input")


main()
