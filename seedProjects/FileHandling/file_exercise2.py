from pathlib import Path

# Inside my_folder/ create three files:

new_directory = Path.home() / "my_folder"
new_directory.mkdir()


file1 = new_directory / "file1.txt"
file2 = new_directory / "file2.txt"
image1 = new_directory / "image1.png"

file1.touch()
file2.touch()
image1.touch()

print(file1.exists())
print(file2.exists())
print(image1.exists())

