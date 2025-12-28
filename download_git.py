import urllib.request
import zipfile
import os
import shutil

# MinGit is a portable, minimal distribution of Git for Windows
URL = "https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/MinGit-2.47.1-64-bit.zip"
ZIP_NAME = "mingit.zip"
EXTRACT_DIR = "git_temp"

print(f"Downloading {URL}...")
try:
    urllib.request.urlretrieve(URL, ZIP_NAME)
    print("Download complete.")

    print("Extracting...")
    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)
    
    print("Git extracted to git_temp")

    # Cleanup
    if os.path.exists(ZIP_NAME):
        os.remove(ZIP_NAME)
    print("Done!")

except Exception as e:
    print(f"Error: {e}")
