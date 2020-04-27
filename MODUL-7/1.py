import re

m = open('indonesia.txt', 'r', encoding = 'latin1')
teks = m.read()
m.close()

pola = r'\sme\w+'
n = re.findall(pola, teks)
print(n)
