import os
import shutil

# Paths
SOURCE_FOLDER = "All_Problems"
DESTINATION_FOLDER = "."  # Root where script is located

# Function to extract tags from file
def extract_tags(filepath):
    tags = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#Tags:"):
                tag_line = line.strip().split(":")[1]
                tags = [tag.strip().replace(" ", "_") for tag in tag_line.split(",")]
                break
    return tags

# Function to create README.md in the folder
def create_readme(folder_path, tag_name):
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f"# {tag_name.replace('_', ' ')} Problems\n\n")
        f.write(f"This folder contains solutions related to **{tag_name.replace('_', ' ')}** problems.\n")

# Main Organizer Function
def organize_files():
    for filename in os.listdir(SOURCE_FOLDER):
        if filename.endswith(".py"):
            filepath = os.path.join(SOURCE_FOLDER, filename)
            tags = extract_tags(filepath)
            
            for tag in tags:
                target_dir = os.path.join(DESTINATION_FOLDER, tag)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    create_readme(target_dir, tag)  # Create README when new folder created
                
                shutil.copy(filepath, os.path.join(target_dir, filename))

    print("✅ All files organized successfully!")

if __name__ == "__main__":
    organize_files()
