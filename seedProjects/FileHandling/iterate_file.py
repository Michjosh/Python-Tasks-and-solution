import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1/ "folder-a"
folder_a.mkdir(exist_ok=True)

file_paths = [
    folder_a/ "private.img", folder_a/ "lyrics.txt",
    folder_a/ "alone.vi", folder_a/ "inside.csv",
    folder_a/ "bible.txt", folder_a/ "looks.jpg"
]

# for path in file_paths:
#     path.touch()

# for file in folder_a.iterdir():
#     print(file.name)
# print(list(folder_a.iterdir()))

# for files in path1.glob("*.py"):
#     print(files.name)

# for files in folder_a.glob("*txt"):
#     print(files.name)

# for files in path1.rglob("*/*txt"):
#     print(files.name)


source = path1 / "bible.txt"
print(source.exists())
#
# destination = path1 /"my_folder" / "my_file.text"
#
# source.replace(destination)
#
# folder_a.rmdir()





