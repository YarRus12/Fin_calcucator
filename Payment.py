from datetime import datetime


def annuity_payment(ammount, procents, month):
    """Формула расчета аннуитетного платежа"""
    procent = (procents/12)/100
    pay_ammount = ammount*(procent/(1-(1+procent)**(-(month-1))))
    return pay_ammount

def full_payment(ammount, procents, month, date):
    summ = ammount
    while summ > 0:
        payment = annuity_payment(ammount, procents, month)
        date = datetime.date(date)
        print(f'{date}, размер платежа составит {round(payment, 2)}, остаток по кредиту составляет {round(summ, 2)}')
        summ -= payment
        mounth_num += 1




#full_payment(748609, 7.91, 82, (2022, 2, 15))