import subprocess
import atexit
import os

FIREWALL_RULE_NAME = "InternetBlocker"

def block_internet():
    subprocess.call(f'netsh advfirewall firewall add rule name="{FIREWALL_RULE_NAME}" dir=out action=block protocol=any', shell=True)
    print("🔒 Internet access has been blocked.")

def unblock_internet():
    subprocess.call(f'netsh advfirewall firewall delete rule name="{FIREWALL_RULE_NAME}"', shell=True)
    print("🔓 Internet access has been restored.")

atexit.register(unblock_internet)

if __name__ == "__main__":
    if os.name != "nt":
        print("This program only works on Windows.")
        exit()

    block_internet()
    input("Press Enter to close the program and restore internet access...")
