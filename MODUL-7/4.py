import re

t = open('KEI.html', 'r', encoding = 'latin1')
teks = t.read()
t.close()

pola = r'(\w+)</a></td>'
u = re.findall(pola, teks)
print(u)

v = open('KEI.html', 'r', encoding = 'latin1')
teks2 = v.read()
v.close()

pola2 = r'(\w+)</a></td>\n<td>(\d.\d+)'
tuples = re.findall(pola2, teks2)
print(tuples)

print(" --- list of tuples --- ")
tupp = [(t[0], float(t[1]))for t in tuples]
print(tupp)
