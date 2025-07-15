import os
import shutil
import pathlib
from pathlib import Path
path = r"C:\Users\harsh\OneDrive\Desktop\Dummy"
# path = input("Enter the folder path: ")

folder = {
    "pdf": "PDFs",
    "txt": "Text_Files",
    "jpg": "Images",
    "png": "png_Images",
    "docx": "Word_Documents",
    "xlsx": "Excel_Spreadsheets",
    "pptx": "PowerPoint_Presentations",
    "mp3": "Audio_Files",
    "pub" : "Publisher_Files",
}
for file in os.listdir(path):
    file_path = Path(path)/file
    if file_path.is_file():
        suffix = file_path.suffix.lower().strip('.')
        for key in folder.keys():
            if suffix == key:
                destination_folder = Path(path) / folder[key]
                destination_folder.mkdir(exist_ok=True)
                shutil.move(file_path, destination_folder / file)
                print(f"Moved {file} to {destination_folder}")