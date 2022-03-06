import os

pre = '''---
title: %s
---

'''

for path in os.listdir(os.getcwd()):
    if not path.endswith(".txt"):
        continue

    file = open(path, "r", encoding="utf-8")

    title = file.readline()
    content = ["<p>"+line+"</p>" for line in file.read().splitlines() if line != ""]
    content = "\n\n".join(content)
    file.close()

    os.remove(path)

    file = open(path[:-4]+".md", "w", encoding="utf-8")
    file.write(pre%(title) + content)
    file.close()
    
