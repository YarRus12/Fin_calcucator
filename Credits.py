from datetime import date
import functional as func

def annuity_payment(ammount, procents, **kwargs):
    """Формула расчета аннуитетного платежа"""
    for key, value in kwargs.items():
        if key == 'days':
            procent_per_day = (procents / 365) / 100
            return ammount * (procent_per_day / (1 - (1 + procent_per_day) ** (-(int(value) - 1))))
        if key == 'month':
            procent_per_month = (procents/12)/100
            return ammount * (procent_per_month / (1 - (1 + procent_per_month) ** (-(value - 1))))

def next_date(date_in):
    """Функция прибавляет к дате 1 месяц"""
    year, month, day = map(int, str(date_in).split('-'))
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1
    return date(year, month, day)

def full_payment(ammount, procents, end_of_period, day_mon_year):
    """Функция расчета размера платежа"""
    summ = ammount
    now_date = date(*day_mon_year)
    months, days = func.month_count(end_of_period, day_mon_year)
    while summ > 0:
        str_date = next_date(now_date)
        payment = annuity_payment(ammount, procents, month = months)
        #payment = annuity_payment(ammount, procents, days = days)
        print(f'На {str_date.day} {func.month_name(str_date.month)} {str_date.year} '
              f'года размер ежемесячного платежа составит {round(payment, 2)}, '
              f'остаток по кредиту составляет {round(summ, 2)}')
        summ -= payment
        now_date = str_date

full_payment(757786.25, 7.91, (2029, 1, 15), (2022, 4, 16))
