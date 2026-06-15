import subprocess


def run_create_branch():
    try:
        branches = subprocess.check_output(
            ["git", "branch"],
            text=True
        ).splitlines()

        existing_branches = []

        for branch in branches:
            branch_name = branch.replace("*", "").strip()
            existing_branches.append(branch_name)

        while True:
            branch_name = input(
                "\nEnter branch name or type 'exit': "
            ).strip()

            if branch_name.lower() == "exit":
                return

            if not branch_name:
                print(
                    "\nBranch name cannot be empty."
                )
                continue

            if " " in branch_name:
                print(
                    "\nBranch names cannot contain spaces."
                )
                continue

            if branch_name in existing_branches:
                print(
                    f"\nBranch '{branch_name}' already exists."
                )
                continue

            break

        print(
            f"\nCreating and switching to '{branch_name}'..."
        )

        subprocess.run(
            ["git", "switch", "-c", branch_name],
            check=True
        )

        print(
            f"\nCreated and switched to '{branch_name}'."
        )

    except subprocess.CalledProcessError as e:
        print(f"\nGit command failed: {e}")

    except FileNotFoundError:
        print("\nGit is not installed or not in PATH.")