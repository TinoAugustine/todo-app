import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


# Use below to test this function within this Python file; this will only run if the file is executed directly
if __name__ == "__main__":
    make_archive(filepaths=["Bonus1.py", "Bonus2.py"], dest_dir="Dest")

