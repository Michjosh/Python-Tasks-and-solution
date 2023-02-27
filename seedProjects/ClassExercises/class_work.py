from pathlib import Path


def empty_list():
    list_of_something = []
    my_directory = Path.home() / "new_folder"
    # my_directory.mkdir()

    my_file = my_directory / "my_file.txt"
    my_file.touch()

    my_file.write_text("I am a good man I know")
    names = my_file.read_text()

    for i in names:
        list_of_something.append(i)

    return list_of_something


print(empty_list())
