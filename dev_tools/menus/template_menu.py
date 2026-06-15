def template_menu():
    while True:
        print("\n=== Template Menu ===")
        print("Available templates: None (Placeholder)")
        print("1. back")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "1":
            break
        else:
            print("\nInvalid choice.")