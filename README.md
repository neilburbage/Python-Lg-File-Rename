## Python-Lg-File-Rename:
### A toolkit for bulk creating, renaming and matching files:
Create test data, bulk rename by extension and regex match and move.

This toolkit contains three small CLI tools that turn a folder of random files into an organised dataset.

### Scripts at a glance

| File | What it does                                                                        |
|------|-------------------------------------------------------------------------------------|
| 01_regex_creator.py | Factory-generate N dummy files of any extension in a source folder.                 |
| 02_regex_rename.py  | Rename all files whose extension is in a comma separated list (e.g., `.jpg,.pdf`).   |
| 03_regex_match.py   | Move regex match (case-insensitive) to destination folder and rewrite matched part. |

### Quick start

```bash
python -m venv venv
# On Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# 1 Create test data in Source_Dir
python 01_regex_creator.py Source_Dir \
       --count 3 \
       --exts ".jpg,.pdf" \
       --dry      # preview

# 2 Bulk-rename by extension
python 02_regex_rename.py Source_Dir \
       --ext ".jpg,.pdf" \
       --newname btc_ \
       --dry      # preview

# 3️ Move files whose name contains “eth” to Eth_Matches
python 03_regex_match.py Source_Dir Eth_Matches \
       --pattern "(?i)eth_" \
       --replace "eth_l2_" \
       --dry      # preview

Python-Lg-File-Rename/
├── 01_regex_creator.py
├── 02_regex_rename.py
├── 03_regex_match.py
├── Source_Dir/   # example source
├── Eth_Matches/  # example destination
├── .gitignore
└── venv/         # virtual env (ignored)









