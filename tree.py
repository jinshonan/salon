# this is used to  print the file directory

import os

def generate_tree(directory, prefix=""):
    # List all items in the directory, excluding hidden files/folders
    items = [item for item in os.listdir(directory) if not item.startswith('.')]
    items.sort()  # Sort for consistent output

    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        # Check if it's the last item in the list
        if i == len(items) - 1:
            print(f"{prefix}└── {item}")
            new_prefix = prefix + "    "
        else:
            print(f"{prefix}├── {item}")
            new_prefix = prefix + "│   "

        # Recursively print the contents of directories
        if os.path.isdir(path):
            generate_tree(path, new_prefix)

if __name__ == "__main__":
    generate_tree(".")