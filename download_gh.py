import urllib.request
import zipfile
import os
import shutil

URL = "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_windows_amd64.zip"
ZIP_NAME = "gh_cli.zip"
EXTRACT_DIR = "gh_temp"

print(f"Downloading {URL}...")
try:
    urllib.request.urlretrieve(URL, ZIP_NAME)
    print("Download complete.")

    print("Extracting...")
    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)
    
    # Find gh.exe in the extracted folders
    gh_path = None
    for root, dirs, files in os.walk(EXTRACT_DIR):
        if "gh.exe" in files:
            gh_path = os.path.join(root, "gh.exe")
            break
    
    if gh_path:
        print(f"Found gh.exe at {gh_path}")
        if os.path.exists("gh.exe"):
            os.remove("gh.exe")
        shutil.move(gh_path, "gh.exe")
        print("Moved gh.exe to current directory.")
    else:
        print("Could not find gh.exe in the zip.")

    # Cleanup
    print("Cleaning up...")
    os.remove(ZIP_NAME)
    shutil.rmtree(EXTRACT_DIR)
    print("Done!")

except Exception as e:
    print(f"Error: {e}")
