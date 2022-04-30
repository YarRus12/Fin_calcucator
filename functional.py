from datetime import datetime, date

def month_count(end_of_period, day_mon_year):
    now_date = datetime(*day_mon_year)
    end_date = datetime(*end_of_period)
    return ((end_date.year - now_date.year) * 12 + (end_date.month - now_date.month)), str(end_date - now_date).split(' ')[0]

def month_name(number):
    month = ['января', 'февраля', 'марта', 'апреля',
             'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    return month[number-1]

def next_date(date_in):
    """Функция прибавляет к дате 1 месяц"""
    year, month, day = map(int, str(date_in).split('-'))
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1
    return date(year, month, day)

def annuity_payment(ammount, procents, **kwargs):
    """Формула расчета аннуитетного платежа"""
    for key, value in kwargs.items():
        if key == 'days':
            procent_per_day = (procents / 365) / 100
            return ammount * (procent_per_day / (1 - (1 + procent_per_day) ** (-(int(value) - 1))))
        if key == 'month':
            procent_per_month = (procents/12)/100
            return ammount * (procent_per_month / (1 - (1 + procent_per_month) ** (-(value - 1))))

def data_inputs():
    #это тестовые данные для удобства разработки
    amount = 757786.25
    procent = 7.91
    end_date = (2029, 1, 15)
    start_date = (2022, 4, 16)
    #Этот фрагмент работает, но для удобства пока оставим его спящим
    """
    amount = decimal(input('Введите размер суммы кредита: '))
    procent = str(input('Введите размер процента по кредиту: '))
    if ',' in str(procent):
        procent = str(procent).replace(',', '.')
    while True:
        end_date = input('Введите год, месяц и день завершения кредита через запятую: ')
        end_date = tuple(int(x.strip()) for x in end_date.split(','))
        start_date = input('Введите год, месяц и день начала кредита через запятую: ')
        start_date = tuple(int(x.strip()) for x in start_date.split(','))
        if start_date >= end_date:
            print("Дата заключения договора кредита больше чем дата завершения, попробуйте еще раз")
        else:
            break"""
    return amount, procent, end_date, start_date