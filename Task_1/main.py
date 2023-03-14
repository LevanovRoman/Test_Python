print(' Посчитаем количество дней между датами.\n'
      'Введите две даты в формате YYYY-MM-DD:')
date1 = input('Первая дата: ')
date2 = input('Вторая дата: ')
quantity_day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def split_date(date):
    """ Получаем значения года, месяца и дня в виде чисел """
    year, month, day = map(int, date.split('-'))
    return year, month, day


def calculate_leap_years(date):
    """ Подсчёт количества високосных лет """
    year = split_date(date)[0]
    month = split_date(date)[1]
    if month <= 2:
        year -= 1
    return int(year / 4 - year / 100 + year / 400)


def count_days_for_date(date):
    """ Подсчёт количества дней от нулевой даты до данной """
    year, month, day = split_date(date)
    in_month = sum([quantity_day_in_month[i] for i in range(month - 1)])
    numbers_of_days = year * 365 + in_month + day + calculate_leap_years(date)
    return numbers_of_days


result = abs(count_days_for_date(date2) - count_days_for_date(date1))
print('Количество дней между этими датами:', result)



