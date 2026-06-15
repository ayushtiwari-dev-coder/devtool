from dev_tools.creation_engine.creator_controller import (
    run_folder_mode,
    run_structure_mode
)

def structure_menu():
    menu_map = {
        "1": run_folder_mode,
        "2": run_structure_mode
    }
    while True:
        print("\n=== Structure Menu ===")
        print("1. folder")
        print("2. structure")
        print("3. back")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "3":
            break
            
        func = menu_map.get(choice)
        if func:
            func()
        else:
            print("\nInvalid choice.")