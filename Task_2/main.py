print('Дано целое положительное число, представленное в виде строки, и целое число "k".\n'
      'Вернуть минимальное возможное число, полученное после удаления из строки k цифр.')
number = input('Введите целое положительное число:')
k = int(input('Введите целое число "k":'))


def find_minimum_number(number, k):
    if len(number) == k:
        return "0"
    lst = []
    for ind, val in enumerate(number):
        if len(lst) == 0:
            lst.append(val)
        else:
            while len(lst) > 0 and val < lst[-1] and len(lst) >= ind - k + 1:
                lst.pop()
            if len(lst) == 0 or len(lst) < len(number) - k:
                lst.append(val)
    return str(int("".join(lst)))


print('Минимальное возможное число, полученное после удаления из строки k цифр:', find_minimum_number(number, k))