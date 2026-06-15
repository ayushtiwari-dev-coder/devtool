from dev_tools.creation_engine.creator_structure import (
    build_structure
)

structure = {
    "database": [
        {
            "name": "connection.py"
        },
        {
            "name": "sql_handler.py"
        }
    ],
    "routes": [
        {
            "name": "user_routes.py"
        }
    ]
}

build_structure(structure)