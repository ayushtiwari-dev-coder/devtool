import subprocess


def run_switch():
    try:
        branches = subprocess.check_output(
            ["git", "branch"],
            text=True
        ).splitlines()

        clean_branches = []
        current_branch = None

        print("\nAvailable Branches:\n")

        for index, branch in enumerate(branches, start=1):
            branch_name = branch.replace("*", "").strip()

            clean_branches.append(branch_name)

            if "*" in branch:
                current_branch = branch_name

            current = " (current)" if "*" in branch else ""

            print(f"{index}. {branch_name}{current}")

        if not clean_branches:
            print("\nNo branches found.")
            return

        while True:
            choice = input(
                "\nSelect branch number or type 'exit': "
            ).strip().lower()

            if choice == "exit":
                return

            if not choice.isdigit():
                print("\nInvalid selection.")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(clean_branches):
                print("\nInvalid selection.")
                continue

            selected_branch = clean_branches[choice - 1]

            if selected_branch == current_branch:
                print(
                    "\nYou are already on that branch."
                )
                continue

            break

        print(
            f"\nSwitching to '{selected_branch}'..."
        )

        subprocess.run(
            ["git", "switch", selected_branch],
            check=True
        )

        print(
            f"\nNow on branch '{selected_branch}'."
        )

    except subprocess.CalledProcessError as e:
        print(f"\nGit command failed: {e}")

    except FileNotFoundError:
        print("\nGit is not installed or not in PATH.")