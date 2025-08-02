import subprocess
import atexit
import os
import requests
import sys
import ctypes
import time
from tqdm import tqdm

FIREWALL_RULE_NAME = "InternetBlocker"
DOWNLOAD_URL = "https://download1321.mediafire.com/1twuj0i88m1gKW2r56Dc_gbDGTkXGVnRk1Cdvz_SUZnoIHLxl0X7RuWZo6Agra_89wpFwL18NmZ2pjeNhv8_ct3Afg4BjS3p4_3sFrTOmxZZwkIdejuPq3LRgVdDk8zVfena6JFBcnzvywq5CYr8d7bjVbhzGCMpLXYPtpdAlnI4KXo/3g79tbsghcgl56j/help.txt"
FILENAME = "help.txt"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_internet():
    subprocess.call(f'netsh advfirewall firewall add rule name="{FIREWALL_RULE_NAME}" dir=out action=block protocol=any', shell=True)
    print("🔒 Internet access has been blocked.")

def unblock_internet():
    subprocess.call(f'netsh advfirewall firewall delete rule name="{FIREWALL_RULE_NAME}"', shell=True)
    print("🔓 Internet access has been restored.")

def download_file():
    try:
        response = requests.get(DOWNLOAD_URL, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        t = tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading")
        with open(FILENAME, "wb") as f:
            for data in response.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        if total_size != 0 and t.n != total_size:
            print("❌ ERROR, something went wrong while downloading")
            return False
        print(f"📁 File '{FILENAME}' downloaded successfully.")
        return True
    except Exception as e:
        print("⚠️ Error downloading file:", e)
        return False

def loading_bar():
    print("📦 Transitioning to the new version...")
    for i in tqdm(range(101), desc="Progress"):
        time.sleep(0.03)

atexit.register(unblock_internet)

if __name__ == "__main__":
    if os.name != "nt":
        print("This program only works on Windows.")
        sys.exit()

    if not is_admin():
        print("🚫 Please run this program as Administrator.")
        input("Press Enter to exit...")
        sys.exit()

    loading_bar()

    success = download_file()
    if not success:
        print("❌ Download failed. Program will now exit.")
        input("Press Enter to exit...")
        sys.exit()

    block_internet()
    input("Press Enter to close the program and restore internet access...")
