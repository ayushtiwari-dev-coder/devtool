import subprocess


def run_commit():
    try:
        print("\n=== Git Status ===\n")

        subprocess.run(
            ["git", "status"],
            check=True
        )

        commit_message = input(
            "\nEnter commit message: "
        ).strip()

        if not commit_message:
            print("Commit message cannot be empty.")
            return

        print("\nRunning git add .")
        subprocess.run(
            ["git", "add", "."],
            check=True
        )

        print("\nRunning git commit")
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True
        )

        print("\nRunning git push")
        subprocess.run(
            ["git", "push"],
            check=True
        )

        print("\nCommit successful.")

    except subprocess.CalledProcessError:
        print("\nGit command failed.")
    #wwww
    except FileNotFoundError:
        print("\nGit is not installed or not in PATH.")