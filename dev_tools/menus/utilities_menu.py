from dev_tools.utilities.bundler import run_bundle

def utilities_menu():
    menu_map = {
        "1": run_bundle
    }
    while True:
        print("\n=== Utilities Menu ===")
        print("1. bundle")
        print("2. back")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "2":
            break
            
        func = menu_map.get(choice)
        if func:
            func()
        else:
            print("\nInvalid choice.")