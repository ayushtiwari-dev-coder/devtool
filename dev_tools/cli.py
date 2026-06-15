import sys

from dev_tools.commands.commit import run_commit
from dev_tools.commands.switch import run_switch
from dev_tools.commands.create_branch import run_create_branch

COMMANDS = {
    "commit": run_commit,
    "switch":run_switch,
    "new-branch":run_create_branch,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: devtool <command>")
        return

    command = sys.argv[1].lower()

    func = COMMANDS.get(command)

    if func:
        func()
    else:
        print(f"Unknown command: {command}")