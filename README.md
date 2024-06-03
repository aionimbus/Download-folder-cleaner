# Download-folder-cleaner
Folder Cleaner This Python script organizes files in the Downloads folder into designated subfolders based on their file types. It helps to maintain a clean and organized Downloads directory by automatically categorizing and moving files into appropriate directories.

Features Automatic Directory Creation: Creates target directories if they don't already exist.
File Type Classification: Categorizes files based on their extensions into predefined categories such as Audio, Compressed, Code, Documents, Images, Softwares, Videos, and Other.
File Skipping: Skips moving files that already exist in the destination directory to avoid conflicts.
Customizable Categories: Easily update the script to add more file types and categories as needed.

Directory Structure Base Directory: ~/Downloads

Target Directories: Audio Compressed Code Documents Images Softwares Videos Fonts Other

File Types The script currently supports the following file types for each category:

Audio: .aif, .cda, .mid, .midi, .mp3, .mpa, .ogg, .wav, .wma, .m4a Compressed: .7z, .deb, .pkg, .rar, .rpm, .tar.gz, .z, .zip, .dmg Code: .js, .jsp, .html, .ipynb, .py, .java, .css, .py, .c, .cpp Documents: .ppt, .pptx, .pdf, .xls, .xlsx, .doc, .docx, .txt, .tex, .epub Images: .bmp, .gif, .ico, .jpeg, .jpg, .png, .jfif, .svg, .tif, .tiff, .arw, .cr2, .nef, .raf, .psd, .webp, .heic Softwares: .apk, .bat, .bin, .exe, .jar, .msi Videos: .3gp, .avi, .flv, .h264, .mkv, .mov, .mp4, .mpg, .mpeg, .wmv, .mmv, .m2t, .m2ts, .wmv Fonts: .ttf, .otf Usage Clone the Repository:

git clone https://github.com/aionimbus/gpt-folder-cleaner.git cd gpt-folder-cleaner

Run the Script:

python3 gptfoldercleaner.py How It Works Define Directories: The script first defines the base Downloads directory and target subdirectories. Create Directories: It creates these directories if they don't already exist. Categorize Files: The script categorizes each file in the Downloads folder based on its extension. Move Files: It moves the files to their respective directories, skipping files that already exist in the destination.
