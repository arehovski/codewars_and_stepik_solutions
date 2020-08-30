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


def is_parent(parent, lst):
    children = 0
    for dct in jsn:
        if dct['name'] not in lst:
            if parent in dct['parents']:
                children += 1
                searched.append(dct['name'])
                children += is_parent(dct['name'], lst)
    return children


if __name__ == '__main__':
    jsn = json.loads(input())
    output = {}
    searched = []
    for dct in jsn:
        output[dct['name']] = is_parent(dct['name'], searched)
        searched.clear()
    for cls, value in sorted(output.items()):
        print(f'{cls} : {value+1}')
