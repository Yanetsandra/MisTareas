LISTAS EN PYTHON
Las listas es una conexi�n de datos ordenada, alguna equivalencia con otros lenguajes ser�a los arrays o vectores. La lista puede contener cualquier tipo de datos (enteros, cadenas, y otras listas)
Como se puede crear una lista: 
>>> lista = [�hola�, 2,�hacker�, [1,2,3,4,5]]

Si se dan cuenta nuestra lista principal tiene un string �hola�, un entero 2 y otra lista, una lista de otra lista.

>>> print (lista)
['hola',2, 'hacker ',[1,2,3,4,5]

Si queremos acceder a uno de los elementos de la lista lo hacemos utilizando el nombre que hacemos referencia a la lista en este caso lo llamaremos lista, puede ser cualquiera y entre corchete indicamos un �ndice, dicho �ndice va de 0 a n-1, como a continuaci�n:

>>> print(lista[0])
hola
>>> print(lista[3])
[1,2,3,4,5]


Para poder acceder al 2 pero no sabemos que hacer ya que es una lista dentro de otra, veamos la soluci�n:
>>> print(lista[3][1])
2


 Hay que tener en cuenta que este operador [] se puede utilizar para modificar los elementos de la lista de esta forma:

>>>lista[0]=�Python�
>>>print(lista)
['Phyton ',2, 'hacker ',[1,2,3,4,5]]


Con el operador [ ] podemos hacer referencia a cualquier elemento de la lista 0 a n-1 pero python trae algo que es recorrer la lista de ultimo al primero utilizando n�mero negativos, como se muestra a continuaci�n:
>>> nombres = [ �angelica�,�paola�,�hachchan�,�Python�]
>>>print (nombres[-1])
Python





Otros ejemplos con listas:
���ANIDAMIENTO: Este sirve para a�adir un elemento a la lista.
Ejemplo: 
	>>> st=[�coma�,�tren�]
	>>>ut=[�ram�,em�,8]
	>>>ut[3].append(st)
	>>>ut
[�ram�,�emm�,8,[�coma�,�tren�]]

FOR:
Es un ciclo que corre los elementos de una lista.
Ejemplo:
	>>> tu=[�Omar�,�Emmanuel�,�Antonio�,�omar�,Jose�,�jose�,�Emmanuel�,�Jose�]
	>>>Numero=0
	>>>for tus in tu:
	If tus=�jose�
Numero=numero+1
>>> Numero
3
INDEX:
	Sirve para mostrar el �ndice de un elemento de una lista.
Ejemplo:
>>> ka=[2,�perro�,8,�gato�]
>>> ka.index(perro)






DEFINIENDO CADENAS
En Python tenemos varias formas ligeramente diferentes de definir cadenas. La forma m�s com�n es escribirlas entre comillas dobles (�):
Cadena = �hola�
Tambi�n pueden utilizarse comillas simples (�), no hay diferencia entre las cadenas delimitadas con � o �.
Por razones obvias, no podemos incluir en la cadena una comilla del mismo tipo que la que se utiliza para definirla, Python no sabr� d�nde termina realmente:
>>> mi_cadena = �hola �amigo� �
File ��, line 1
mi_cadena = �hola �mundo� �
SyntaxError.invalidsyntax
Una forma posible de evitar esto es delimitar la cadena con comillas simples si sabemos que contendr� comillas dobles y delimitarla con comillas dobles si sabemos que contendr� comillas simples.
Tampoco podemos incluir saltos de l�nea en la cadena:
>>> mi_cadena = �hola �amigo� �
File ��, line 1
mi_cadena = �hola 
		^

SyntaxError.EOL while scaning string literal
Para solucionar esto, tenemos la opci�n de utilizar secuencias de escape. Las secuencias de escape permiten introducir caracteres especiales, escap�ndolos(forz�ndolos a ser caracteres sin significado especial) con una contrabarra (\) delante. La secuencia de escape para un salto de l�nea es �\n�:
>>> print �hola � \n \�mundo\� � # los espacios antes y despu�s de \n no son necesarios, se agregan por claridad
Hola
�mundo�

Para solucionar el problema de los saltos de l�nea o las comillas, podemos utilizar tambi�n una tercera v�a: las cadenas en Python pueden delimitarse con bloques de tres comillas dobles (��") o tres ap�strofes (��). Saltos de l�nea y comillas individuales est�n permitidos en este tipo de cadenas.
>>> print ���hola
�mundo� ���
