import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Scripts': ['.py', '.js', '.sh'],
    'Others': []
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'

def organize(folder_path):
    if not os.path.exists(folder_path):
        print("The folder does not exist.")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            category = get_category(file)
            category_folder = os.path.join(folder_path, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            shutil.move(full_path, os.path.join(category_folder, file))
            print(f"Moved: {file} -> {category}/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
else:
    folder_path = input("Enter the path of the folder to organize: ").strip()
    organize(folder_path)
