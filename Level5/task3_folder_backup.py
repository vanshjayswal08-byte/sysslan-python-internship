# task3_folder_backup.py
import shutil
import os
from datetime import datetime

def create_backup(source_folder: str, backup_folder: str = "backups"):
    """Create timestamped backup of a folder."""
    if not os.path.exists(source_folder):
        print(f"❌ Source folder '{source_folder}' not found!")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(source_folder)}_backup_{timestamp}"
    backup_path = os.path.join(backup_folder, backup_name)
    
    os.makedirs(backup_folder, exist_ok=True)
    
    try:
        shutil.copytree(source_folder, backup_path)
        print(f"✅ Backup created successfully!")
        print(f"📍 Location: {backup_path}")
        print(f"📦 Size: {sum(os.path.getsize(os.path.join(root, f)) for root, _, files in os.walk(backup_path) for f in files) / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def main():
    print("💾 Automated Folder Backup Tool")
    print("=" * 50)
    
    source = input("Enter folder path to backup (default: Level_4): ").strip() or "Level_4"
    create_backup(source)

if __name__ == "__main__":
    main()