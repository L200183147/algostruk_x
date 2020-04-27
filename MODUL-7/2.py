import re
o = open('indonesia.txt', 'r', encoding = 'latin1')
teks = o.read()
o.close()

pola = r'di\w+'
p = re.findall(pola, teks)
print(p)
