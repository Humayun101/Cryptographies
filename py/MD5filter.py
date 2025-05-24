import re

# Use full path to cleaned_hashes.txt
file_path = "/home/humayun404/Downloads/cleaned_hashes.txt"

# Load hashes
with open(file_path, "r") as f:
    hashes = [line.strip() for line in f]

# Filter only valid lowercase MD5 hashes (32-character hex)
valid_md5s = [h for h in hashes if re.fullmatch(r"[a-f0-9]{32}", h)]

# Show result
if valid_md5s:
    print(f"✅ Real flag found: flag{{{valid_md5s[0]}}}")
else:
    print("❌ No valid MD5-format hash found.")
