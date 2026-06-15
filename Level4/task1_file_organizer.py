# task1_file_organizer.py
import os
import shutil
from datetime import datetime

def organize_files(source_folder: str = "downloads"):
    """Automatically organize files based on their extensions."""
    if not os.path.exists(source_folder):
        print(f"📁 Creating sample folder: {source_folder}")
        os.makedirs(source_folder)
        # Create sample files
        sample_files = ["report.pdf", "photo.jpg", "notes.txt", "video.mp4", "data.csv"]
        for f in sample_files:
            with open(os.path.join(source_folder, f), 'w') as _:
                pass
    
    categories = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav'],
        'Others': []
    }
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in categories.items():
                if ext in extensions:
                    dest_folder = os.path.join(source_folder, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"✅ Moved: {filename} → {category}/")
                    moved = True
                    break
            
            if not moved:
                dest_folder = os.path.join(source_folder, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"✅ Moved: {filename} → Others/")
    
    print(f"\n🎉 File organization completed in '{source_folder}' folder!")

if __name__ == "__main__":
    print("📂 Automatic File Organizer")
    print("=" * 50)
    folder = input("Enter folder path to organize (default: downloads): ").strip()
    organize_files(folder or "downloads")