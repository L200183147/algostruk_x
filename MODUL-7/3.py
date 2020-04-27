import re

q = open('indonesia.txt', 'r', encoding = 'latin1')
teks = q.read()
q.close()

pola = r'di\s\w+'
r = re.findall(pola, teks)
print(r)
