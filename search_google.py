#!/usr/bin/env python3
import clipboard
import webbrowser

url = "https://www.google.com.tr/search?q=" + clipboard.paste()
webbrowser.open(url)
exit()
