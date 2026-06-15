import sys

# Command imports for direct execution
from dev_tools.commands.commit import run_commit
from dev_tools.commands.switch import run_switch
from dev_tools.commands.create_branch import run_create_branch

from dev_tools.creation_engine.creator_controller import (
    run_folder_mode,
    run_structure_mode,
    run_template_mode
)

from dev_tools.utilities.bundler import run_bundle

# Interactive Menu import
from dev_tools.menus.main_menu import main_menu

# Command Map for direct CLI execution
COMMANDS = {
    "commit": run_commit,
    "switch": run_switch,
    "new-branch": run_create_branch,
    "folder": run_folder_mode,
    "structure": run_structure_mode,
    "template": run_template_mode,
    "bundle": run_bundle
}

def main():
    try:
        if len(sys.argv) < 2:
            main_menu()
            return

        command = sys.argv[1].lower()
        func = COMMANDS.get(command)
        
        if func:
            func()
        else:
            print(f"Unknown command: {command}")
            print("Available commands:", ", ".join(COMMANDS.keys()))
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled. Exiting DevTool...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[DevTool Error] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()