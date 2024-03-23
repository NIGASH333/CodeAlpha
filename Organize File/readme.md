# File Organization Script
![Screenshot (13)](https://github.com/NIGASH333/CodeAlpha/assets/113447646/f04ca057-43dd-4dc0-ab99-6d964b9d855d)



![Screenshot (14)](https://github.com/NIGASH333/CodeAlpha/assets/113447646/e1b4ce55-a1f8-4065-aac5-4ce3103823fc)



![Screenshot (15)](https://github.com/NIGASH333/CodeAlpha/assets/113447646/b26f6162-4ec1-4c3d-905c-abba1ae4b1f1)



This Python script helps organize files within a specified directory based on their file extensions. It categorizes files into different folders according to their types, such as images, documents, videos, audios, archives, executables, scripts, and others.

## How It Works

1. **Run the script**: Execute the Python script to start organizing files.

2. **Enter directory path**: Provide the directory path where the files to be organized are located.

3. **File Organization**: The script scans the specified directory, identifies files, and moves them into respective folders based on their file extensions.

4. **Output**: During the process, the script prints messages indicating the files being moved and their destination folders.

## File Categories

- **Images**: Files with extensions `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`.
- **Documents**: Files with extensions `.doc`, `.docx`, `.pdf`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`.
- **Videos**: Files with extensions `.mp4`, `.avi`, `.mkv`, `.mov`, `.flv`.
- **Audios**: Files with extensions `.mp3`, `.wav`, `.ogg`, `.flac`.
- **Archives**: Files with extensions `.zip`, `.rar`, `.tar`, `.gz`.
- **Executables**: Files with extensions `.exe`, `.msi`.
- **Scripts**: Files with extensions `.py`, `.sh`, `.bat`.
- **Others**: Default folder for files with unknown extensions.

## Dependencies

- Python 3.x

## Usage Example

Suppose you have a directory named `Documents` containing various files. Running the script within this directory will organize the files into respective folders based on their types.

```bash
python organize_files.py

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
