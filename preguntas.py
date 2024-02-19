"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def c():
    l=[]
    for i in open('data.csv'):
        ls=i.split()
        ds={}
        for i in ls[4].split(','):
            i=i.split(':')
            ds[i[0]]=int(i[1])

        d={
            'id':ls[0],
            'cuenta':int(ls[1]),
            'fecha':ls[2],
            'letras':ls[3].split(','),
            'claves':ds
        }
        l.append(d)
    return l

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum(map(lambda x:x['cuenta'],c()))

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    d={}
    for i in list(map(lambda x:x['id'],c())):
        try:
            d[i]+=1
        except:
            d[i]=1
    
    
    return list(sorted(d.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    d={}
    for i,j in list(map(lambda x:(x['id'],x['cuenta']),c())):
        try:
            d[i]+=j
        except:
            d[i]=j

    return list(sorted(d.items()))

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    d={}
    for i in list(map(lambda x:x['fecha'][5:7],c())):
        try:
            d[i]+=1
        except:
            d[i]=1
    return list(sorted(d.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    l=[
        ["A", 0, 9],
        ["B", 0, 9],
        ["C", 0, 9],
        ["D", 0, 9],
        ["E", 0, 9],
    ]
    for i in c():
        for j in l:
            if j[0]==i['id']:
                if j[1]<i['cuenta']:
                    j[1]=i['cuenta']
                if j[2]>i['cuenta']:
                    j[2]=i['cuenta']

    for i in range(len(l)):
        l[i]=tuple(l[i])

    return l


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    d={}
    for i in c():
        
        for j in i['claves']:
            try:
                if d[j]['max']<i['claves'][j]:
                    d[j]['max']=i['claves'][j]
                if d[j]['min']>i['claves'][j]:
                    d[j]['min']=i['claves'][j]
            except:
                d[j]={'min':i['claves'][j] ,'max':i['claves'][j]}
    
    l=[]

    for i in d:
        l.append((i,d[i]['min'],d[i]['max']))
        
    return sorted(l)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    d={}

    for i in c():
        try:
            d[i['cuenta']].append(i['id'])
        except:
            d[i['cuenta']]=[i['id']]
    l=[]
    for i in d:
        l.append((i,d[i]))
    return sorted(l)
    

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    d={}

    for i in c():
        try:
            if i['id'] not in d[i['cuenta']]:
                d[i['cuenta']].append(i['id'])
        except:
            d[i['cuenta']]=[i['id']]
    l=[]
    for i in d:
        l.append((i,sorted(d[i])))
    return sorted(l)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    d={}
    for i in c():
        
        for j in i['claves']:
            try:
                d[j]+=1
            except:
                d[j]=1
        
    return dict(sorted(d.items()))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    l=[]
    for i in c():
        l.append((i['id'],len(i['letras']),len(i['claves'])))

    return l

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    d={}
    for i in c():
        for j in i['letras']:
            try:
                d[j]+=i['cuenta']
            except:
                d[j]=i['cuenta']
    return dict(sorted(d.items()))

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """ 
    d={}
    for i in c():
        for j in i['claves']:
            try:
                d[i['id']]+=i['claves'][j]
            except:
                d[i['id']]=i['claves'][j]

    return dict(sorted(d.items()))