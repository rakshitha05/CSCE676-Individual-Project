import os
import gzip
import shutil
import urllib.request
from pathlib import Path

DATA_URL = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
RAW_GZ_PATH = Path("data") / "facebook_combined.txt.gz"
DATA_PATH = Path("data") / "facebook_combined.txt"

def main():
    os.makedirs("data", exist_ok=True)

    if not RAW_GZ_PATH.exists():
        print(f"Downloading {DATA_URL}")
        urllib.request.urlretrieve(DATA_URL, RAW_GZ_PATH)

    if not DATA_PATH.exists():
        print(f"Extracting to {DATA_PATH}")
        with gzip.open(RAW_GZ_PATH, "rb") as f_in:
            with open(DATA_PATH, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    print("Dataset ready.")

if __name__ == "__main__":
    main()
