"""
Fet per: Marc Balaguer Guerra
Data: 18/10/2024

Tens una llista d'edats de participants a un esdeveniment. Per a organitzar grups per edats, necessites ordenar aquesta llista de
manera ascendent.
Utilitza l'algorisme d'ordenació de la bombolla per ordenar la llista participants de menor a major edat.
"""

participants = [
    ["Joan", 22],
    ["Maria", 45],
    ["Carlos", 38],
    ["Anna", 19],
    ["Pere", 56],
    ["Laura", 24],
    ["Enric", 12],
    ["Sònia", 27],
    ["David", 31],
    ["Elena", 18],
    ["Ricard", 42]
]

n = len(participants) # optimització
intercanvi = True # per entrar la 1a vegada
while intercanvi:
	intercanvi = False # per saber si ha acabat
	for i in range(1, n):
		if participants[i - 1][1] > participants[i][1]:
			participants[i][1], participants[i-1][1] = participants[i - 1][1], participants[i][1] 
			intercanvi = True
         
	n = n - 1 # optimització

# gran print
# C:
print(participants)