
from seedProjects.FileHandling.file_exercise2 import new_directory, image1

images_directory = new_directory / "images"
images_directory.mkdir()

# Move the file image1.png to a new directory called images/
# inside  my_folder/ directory.

image1.replace(images_directory / "image1.png")

print(images_directory.exists())
print(image1.exists())