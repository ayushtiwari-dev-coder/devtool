from pathlib import Path


def create_file(
    folder_name,
    file_name,
    content=""
):
    file_path = Path(folder_name) / file_name

    file_path.touch(
        exist_ok=True
    )

    if content:
        file_path.write_text(
            content,
            encoding="utf-8"
        )

    return file_path