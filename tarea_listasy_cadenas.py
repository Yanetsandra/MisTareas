LISTAS EN PYTHON
Las listas es una conexión de datos ordenada, alguna equivalencia con otros lenguajes sería los arrays o vectores. La lista puede contener cualquier tipo de datos (enteros, cadenas, y otras listas)
Como se puede crear una lista: 
>>> lista = [“hola”, 2,”hacker”, [1,2,3,4,5]]

Si se dan cuenta nuestra lista principal tiene un string “hola”, un entero 2 y otra lista, una lista de otra lista.

>>> print (lista)
['hola',2, 'hacker ',[1,2,3,4,5]

Si queremos acceder a uno de los elementos de la lista lo hacemos utilizando el nombre que hacemos referencia a la lista en este caso lo llamaremos lista, puede ser cualquiera y entre corchete indicamos un índice, dicho índice va de 0 a n-1, como a continuación:

>>> print(lista[0])
hola
>>> print(lista[3])
[1,2,3,4,5]


Para poder acceder al 2 pero no sabemos que hacer ya que es una lista dentro de otra, veamos la solución:
>>> print(lista[3][1])
2


 Hay que tener en cuenta que este operador [] se puede utilizar para modificar los elementos de la lista de esta forma:

>>>lista[0]=”Python”
>>>print(lista)
['Phyton ',2, 'hacker ',[1,2,3,4,5]]


Con el operador [ ] podemos hacer referencia a cualquier elemento de la lista 0 a n-1 pero python trae algo que es recorrer la lista de ultimo al primero utilizando número negativos, como se muestra a continuación:
>>> nombres = [ “angelica”,”paola”,”hachchan”,”Python”]
>>>print (nombres[-1])
Python





Otros ejemplos con listas:
“””ANIDAMIENTO: Este sirve para añadir un elemento a la lista.
Ejemplo: 
	>>> st=[“coma”,”tren”]
	>>>ut=[“ram”,em”,8]
	>>>ut[3].append(st)
	>>>ut
[“ram”,”emm”,8,[“coma”,”tren”]]

FOR:
Es un ciclo que corre los elementos de una lista.
Ejemplo:
	>>> tu=[“Omar”,”Emmanuel”,”Antonio”,”omar”,Jose”,”jose”,”Emmanuel”,”Jose”]
	>>>Numero=0
	>>>for tus in tu:
	If tus=”jose”
Numero=numero+1
>>> Numero
3
INDEX:
	Sirve para mostrar el índice de un elemento de una lista.
Ejemplo:
>>> ka=[2,”perro”,8,”gato”]
>>> ka.index(perro)






DEFINIENDO CADENAS
En Python tenemos varias formas ligeramente diferentes de definir cadenas. La forma más común es escribirlas entre comillas dobles (“):
Cadena = “hola”
También pueden utilizarse comillas simples (‘), no hay diferencia entre las cadenas delimitadas con ” o ‘.
Por razones obvias, no podemos incluir en la cadena una comilla del mismo tipo que la que se utiliza para definirla, Python no sabrá dónde termina realmente:
>>> mi_cadena = “hola ”amigo” “
File “”, line 1
mi_cadena = “hola “mundo” ”
SyntaxError.invalidsyntax
Una forma posible de evitar esto es delimitar la cadena con comillas simples si sabemos que contendrá comillas dobles y delimitarla con comillas dobles si sabemos que contendrá comillas simples.
Tampoco podemos incluir saltos de línea en la cadena:
>>> mi_cadena = “hola ”amigo” “
File “”, line 1
mi_cadena = “hola 
		^

SyntaxError.EOL while scaning string literal
Para solucionar esto, tenemos la opción de utilizar secuencias de escape. Las secuencias de escape permiten introducir caracteres especiales, escapándolos(forzándolos a ser caracteres sin significado especial) con una contrabarra (\) delante. La secuencia de escape para un salto de línea es “\n”:
>>> print “hola ” \n \”mundo\” “ # los espacios antes y después de \n no son necesarios, se agregan por claridad
Hola
“mundo”

Para solucionar el problema de los saltos de línea o las comillas, podemos utilizar también una tercera vía: las cadenas en Python pueden delimitarse con bloques de tres comillas dobles (“”") o tres apóstrofes (”’). Saltos de línea y comillas individuales están permitidos en este tipo de cadenas.
>>> print “””hola
“mundo” “””
