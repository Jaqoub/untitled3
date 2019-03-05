import Øvelse
from Øvelse import greeting
import sys
import os
from urllib.request import urlopen

res = urlopen('http://kea.dk')
print(res)
html = res.read()
#print(html)


file = open('kea.html', 'w')
file.write(html)
print(html)

html = res.read().decode('utf-8')

os.mkdir('XXX')
os.chdir('XXX')

sys.exit()
subprocess.run(['git', 'clone', 'http://github.com'])

print(greeting)
one.main()