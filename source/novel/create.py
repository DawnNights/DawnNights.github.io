import os
top = '<html data-dpr="2"style="font-size: 108px;"><head lang="en"><meta charset="UTF-8"><title>DawnNights的小文库</title><meta name="name"content=""><meta name="image"content=""><!--more meta--><meta name="format-detection"content="telephone=no"><meta name="apple-mobile-web-app-capable"content="yes"><meta name="apple-mobile-web-app-status-bar-style"content="black"><meta name="viewport"content="width=device-width, initial-scale=0.5, maximum-scale=0.5, minimum-scale=0.5, user-scalable=0"><!--针对UC浏览器的设置--><meta name="browsermode"content="application"><!--应用模式--><meta name="full-screen"content="no"><!--QQ应用模式--><meta name="x5-page-mode"content="app"><link type="image/x-icon"rel="shortcut icon"href="https://wap.ciweimao.com/resources/images/icon-logo.png"><link rel="stylesheet"href="https://wap.ciweimao.com/resources/css/style.css?v=1.0.5"><link rel="miphtml"href="https://mip.ciweimao.com/chapter/107522789"><link id="J_readbookStyle"rel="stylesheet"type="text/css"href="https://wap.ciweimao.com/resources/css/skin/white.css"><div class="container"><div class="book-read-box"id="J_BookReadBox"><h1 class="read-hd">无标题</h1><div class="read-bd"id="J_BookRead"style="font-size: 28px;">'
down = '</div><div class="chapter-over"><span>本章结束</span></div><div class="book-read-page clearfix"><a class="btn-page J_BtnPagePrev"data-href=""href="javascript:"><i class="icon icon-prev"></i>上一章</a><a href="/source/novel"class="btn-list"><i class="icon icon-catalogue"></i>目录</a><a class="btn-page J_BtnPageNext"data-href=""href="javascript:"><i class="icon icon-next"></i>下一章</a></div></div></div><div class="mask"style="display: none; opacity: 0;"></div><!--各种默认的浏览器行为限制--><script>if(navigator.control){navigator.control.gesture(false);navigator.control.longpressMenu(false);navigator.control.menu(false)}</script></body></html>'

for path in os.listdir(os.getcwd()):
    if path.endswith(".txt"):
        text = open(path, "r", encoding="utf-8").read().splitlines()
        text = top + "\n".join(['<p class="chapter">%s</p>' %
                               (txt) for txt in text]) + down

        os.remove(path)
        open(path[:-4]+".html", "w", encoding="utf-8").write(text)
