Zippy-Archiver - README
Zippy-Archiver is a lightweight Python command-line tool designed as a foundational step toward creating a simplified zip software. Its primary function is to inventory and list the files you've placed in a dedicated /storage directory. This tool serves as an accessible starting point or educational resource for those interested in understanding the basic mechanics of file management within an archive-like system.

Key Features
File Scanning: Automatically scans the contents of the dedicated /storage folder.

User-Friendly Output: Presents discovered files in a clear, numbered list for easy reference.

Gentle Error Handling: Provides a clear warning if no files are found, guiding you to add items to the storage location.

Simple Python Script: The entire logic is contained within a straightforward Python file (main/zippy.py), making it very easy to study and modify. The project also includes test scripts to experiment with reading raw file data.

Installation
Follow these steps to get the project up and running on your local machine.

Clone the repository:

bash
git clone https://github.com/JoelRosehill/Zippy-archiver.git
Navigate to the project directory:

bash
cd Zippy-archiver
Usage
Using Zippy-Archiver is simple and involves just two steps: adding your files to storage and running the script.

Place your items in the /storage folder:
Before running the tool, add any files or folders you wish to include into the storage directory located in the project's root. A few placeholder files (example.png, test1.txt, test2.rtf) are already provided as examples.

⚠️ Note: The tool is currently a read-only inventory system and will not modify, compress, or archive your files in any way.

Run the run.py script:

bash
python run.py
Expected Output Scenarios:

If the /storage folder contains files, the tool will display a version identifier and a numbered list of the items, like so:

text
Version: test 1.0
Found these items in /storage folder:
-------------------------------------
example.png[1], test1.txt[2], test2.rtf[3]
If the /storage folder is empty, you will see this message:

text
Version: test 1.0
Found nothing in /storage folder, please add items to /storage folder and try again.
Exploring the Codebase
Beyond the main tool, the repository contains useful components to aid learning:

test/zip.py: This script demonstrates how to read a file in binary mode, a fundamental skill for any compression undertaking.

storage/example.png: A sample binary image file provided for you to test the functionality of the scripts.

Project Structure
text
Zippy-archiver/
├── main/             # Core application logic
│   ├── __pycache__/ # Python bytecode cache
│   └── zippy.py      # Main script for listing files
├── storage/          # Target directory for files to be listed
│   ├── example.png   # Sample image file
│   ├── test1.txt     # Placeholder text file
│   └── test2.rtf     # Placeholder RTF file
├── test/             # Test and learning scripts
│   └── zip.py        # Script for reading raw file data
└── run.py            # Entry point to execute the tool
