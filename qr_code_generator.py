import pyqrcode
url = pyqrcode.create('https://pypi.org/project/PyQRCode/')
url.svg('uca-url.svg', scale=1)
url.eps('uca-url.eps', scale=1)
print(url.terminal(quiet_zone=1))