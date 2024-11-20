"""
Fet per: Marc Balaguer Guerra
Data: 18/10/2024

Ara tens una llista ordenada de llibres on cada llibre està representat per una llista que conté el títol del llibre i el nom de
l'autor. Vols verificar si un determinat llibre, "Moby Dick" de Herman Melville, està disponible a la biblioteca.
"""

llibres = [
    ["A Tale of Two Cities", "Charles Dickens"],
    ["Catcher in the Rye", "J.D. Salinger"],
    ["Don Quixote", "Miguel de Cervantes"],
    ["Harry Potter", "J.K. Rowling"],
    ["Moby Dick", "Herman Melville"],
    ["The Great Gatsby", "F. Scott Fitzgerald"],
    ["War and Peace", "Leo Tolstoy"]
]

element_cercar = ["Moby Dick", "Herman Melville"]

trobat = False
inf = 0
sup = len(llibres)-1
while inf <= sup and not trobat:
    mig = (sup - inf)//2 + inf
    if element_cercar == llibres[mig]: 
        trobat = True 
    elif element_cercar < llibres[mig]:
        sup = mig - 1
    else:
        inf = mig + 1


if not trobat:
    print("no trobat")
else:
    print(f"trobat a la posició",mig)
