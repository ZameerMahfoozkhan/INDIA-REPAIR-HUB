import os
import re

dir_path = r"c:\Users\zamee\Desktop\indiarepairhub"

replacements = [
    (r"TV models", "appliance models"),
    (r"TV model", "appliance model"),
    (r"the TV", "the appliance"),
    (r"your TV", "your appliance"),
    (r"my TV", "my appliance"),
    (r"LED TV", "appliance"),
    (r"Smart TV", "appliance"),
    (r"TV Fixed", "Appliance Fixed"),
    (r"TV ", "appliance "),
]

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace text replacements
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Replacement complete.")
