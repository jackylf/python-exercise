#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    content = ' '.join(sys.argv[1:]) #用法：python baidu.py 所搜索内容
else:
    content = pyperclip.paste()

webbrowser.open('https://www.baidu.com/s?wd=' + content)