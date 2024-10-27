
import subprocess
import platform
import tempfile
import os

def print_text(text):
    # Create a temporary text file for printing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as tmp_file:
        tmp_file.write(text)
        tmp_file_path = tmp_file.name

    # Determine platform and print the file
    try:
        system = platform.system()
        if system == "Windows":
            # Use Notepad to print on Windows
            subprocess.run(['notepad.exe', '/p', tmp_file_path])
        elif system == "Linux":
            # Use lp for Linux printing
            subprocess.run(['lp', tmp_file_path])
        elif system == "Darwin":  # macOS
            # Use lpr for macOS printing
            subprocess.run(['lpr', tmp_file_path])
        else:
            print(f"Printing is not supported on this platform: {system}")
    finally:
        # Clean up temporary file
        os.remove(tmp_file_path)
