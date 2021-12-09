import os

html = '''<html>

<head>
    <meta charset="utf-8">
    <meta name="description">
    <title>夜黎的小文库</title>
    <link href="https://rs.sfacg.com/web/m/css/v2/book-1.0.14.css" rel="stylesheet" type="text/css">
</head>

<body>
    <a name="top"></a>
    <ul class="menu_top_list book_view_top" style="top: -10px;height: 50px;">
        <li><a href="/source/novel">返回</a></li>
        <li>%s</li>
        <li></li>
    </ul>
    <div class="yuedu Content_Frame" style="margin-top:0.4rem;">
        <div style="text-indent: 2em;">
            %s
            <br><br><br><br><br><br><br>
        </div>
    </div>
</body>
<div class="bottom_menu"></div>
</html>'''

for path in os.listdir(os.getcwd()):
    if not path.endswith(".txt"):
        continue

    file = open(path, "r", encoding="utf-8")

    title = file.readline()
    content = ["<p>"+line+"</p>" for line in file.read().splitlines() if line != ""]
    content = "\n".join(content)
    file.close()

    os.remove(path)

    file = open(path[:-4]+".html", "w", encoding="utf-8")
    file.write(html%(title, content))
    file.close()
    
