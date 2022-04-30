from datetime import date
import functional as func

class Credit():
    def __init__(self):
        amount, procent, end_date, start_date = func.data_inputs()
        self.sum = amount
        self.procents = procent
        self.now_date = date(*start_date)
        self.months, self.days = func.month_count(end_date, start_date)
        self.pay_for_day = func.annuity_payment(self.sum, self.procents, month = self.months)
        self.pay_for_month = func.annuity_payment(self.sum, self.procents, month=self.months)

class Annoy_payment(Credit):
    def schedule(self):
        """Функция расчета размера платежа"""
        while self.sum > 0:
            pay_date = func.next_date(self.now_date)
            print(f'На {pay_date.day} {func.month_name(pay_date.month)} {pay_date.year} '
                  f'года размер ежемесячного платежа составит {round(self.pay_for_month, 2)}, '
                  f'остаток по кредиту составляет {round(self.sum, 2)}')
            self.sum -= self.pay_for_month
            self.now_date = pay_date

if __name__ == '__main__':
    main = Credit()


