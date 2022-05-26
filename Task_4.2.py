"""
2) Определите класс итератор ReverseIter, который
принимает список и итерируется по нему в обратном направлении

Метод __iter__(), который возвращает объект с помощью метода __next__().
Если класс определяет __next__(), то __iter__() может просто вернуть себя:
"""


class ReversIter:

    def __init__(self, stroka):
        self.stroka = stroka
        self.index = len(stroka)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.stroka[self.index]


revers = ReversIter("Google Maps")
# print(iter(revers))

# проходка по словам
for char in revers:
    print(char)
