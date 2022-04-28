import datetime
#from datetime import relativedelta
import dateutil

def annuity_payment(ammount, procents, month):
    """Формула расчета аннуитетного платежа"""
    procent = (procents/12)/100
    pay_ammount = ammount*(procent/(1-(1+procent)**(-(month-1))))
    return pay_ammount

def full_payment(ammount, procents, months, day_mon_year):
    summ = ammount
    mounth_num = 0
    while summ > 0:
        payment = annuity_payment(ammount, procents, months)
        #Здесь следует переправить переменную year для избежания ValueError: month must be in 1..12
        day, month, year = day_mon_year
        if month < 12:
            month += mounth_num
        else:
            month = 1
            year += 1
        date = datetime.date(day, month, year).isoformat()
        print(f'{date}, размер платежа составит {round(payment, 2)}, остаток по кредиту составляет {round(summ, 2)}')
        summ -= payment
        mounth_num += 1

#print('Today: ', datetime.today().strftime('%d/%m/%Y'))
#print('After Month:', date_after_month.strftime('%d/%m/%Y'))

#def payment():

full_payment(748609, 7.91, 82, (2022, 2, 15))