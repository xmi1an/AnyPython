# Video Organizer Script

## Overview
The `organize_videos.py` script is a simple Python utility designed to help you sort a large collection of video files into individual folders, with each folder containing a fixed number of videos.

This is particularly useful if you have a series of instructional or educational videos, that you want to watch in daily increments.

## Features
- Automatically sorts video files into sequentially numbered folders.
- Each folder can contain a pre-defined number of videos (default is set to 5).
- Supports common video file formats such as .mp4, .avi, .mkv, and .mov.

## Prerequisites
To use this script, you need:
- Python 3.x installed on your system.
- Videos must be named in a way that allows proper sorting (e.g., numerically or alphabetically).

## Usage
1. Clone or download this repository to your local machine.
2. Place the `organize_videos.py` script in a directory of your choice.
3. Open the script in a text editor, and set the `source_folder` variable to the path where your videos are currently stored.
4. Set the `destination_base` variable to the path where you want the new folders containing sorted videos to be created.
5. Save the changes to the script.
6. Open a terminal or command prompt.
7. Navigate to the directory where you saved the `organize_videos.py` script.
8. Run the script by typing `python organize_videos.py` and pressing Enter.

## Customization
If you want to change the number of videos per folder or support additional file types, you can modify the script as follows:
- To change the number of videos per folder, modify the `chunk` size in the list comprehension.
- To support additional video formats, add the desired file extensions to the `files` list filter condition.

## Disclaimer
This script moves files from the source folder to the destination folders. It is recommended to back up your videos before running the script to prevent any accidental data loss.

## License
This script is provided "as is" without any warranty of any kind, either expressed or implied. Feel free to use and modify it as you need for your personal purposes.
