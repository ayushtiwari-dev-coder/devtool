from dev_tools.commands.commit import run_commit
from dev_tools.commands.switch import run_switch
from dev_tools.commands.create_branch import run_create_branch

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