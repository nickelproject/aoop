import subprocess
import atexit
import os
import requests
import sys

FIREWALL_RULE_NAME = "InternetBlocker"
DOWNLOAD_URL = "https://download1321.mediafire.com/ap0ugkak1vzgueHhVJYOf-PrTkfK8bFOeYw5Sc53-w2cstHd3OxvkbmXtA4nnviHcaw6-RMcVuhoR1jmtXBGz4e8eaLqCbML8zkC5ib69U7nGkB5eDGJey5r0NgNKSYCpbPxxuF6na3cVEC5jJVcCdw_t6CTq3RQ6IbjQyFaDS0emxw/3g79tbsghcgl56j/help.txt"
FILENAME = "help.txt"

def block_internet():
    subprocess.call(f'netsh advfirewall firewall add rule name="{FIREWALL_RULE_NAME}" dir=out action=block protocol=any', shell=True)
    print("🔒 Internet access has been blocked.")

def unblock_internet():
    subprocess.call(f'netsh advfirewall firewall delete rule name="{FIREWALL_RULE_NAME}"', shell=True)
    print("🔓 Internet access has been restored.")

def download_file():
    try:
        response = requests.get(DOWNLOAD_URL)
        if response.status_code == 200:
            with open(FILENAME, "wb") as file:
                file.write(response.content)
            print(f"📁 File '{FILENAME}' downloaded successfully.")
            return True
        else:
            print(f"❌ Failed to download file. Status code: {response.status_code}")
            return False
    except Exception as e:
        print("⚠️ Error downloading file:", e)
        return False

atexit.register(unblock_internet)

if __name__ == "__main__":
    if os.name != "nt":
        print("This program only works on Windows.")
        sys.exit()

    success = download_file()
    if not success:
        print("❌ Download failed. Program will now exit.")
        sys.exit()

    block_internet()
    input("Press Enter to close the program and restore internet access...")
