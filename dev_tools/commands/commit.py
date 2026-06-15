import subprocess
from pathlib import Path


def run_commit():
    try:
        print("new_version")
        # Repository name
        repo_path = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True
        ).strip()

        repo_name = Path(repo_path).name

        # Current branch
        branch = subprocess.check_output(
            ["git", "branch", "--show-current"],
            text=True
        ).strip()

        # Changed files
        changes = subprocess.check_output(
            ["git", "status", "--short"],
            text=True
        ).strip()

        print("\n" + "=" * 50)
        print(f"Repository : {repo_name}")
        print(f"Branch     : {branch}")
        print("=" * 50)

        if not changes:
            print("\nNo changes detected.")
            return

        print("\nChanged Files:\n")
        print(changes)

        continue_choice = input(
            "\nContinue with commit? (y/n): "
        ).strip().lower()

        if continue_choice != "y":
            print("\nCommit cancelled.")
            return

        commit_message = input(
            "\nEnter commit message: "
        ).strip()

        if not commit_message:
            print("\nCommit message cannot be empty.")
            return

        print("\nRunning git add .")
        subprocess.run(
            ["git", "add", "."],
            check=True
        )

        print("Running git commit")
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True
        )

        # Check if remote exists
        remote = subprocess.run(
            ["git", "remote"],
            capture_output=True,
            text=True
        )

        if not remote.stdout.strip():
            print(
                "\nCommit successful. No remote configured, skipping push."
            )
            return

        # Check if current branch has an upstream
        try:
            subprocess.check_output(
                [
                    "git",
                    "rev-parse",
                    "--abbrev-ref",
                    "--symbolic-full-name",
                    "@{u}"
                ],
                stderr=subprocess.DEVNULL,
                text=True
            )

            has_upstream = True

        except subprocess.CalledProcessError:
            has_upstream = False

        if has_upstream:
            print("Running git push")

            subprocess.run(
                ["git", "push"],
                check=True
            )

        else:
            print(
                f"First push detected for branch '{branch}'."
            )
            print(
                f"Running: git push -u origin {branch}"
            )

            subprocess.run(
                [
                    "git",
                    "push",
                    "-u",
                    "origin",
                    branch
                ],
                check=True
            )

        print("\nCommit and push successful.")

    except subprocess.CalledProcessError as e:
        print(f"\nGit command failed: {e}")

    except FileNotFoundError:
        print("\nGit is not installed or not in PATH.")