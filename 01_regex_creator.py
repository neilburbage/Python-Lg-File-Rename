from pathlib import Path
import argparse

PROJECT_ROOT = Path(__file__).resolve().parent

def resolve_directory(dir_arg: str) -> Path:
    """
    If *dir_arg* is an absolute path (or begins with ~), expand it normally.
    Otherwise, treat it as a subfolder of the project root.
    """
    p = Path(dir_arg).expanduser()
    return p if p.is_absolute() else PROJECT_ROOT / p

def make_files(directory: str, count: int, ext:str, *, start: int = 1) -> None:
    """
    Create *count* empty files named file<start><ext>, file<start+1><ext> ...
    in *directory*. Directory is created if missing.
    """
    directory = resolve_directory(directory)
    directory.mkdir(parents=True, exist_ok=True)

    ext_list = [e.strip() if e.startswith(".") else f".{e.strip()}]"
            for e in args.exts.split(",")]

    for ext in ext_list:
        for i in range(start, start + count):
            (directory / f"file{i}{ext}").touch()
            print(f"Created file{i}{ext}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk create files.")
    parser.add_argument("directory", help="Target folder (relative = sub folder of project)")
    parser.add_argument("--count", type=int, default=10,
                        help="Number of files to create (default: 10)")
    parser.add_argument("--exts", default=".txt",
                        help='Comma separated list like ".py,.jpg,.docx"')
    parser.add_argument("--start", type=int, default=1,
                        help="Starting number for filenames (default: 1)")
    args = parser.parse_args()

    make_files(args.directory, args.count, args.exts, start=args.start)

# --- examples ---

# python 01_regex_creator.py Source_Dir --count 3 --exts ".jpg,.pdf,.py,.docx,.rs,.sol,.xls,.ts,.csv" --dry
# python 01_regex_creator.py Source_Dir --count 3 --exts ".jpg,.pdf,.py,.docx,.rs,.sol,.xls,.ts,.csv"