import os

print("Hello world from ...")
os.system("python --version")


"""
Practica Listas Python CodeCademy

Step 1: funcion len()
Nuestra amiga Jiho ha tenido tanto éxito en el negocio de las flores y los comestibles que ha decidido abrir una tienda de muebles.

Jiho ha recopilado una lista de artículos en una lista llamada "inventario" y quiere saber algunos datos sobre ella.

En primer lugar, ¿cuántos artículos hay en el almacén?
Guarda la respuesta en una variable llamada "inventario_len".

Step 2:
Selecciona el primer elemento del inventario. Guárdalo en una variable llamada "primero".

*Recuerde que las listas de Python tienen índice cero. index [0]

Step 3:
Selecciona el último elemento del inventario. Guárdalo en una variable llamada "ultimo".

Step 4: (Slicing List)
Selecciona los artículos del "inventario" empezando por el "índice 2 y hasta el índice 6", pero sin incluirlo.

Guarda tu respuesta en una variable llamada "inventario_2_6".

Step 5: (Slicing List)
Selecciona los 3 primeros artículos del "inventario". Guárdalo en una variable llamada "first_3".

Step 6: metodo .count()
¿Cuántas "camas gemelas" hay en el "inventario"? Guarda tu respuesta en una variable llamada "twin_beds".

Step 7 metodo .pop()

Elimina el 5º elemento del "inventario". Guarda el valor en una variable llamada "elemento_eliminado". (El elemento 5 seria el indice 4)


Step 8 metodo .insert()
Se ha añadido un nuevo elemento a nuestro inventario llamado "Armazón de cama del siglo XIX".

Utilice el método .insert() para colocar el nuevo elemento como el undécimo elemento de nuestro "inventario".

Step 9 funcion sorted() o metodo .sort()
Ordene el inventario utilizando el método .sort() o la función sorted().

Recuerde, la función sorted() no cambia la lista original - crea una nueva lista con los elementos correctamente ordenados. Si utiliza sorted() tendrá que establecer el inventario igual al valor devuelto por sorted().

Imprima el inventario para ver el resultado.

"""


#Practica Listas Python 

inventario = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Step 1 funcion len()
#Guardo la Variable inventario_len en inventario
inventario_len = len(inventario)

#Step 2
primero = inventario[1]

#Step 3
ultimo = inventario[18]

#Step 4 Slicing List
inventario_2_6 = inventario[2:6]

#Step 5 Slicing List
primero_3 = inventario[:3]


#Step 6 .count()
twin_beds = inventario.count('twin bed') #4


#Step 7 .pop()
elemento_eliminado = inventario.pop(4)


#Step 8 .insert()
inventario.insert(10, "19th Century Bed Frame")
print(inventario)


#Step 9 metodo .sort() o funcion sorted()

#.sort()
inventario.sort()

#sorted()
inventario = sorted(inventario)

print(inventario)