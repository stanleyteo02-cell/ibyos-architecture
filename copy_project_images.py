import shutil
from pathlib import Path

base = Path(r"c:\Users\Edw\Downloads\startbootstrap-creative-gh-pages\startbootstrap-creative-gh-pages")
source_map = {
    "villa-panbil": Path(r"c:\Users\Edw\OneDrive\Pictures\PANBIL"),
    "wellness-village": Path(r"c:\Users\Edw\OneDrive\Pictures\Wellness"),
    "yafindo-showunit": Path(r"c:\Users\Edw\OneDrive\Pictures\Showunit"),
}

for folder, src in source_map.items():
    dest = base / "assets" / "img" / "portfolio" / folder
    dest.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        print(f"Missing source folder: {src}")
        continue
    files = list(src.glob("*.*"))
    print(f"Copying {len(files)} images for {folder}")
    for file in files:
        if file.is_file():
            shutil.copy2(file, dest / file.name)
print("done")
