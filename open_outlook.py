import webbrowser

url = "https://outlook.office.com/mail/"
firefox_path = "/usr/bin/firefox"  
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open(url)