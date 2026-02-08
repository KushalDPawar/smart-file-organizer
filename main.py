import os
import shutil

def get_unique_filename(folder, filename):
    name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{name}_{counter}{extension}"
        counter += 1

    return new_filename


# 🔹 CATEGORY MAPPING
CATEGORIES = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "docx", "txt", "xlsx"],
    "Code": ["py", "c", "cpp", "java"]
}


FOLDER_PATH = input("Enter the folder path to organize: ")

if not os.path.exists(FOLDER_PATH):
    print("❌ Folder does not exist.")
    exit()


for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    name, extension = os.path.splitext(filename)
    extension = extension[1:].lower()

    if extension == "":
        print(f"Skipped (no extension): {filename}")
        continue

    # 🔹 Decide category
    category = "Others"
    for folder_name, extensions in CATEGORIES.items():
        if extension in extensions:
            category = folder_name
            break

    category_folder = os.path.join(FOLDER_PATH, category)

    if not os.path.exists(category_folder):
        os.mkdir(category_folder)
        print(f"Created folder: {category}")

    unique_filename = get_unique_filename(category_folder, filename)
    destination_path = os.path.join(category_folder, unique_filename)

    shutil.move(file_path, destination_path)
    print(f"Moved: {filename} → {category}/{unique_filename}")

print("\n✅ Files organized successfully!")
