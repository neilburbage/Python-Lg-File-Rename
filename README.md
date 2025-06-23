# Python Large File Renamer


**<strong>A toolkit for bulk creating, renaming and matching files:</strong>**<br>
**<strong>Create test data, bulk rename by extension, regex match and move.</strong>**<br>

<small>
<strong>Contains three small CLI tools that turn a folder of random files into an organised dataset.</strong><br>
</small>

---

### Scripts at a glance

<small>

| File | What it does                                                                        |
|------|-------------------------------------------------------------------------------------|
| 01_regex_creator.py | Factory-generate N dummy files of any extension in a source folder.                 |
| 02_regex_rename.py  | Rename all files whose extension is in a comma separated list (e.g., `.jpg,.pdf`).  |
| 03_regex_match.py   | Move regex match (case insensitive) to destination folder and rewrite matched part. |

</small>

 ---

<small>

### Quick start 

**Clone this repo:**  
```git clone git@github.com:neilburbage/Python-Lg-File-Rename.git```  
**Make sure you've added your SSH key first:**   
```https://docs.github.com/en/authentication/connecting-to-github-with-ssh```    
```cd Python-Lg-File-Rename```  
**Create a virtual environment:**       
```python -m venv .venv```  
```# Linux / macOS: source .venv/bin/activate```     
```# Windows (PowerShell): .venv\Scripts\Activate.ps1```  
```# Windows (cmd): .venv\Scripts\activate.bat``` 

</small>

---

<small>

```bash
# 1 Create test data in Source_Dir
python 01_regex_creator.py Source_Dir \
        --count 3 \
        --exts ".jpg,.pdf" \
        --dry   # preview
        
# 2 Bulk-rename by extension        
python 02_regex_rename.py Source_Dir \
        --ext ".jpg,.pdf" \
        --newname btc_ \
        --dry   # preview

# 3 Move files whose name contains “eth” to Eth_Matches
python 03_regex_match.py Source_Dir Eth_Matches \
        --pattern "(?i)eth_" \
        --replace "eth_l2_" \
        --dry   # preview

```

</small>

---

### Project layout

```
Python-Lg-File-Rename/
│
├── 01_regex_creator.py   # file creator script
├── 02_regex_rename.py    # file renamer script
├── 03_regex_match.py     # regex match script
├── Source_Dir/           # example source directory
├── Eth_Matches/          # example destination directory
├── .gitignore            # .venv/, __pycache__/
└── README.md             # you are here
```

---







