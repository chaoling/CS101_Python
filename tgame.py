# Text Based Family Guy Game
# Matthew Duda
# Game setup
def show_instructions():
    # Display the instructions for the player
    print("Griffin Household Adventure Game")
    print("Collect all items to enter Chris's Room and defeat the evil monkey.")
    print("Move commands: go Forward, go Left, go Right, go Backwards")
    print("Collect items with command: get 'item name'")
    print()
# Rooms with possible directions and items
rooms = {
'Family Room': {'Forward': 'Kitchen', 'Right': 'Living Room', 'Left': 'Stewie’s Room', 'Backwards': 'Basement', 'item': None},
'Kitchen': {'Backwards': 'Family Room', 'item': "Meg's Hat"},
'Living Room': {'Left': 'Family Room', 'Forward': 'Garage', 'item': "Peter's Bird Record"},
'Garage': {'Backwards': 'Living Room', 'item': "Lois's Peloton Bike"},
'Chris’s Room': {'item': 'Evil Monkey'},
'Stewie’s Room': {'Right': 'Family Room', 'item': "Stewie's Teddy Bear"},
'Basement': {'Forward': 'Family Room', 'item': "Chris's Phone"}
}

# Game variables
current_room = 'Family Room'
inventory = []
can_enter_chris_room = False
# Function to display the player's current status
def show_status():
    # Display the player's current room and inventory status
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    item_in_room = rooms[current_room].get('item')
    if item_in_room:
        print(f"You see a {item_in_room}")
        print("--------------------------")
# Function to move between rooms
def move_between_rooms(direction):
    global current_room
    direction = direction.capitalize()
    # Check if the direction is valid for the current room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        # Check if the player can enter Chris's room
        if new_room == "Chris’s Room" and not can_enter_chris_room:
            print("You cannot enter Chris's Room yet! You need all items and Brian's Keys.")
        else:
            current_room = new_room
            print(f"You moved to the {current_room}.")
    else:
        print("Invalid direction! Try 'Forward', 'Left', 'Right', or 'Backwards'.")
# Function to get an item from the room
def get_item(item):
    item = item.capitalize()
    # Check if the item is in the current room and can be collected
    item_in_room = rooms[current_room].get('item')
    if item_in_room == item:
        inventory.append(item)
        print(f"{item} retrieved!")
    # Check if we can now enter Chris's Room
    if item == "Brian's Prius Keys" and len(inventory) == 5:
        global can_enter_chris_room
        can_enter_chris_room = True
        # Remove the item from the room
        rooms[current_room]['item'] = None
    else:
     print(f"Can't get {item}!")
# Main function to drive the game
def main():
    show_instructions()
    # Loop until the game ends
    while True:
        show_status()
        # Get the player's next move
        command = input("Enter your move: ").strip().lower()
        # Check if the command starts with "go" or "get"
        if command.startswith('go '):
            direction = command[3:].capitalize()
            move_between_rooms(direction)
        elif command.startswith('get '):
            item = command[4:].capitalize()
            get_item(item)
        else:
            # Win/loss conditions
            if current_room == "Chris’s Room":
                if can_enter_chris_room and "Evil Monkey" not in inventory:
                    print("Congratulations! You have collected all items and defeated the evil monkey!")
                break
            else:
                print("You encountered the evil monkey without all items. Game Over!")
                break
# Start the game
if __name__ == "__main__":
    main()