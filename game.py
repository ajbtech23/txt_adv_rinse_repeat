def get_user_action():
    return input("\nWhat would you like to do Sailor?\n> ")

def play():

    arr_inventory = ['Dagger', 'Gold(5)', 'Berries', 'Cloak']
    user_player_is_active = True

    while user_player_is_active:

        user_action = get_user_action()

        if user_action in ['q', 'Q', 'quit', 'Quit', 'exit', 'Exit']:
            print("Travel safe... for these be treacherous waters...")
            user_player_is_active = False
        elif user_action in ['n', 'N', 'north', 'North', '^']:
            print("You are travelling North!")
        elif user_action in ['e', 'E', 'east', 'East', '>']:
            print("You are travelling East")
        elif user_action in ['s', 'S', 'south', 'South', 'v']:
            print("You are travelling South")
        elif user_action in ['w', 'W', 'west', 'West', '<']:
            print("You are travelling West")
        elif user_action in ['i', 'I', 'inventory', 'Inventory']:
            print(f"\nYou have access to the following items in your inventory:\n")
            i = 0
            for item in arr_inventory:
                print(f"{i + 1}. {item}")
                i += 1
        else:
            print("Try again Sailor...")

play()
