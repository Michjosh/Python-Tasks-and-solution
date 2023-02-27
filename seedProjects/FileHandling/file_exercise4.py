import shutil

from seedProjects.FileHandling.file_exercise2 import file1, new_directory

# Delete the file file1.txt
# Delete the my_folder/ directory.

file1.unlink()
shutil.rmtree(new_directory)

print(file1.exists())
print(new_directory.exists())