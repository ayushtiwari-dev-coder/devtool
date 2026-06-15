from dev_tools.menus.git_menu import git_menu
from dev_tools.menus.structure_menu import structure_menu
from dev_tools.menus.template_menu import template_menu
from dev_tools.menus.utilities_menu import utilities_menu

def main_menu():
    menu_map = {
        "1": git_menu,
        "2": structure_menu,
        "3": template_menu,
        "4": utilities_menu
    }
    while True:
        print("\n=== Main Menu ===")
        print("1. Git Commands")
        print("2. Structure")
        print("3. Templates")
        print("4. Utilities")
        print("5. Exit")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "5":
            print("\nExiting DevTool.")
            break
            
        func = menu_map.get(choice)
        if func:
            func()
        else:
            print("\nInvalid choice.")