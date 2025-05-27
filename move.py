import os
import shutil

source_dir = r'c:\Users\Vinscent Joshua\Documents\GitHub\MusicStore\AlbumArts\vjdyofficialmusic-2023'
dest_dir = r'c:\Users\Vinscent Joshua\Documents\GitHub\MusicStore\AlbumArts\vjdyofficialmusic-2023'

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Move all .jpg and .png files
for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.jpg', '.png')):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(dest_dir, filename)
        shutil.move(src_path, dst_path)  # Use shutil.copy() if you want to copy instead of move
        print(f"Moved: {filename}")