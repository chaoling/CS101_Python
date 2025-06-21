# Bradley Burris
rooms = {
'Home Stadium': {'up': 'Division', 'down': 'Champions', 'left': 'Underdogs',
'item': None},
'Division': {'down': 'Home Stadium', 'item': 'Batting Gloves'},
'Champions': {'right': 'Heroes', 'up': 'Home Stadium', 'item': 'Helmet'},
'Heroes': {'up': 'Rivals', 'left': 'Champions', 'item': 'Cleats'},
'Rivals': {'down': 'Heroes', 'item': 'Pitcher!'},
'Underdogs': {'right': 'Home Stadium', 'left': 'Contenders', 'item': 'Glove'},
'Contenders': {'right': 'Underdogs', 'down': 'Dynastys', 'item': 'Bat'},
'Dynastys': {'up': 'Contenders', 'item': 'Hat'}
}
def move(current_room, direction):
    """Move to a different room if possible."""
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    return None

def main():
    current_room = 'Home Stadium'
    inventory = []
    required_items_to_win = 6
    print("Welcome to your MLB Journey!")
    print("Collect 6 items to win the game, or be struck out by the Pitcher.")
    print("Move commands: go Up, go Down, go Left, go Right")
    print("Add to Inventory: get 'item name'\n")
    while True:
        print(f"You are in the {current_room}")
        print(f"Inventory: {inventory}")
        item = rooms[current_room].get('item')
        if item and item != 'Dragon' and item not in inventory:
            print(f"You see a {item}")
        if item == 'Pitcher!':
            print("\nSTRIKE THREE!...GAME OVER! You have been struck out by the Pitcher!")
            print("Thanks for playing.")
            break
        if len(inventory) == required_items_to_win:
            print("\nCongratulations! You've collected all the items and made it to the MLB!")
            break
        command = input("\nEnter your move: ").strip().lower()
        if command == 'exit':
            print("Thank you for playing.")
            break
        elif command.startswith("go "):
            direction = command[3:].lower()
            next_room = move(current_room, direction)
            if next_room:
                current_room = next_room
            else:
                print("You can't go that way!")
        elif command.startswith("get "):
            item_name = command[4:].capitalize()
            if item and item.lower() == item_name.lower() and item not in inventory:
                inventory.append(item)
                print(f"{item} retrieved!")
                rooms[current_room]['item'] = None
            else:
                print(f"Can't get {item_name}!")

if __name__ == "__main__":
    main()