from datetime import datetime, timedelta
#from datetime import relativedelta
#import dateutil

def annuity_payment(ammount, procents, month):
    """Формула расчета аннуитетного платежа"""
    procent = (procents/12)/100
    pay_ammount = ammount*(procent/(1-(1+procent)**(-(month-1))))
    return pay_ammount

def calendar(date_in):
    year, month, day = date_in
    return datetime(year, month, day)


def next_date(date):
    date = str(date).split(' ')
    year, month, day = map(int, str(date[0]).split('-'))
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1
    return datetime(year, month, day)


def full_payment(ammount, procents, months, end_of_period, day_mon_year):
    summ = ammount
    date = calendar(day_mon_year)
    end_date = calendar(end_of_period)
    while summ > 0:
        date = next_date(date)
        payment = annuity_payment(ammount, procents, months)
        #Здесь следует переправить переменную year для избежания ValueError: month must be in 1..12
        print(f'{date}, размер платежа составит {round(payment, 2)}, остаток по кредиту составляет {round(summ, 2)}')
        summ -= payment



#print('Today: ', datetime.today().strftime('%d/%m/%Y'))
#print('After Month:', date_after_month.strftime('%d/%m/%Y'))

#def payment():
#print(calendar((2022, 2, 15)))
full_payment(748609, 7.91, 81, (2027, 2, 15), (2022, 2, 15))