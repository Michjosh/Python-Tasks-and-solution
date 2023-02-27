from pathlib import Path
# Create a new directory in your home folder called my_folder
file_path = Path.home() / "my_folder"

file_path.mkdir(exist_ok=True)

print(file_path.exists())

print(file_path.name)

print(file_path.parent.name)