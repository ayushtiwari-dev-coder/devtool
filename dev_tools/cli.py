import sys
from dev_tools.commands.commit import run_commit

def main():
    if len(sys.argv) < 2:
        print("Usage: devtool <command>")
        return

    command = sys.argv[1]

    if command == "commit":
        run_commit()
    else:
        print(f"Unknown command: {command}")