from dev_tools.creation_engine.creator_folder import (
    create_folder
)

from dev_tools.creation_engine.creator_file import (
    create_file
)


def build_structure(structure):
    for folder_name, files in structure.items():

        create_folder(folder_name)

        for file_data in files:

            create_file(
                folder_name,
                file_data["name"],
                file_data.get(
                    "content",
                    ""
                )
            )