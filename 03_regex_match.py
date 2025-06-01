"""
03_regex_match.py
Move every file whose base name matches a regex, (case insensitive),
into a destination directory and rewrite the matching base names.
"""

from pathlib import Path
import argparse
import re

def move_matches(src_dir: str,
                 dest_dir: str,
                 pattern: str = r"eth",
                 replace: str | None = None,
                 *,
                 dry: bool = False) -> None:
    """
    Move all files whose base name matches `pattern`
    into `dest_dir`, and implement a new file name, (case insensitive).

    Parameters
    src_dir  : source directory (must exist)
    dest_dir : destination directory (create if missing)
    pattern  : regex pattern; default 'eth'
    replace  : replacement text applied to matched pattern
    dry      : if True, only preview what would be moved
    """
    src =  Path(src_dir).expanduser()
    dest = Path(dest_dir).expanduser()
    regex = re.compile(pattern, flags=re.IGNORECASE)

    if not src.is_dir():
        raise FileNotFoundError(src)
    dest.mkdir(parents=True, exist_ok=True)

    moved = 0
    for entry in src.iterdir():
        if not entry.is_file():
            continue
        if not regex.search(entry.stem):
            continue
        if replace is None:
            new_stem = entry.stem
        else:
            new_stem = regex.sub(replace, entry.stem, count=1)
        new_name = f"{new_stem}{entry.suffix}"
        target   = dest / new_name

        if dry:
            print(f"[dry] {entry.name} -> {new_name}")
        else:
            entry.rename(target)
            print(f"Moved {entry.name} -> {new_name}")
        moved += 1

    if moved == 0:
        print(f"No files matching /{pattern}/ found in {src}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Move files whose name matches a regex and rewrite that part")
    p.add_argument("source",        help="Source directory")
    p.add_argument("destination",   help="Destination directory (create if missing)")
    p.add_argument("--pattern", default="eth",
                   help="Regex to match (default: 'eth')")
    p.add_argument("--replace",
                   help="Replacement text for the matched part")
    p.add_argument("--dry", action="store_true",
                   help="Preview without moving")
    args = p.parse_args()

    move_matches(args.source, args.destination,
                 pattern=args.pattern,
                 replace=args.replace,
                 dry=args.dry)

# --- examples ---
# eth_1.jpg -> eth_l2_1.jpg
# python 03_regex_match.py Source_Dir Eth_Matches --pattern "(?i)eth_" --replace "eth_l2_" --dry
# python 03_regex_match.py Source_Dir Eth_Matches --pattern "(?i)eth_" --replace "eth_l2_"