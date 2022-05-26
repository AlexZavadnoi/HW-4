"""
1) Необходимо написать функцию калькулятор, которая принимает
строку состоящую из числа, оператора и второго числа разделенных пробелом.
Например ('1 + 1');
Необходимо разделить строку используя str.split(), и проверить является
результирующий список валидным.

    a) Если ввод не состоит из 3 элементов, необходимо возбудить исключение FormulaError,
которое является пользовательским исключением.

    b) Попытайтесь сконвертировать первое и третье значение ввода к типу float.
Перехватите любые исключения типа ValueError, которые возникают, и выбросите FormulaError

    c) Если второе значение ввода не является '+', '-', '*', '/' также выбросите FormulaError.
    Если input валидный - ф - я должна вернуть результат операции
"""


def calculet():
    user_str = input("Введите 2 числа и оператор разделенных пробелом: ").split()
    number = []

    for i in user_str:
        number.append(i)
    # print(number)

    if number[1] == "+":
        try:
            return print(float(number[0]) + float(number[2]))
        except:
            print("FormulaError")

    elif number[1] == '-':
        try:
            return print(float(number[0]) - float(number[2]))
        except:
            print("FormulaError")

    elif number[1] == '*':
        try:
            return print(float(number[0]) * float(number[2]))
        except:
            print("FormulaError")

    elif number[1] == '/':
        try:
            return print(float(number[0]) / float(number[2]))
        except:
            print("FormulaError")

    else:
        print("FormulaError")


calculet()


