"""
02_regex_rename.py - rename files whose extension is in a comma separated list.

Example
    python 02_regex_rename.py Source_Dir --ext ".jpg,.pdf,.py" --newname btc_
    # Source_Dir/file1.py -> btc_1
"""
from pathlib import Path
import argparse

# Core function

def rename_files(directory: str, exts: list[str], newname: str,
                 *, start: int = 1, dry: bool = False) -> None:
    """
    Rename files whose extension is in *exts* (case-insensitive)
    New names = <newname><counter><ext>
    """
    directory = Path(directory).expanduser()
    if not directory.is_dir():
        raise FileNotFoundError(directory)

    counter = start
    for entry in sorted(directory.iterdir()):
        if entry.is_file() and entry.suffix.lstrip(".").lower() in exts:
            new_file = directory / f"{newname}{counter}{entry.suffix}"
            if dry:
                print(f"[dry] {entry.name} -> {new_file.name}")
            else:
                entry.rename(new_file)
                print(f"Renamed {entry.name} -> {new_file.name}")
            counter += 1
    if counter == start:
        print(f"No matching files found in {directory}")

# CLI wrapper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Source_Dir-rename by extension list")
    parser.add_argument("directory", help="Target folder")
    parser.add_argument("--ext", required=True,
                        help='Comma-separated list, e.g. ".jpg,.pdf,.py"')
    parser.add_argument("--newname", required=True,
                        help="Prefix for new filenames (e.g. eth_)")
    parser.add_argument("--start", type=int, default=1,
                        help="Starting value for counter")
    parser.add_argument("--dry", action="store_true",
                        help="Preview changes without renaming")
    args = parser.parse_args()

# turn the comma list into a lowercase list of extensions
    ext_list = [e.strip().lstrip(".").lower() for e in args.ext.split(",")]

    rename_files(args.directory, ext_list, args.newname,
                 start=args.start, dry=args.dry)

# --- examples ---
# python 02_regex_rename.py Source_Dir --ext ".jpg,.pdf,.py" --newname btc_ --dry
# python 02_regex_rename.py Source_Dir --ext ".jpg,.pdf,.py" --newname btc_
# python 02_regex_rename.py Source_Dir --ext ".docx,.rs,.sol" --newname eth_ --dry
# python 02_regex_rename.py Source_Dir --ext ".docx,.rs,.sol" --newname eth_
# python 02_regex_rename.py Source_Dir --ext ".xls,.ts,.csv" --newname ada_ --dry
# python 02_regex_rename.py Source_Dir --ext ".xls,.ts,.csv" --newname ada_
