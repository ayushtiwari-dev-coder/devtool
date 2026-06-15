from pathlib import Path


def create_folder(folder_name):
    folder_path = Path(folder_name)

    folder_path.mkdir(
        parents=True,
        exist_ok=True
    )

    return folder_path