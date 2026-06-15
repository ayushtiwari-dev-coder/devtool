from dev_tools.creation_engine.creator_structure import build_structure

def get_folder_name():
    return input("\nEnter folder name or type 'done': ").strip()

def get_file_names():
    files = []
    while True:
        file_name = input("\nEnter file name or type 'done': ").strip()
        
        if file_name.lower() == "done":
            break
            
        if not file_name:
            print("\nFile name cannot be empty.")
            continue
            
        files.append({
            "name": file_name
        })
        
    return files

def run_folder_mode():
    structure = {}
    while True:
        folder_name = get_folder_name()
        
        if folder_name.lower() == "done":
            break
            
        if not folder_name:
            print("\nFolder name cannot be empty.")
            continue
            
        # Add folder with empty list (no files)
        structure[folder_name] = []
        
    if not structure:
        print("\nNo folders provided.")
        return
        
    build_structure(structure)
    print("\nFolders created successfully.")

def run_structure_mode():
    structure = {}
    while True:
        folder_name = get_folder_name()
        
        if folder_name.lower() == "done":
            break
            
        if not folder_name:
            print("\nFolder name cannot be empty.")
            continue
            
        # Collect files for the specified folder
        files = get_file_names()
        structure[folder_name] = files
        
    if not structure:
        print("\nNo structure provided.")
        return
        
    build_structure(structure)
    print("\nStructure created successfully.")

def run_template_mode():
    # Placeholder for future template logic
    print("\n[Template Mode Placeholder]")
    print("- Choose template")
    print("- Enter destination folder name")
    print("- Enter destination file name if required")
    print("- Load template")
    print("- Call build_structure()")
    print("\nTemplate mode is not fully implemented yet.")