import os
import shutil

# Set your source folder where all your ReactJS videos are located
source_folder = "./"
# Set your destination base folder where you want new folders to be created
destination_base = "./daily_videos"

# Ensure that source folder exists
if not os.path.exists(source_folder):
    print("The source folder does not exist!")
    exit()

# Ensure that destination base folder exists
if not os.path.exists(destination_base):
    os.makedirs(destination_base)

# List all files and filter out non-video files if necessary
files = [
    f
    for f in sorted(os.listdir(source_folder))
    if f.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))
]

# Chunk files into groups of 5
chunks = [files[i : i + 5] for i in range(0, len(files), 5)]

# Loop through each chunk and move the files into new folders
for index, chunk in enumerate(chunks, start=1):
    # Create a folder for each chunk
    folder_name = (
        f"Day_{index:03d}"  # This will create folders named Day_001, Day_002, etc.
    )
    folder_path = os.path.join(destination_base, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Move each video into the current folder
    for filename in chunk:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(folder_path, filename)

        # Move the file
        shutil.move(source_path, destination_path)

    print(f"Moved {len(chunk)} videos to {folder_path}")

print("All videos have been sorted into folders!")
