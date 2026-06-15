import os
from pathlib import Path


IGNORED_DIRS = {
    
    "node_modules", ".next", "dist", "build", "out", "coverage",
    
    "__pycache__", "venv", "env", ".venv", ".tox", ".pytest_cache", ".ruff_cache",
    
    "target", "bin", "obj",
    
    ".git", ".vscode", ".idea", ".svn", ".DS_Store"
}

IGNORED_EXTENSIONS = {
    
    ".pyc", ".pyo", ".pyd",
    
    ".o", ".out", ".exe", ".dll", ".so", ".dylib", ".class",
    
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".mp4", ".pdf", ".zip", ".tar", ".gz"
}

IGNORED_FILES = {
    
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock"
}

def run_bundle():
    print("\n=== Bundle Project Context ===")
    
    # 1. Get extensions
    ext_input = input("Enter file extensions to bundle (e.g., .py, .js, .cpp) or type 'all': ").strip().lower()
    
    if not ext_input:
        print("\nOperation cancelled: No extensions provided.")
        return

    requested_extensions = set()
    if ext_input != "all":
        # Parse and format extensions (ensure they start with a dot)
        raw_exts = [e.strip() for e in ext_input.split(",")]
        for ext in raw_exts:
            if not ext.startswith("."):
                ext = "." + ext
            requested_extensions.add(ext)

    # 2. Get output file name
    out_name = input("Enter output file name [default: project_context.txt]: ").strip()
    if not out_name:
        out_name = "project_context.txt"
        
    output_path = Path(out_name).resolve()

    print(f"\nBundling files into '{out_name}'...")
    
    bundled_count = 0
    
    try:
        with open(output_path, "w", encoding="utf-8") as outfile:
            for root, dirs, files in os.walk("."):
                # Modify dirs in-place to completely skip ignored directories
                dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
                
                for file in files:
                    # Skip completely ignored files (like locks)
                    if file in IGNORED_FILES:
                        continue
                        
                    path = Path(root) / file
                    
                    # Skip ignored extensions
                    if path.suffix.lower() in IGNORED_EXTENSIONS:
                        continue
                        
                    # Filter by requested extensions
                    if ext_input != "all" and path.suffix.lower() not in requested_extensions:
                        continue
                        
                    # Prevent bundling the output file into itself!
                    if path.resolve() == output_path:
                        continue
                        
                    # Try to read and write the file
                    try:
                        content = path.read_text(encoding="utf-8")
                        
                        # Add a clear header for each file
                        relative_path = path.relative_to(".")
                        outfile.write(f"{'=' * 60}\n")
                        outfile.write(f"FILE: {relative_path}\n")
                        outfile.write(f"{'=' * 60}\n\n")
                        outfile.write(content)
                        outfile.write("\n\n")
                        
                        bundled_count += 1
                    except UnicodeDecodeError:
                        # Silently skip binary files that slipped through the extension check
                        continue
                        
        print(f"\nBundle complete! Gathered {bundled_count} files into {out_name}.")
        
    except Exception as e:
        print(f"\nAn error occurred while bundling: {e}")