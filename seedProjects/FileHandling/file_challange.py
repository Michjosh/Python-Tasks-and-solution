from pathlib import Path

document_directory = Path.cwd() / "practice_file"

document_directory.mkdir()
print(document_directory.exists())

image1 = document_directory / "image1.png"
image2 = document_directory / "image2.gif"
image3 = document_directory / "image3.png"
image4 = document_directory / "image4.jpg"

image1.touch()
image2.touch()
image3.touch()
image4.touch()

print(image1.exists())
print(image2.exists())
print(image3.exists())
print(image4.exists())

images_folder = Path.home() / "images"
images_folder.mkdir(exist_ok=True)

print(images_folder.exists())

for path in document_directory .rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_folder / path.name)


