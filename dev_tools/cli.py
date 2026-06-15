import sys

from dev_tools.commands.commit import run_commit
from dev_tools.commands.switch import run_switch
from dev_tools.commands.create_branch import run_create_branch

from dev_tools.creation_engine.creator_controller import (
    run_folder_mode,
    run_structure_mode,
    run_template_mode
)

# Command Map for direct CLI execution
COMMANDS = {
    "commit": run_commit,
    "switch": run_switch,
    "new-branch": run_create_branch,
    "folder": run_folder_mode,
    "structure": run_structure_mode,
    "template": run_template_mode
}

# --- Interactive Menus ---

def git_menu():
    menu_map = {
        "1": run_commit,
        "2": run_switch,
        "3": run_create_branch
    }
    while True:
        print("\n=== Git Menu ===")
        print("1. commit")
        print("2. switch")
        print("3. new-branch")
        print("4. back")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "4":
            break
            
        func = menu_map.get(choice)
        if func:
            func()
        else:
            print("\nInvalid choice.")

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

def main_menu():
    menu_map = {
        "1": git_menu,
        "2": structure_menu,
        "3": template_menu
    }
    while True:
        print("\n=== Main Menu ===")
        print("1. Git Commands")
        print("2. Structure")
        print("3. Templates")
        print("4. Exit")
        
        choice = input("\nSelect an option: ").strip()
        if choice == "4":
            print("\nExiting DevTool.")
            break
            
        func = menu_map.get(choice)
        if func:
            func()
        else:
            print("\nInvalid choice.")

# --- Main Entry Point ---

def main():
    # If no arguments provided, launch the interactive menu
    if len(sys.argv) < 2:
        main_menu()
        return

    # Direct command execution
    command = sys.argv[1].lower()
    func = COMMANDS.get(command)
    
    if func:
        func()
    else:
        print(f"Unknown command: {command}")
        print("Available commands:", ", ".join(COMMANDS.keys()))

if __name__ == "__main__":
    main()