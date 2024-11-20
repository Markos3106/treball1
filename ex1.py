"""
Fet per: Marc Balaguer Guerra
Data: 14/10/2024

Suposa que ets un professor que necessita ordenar les qualificacions finals dels estudiants de menor a major per a poder assignar les
notes finals fàcilment. Les qualificacions estan emmagatzemades en una llista de Python. Implementa l'algorisme d'ordenació de la
bombolla per ordenar aquesta llista.
"""

qualificacions = [8.8, 9.5, 7.0, 10.0, 9.3, 8.5, 7.4, 9.9, 9.2, 7.8]

n = len(qualificacions) # optimització
intercanvi = True # per entrar la 1a vegada
while intercanvi:
	intercanvi = False # per saber si ha acabat
	for i in range(1, n):
		if qualificacions[i - 1] > qualificacions[i]:
			qualificacions[i], qualificacions[i-1] = qualificacions[i - 1], qualificacions[i] 
			intercanvi = True
         
	n = n - 1 # optimització

print(qualificacions)
