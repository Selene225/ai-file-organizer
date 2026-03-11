import os
import shutil

folder_path = input("Enter folder path:")
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        if filename.endswith(".jpg") or filename.endswith(".png"):
            category = "Images"

        elif filename.endswith(".pdf") or filename.endswith(".docx"):
            category = "Documents"

        elif filename.endswith(".py"):
            category = "Code"

        else:
            category = "Others"

        category_path = os.path.join(folder_path, category)

        if not os.path.exists(category_path):
            os.makedirs(category_path)

        print(f"Moving {filename} to {category} folder.")
        shutil.move(file_path, os.path.join(category_path, filename))

print("Files organized successfully!")