import time
from tqdm import tqdm

def main():
    print("Loading...")
    for _ in tqdm(range(100), bar_format="{l_bar}{bar} {n_fmt}%"):
        time.sleep(0.03)
    print("Test")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
