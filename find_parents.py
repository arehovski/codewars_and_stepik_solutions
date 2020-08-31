"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта
есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется
явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2
"""


import json


def is_parent(graph, parent, searched):
    children = 0
    for item in graph:
        if item['name'] not in searched:
            if parent in item['parents']:
                children += 1
                searched.append(item['name'])
                children += is_parent(graph, item['name'], searched)
    return children


def main_parents(graph):
    graph = json.loads(graph)
    output = {}
    searched = []
    for item in graph:
        output[item['name']] = is_parent(graph, item['name'], searched)
        searched.clear()
    output_string = '\n'.join(f'{cls} : {value+1}' for cls, value in sorted(output.items()))
    return output_string
