from datetime import date
import functional as func

class Credit():
    def __init__(self, ammount, procents, end_of_period, day_mon_year):
        self.sum = ammount
        self.procents = procents
        self.now_date = date(*day_mon_year)
        self.months, self.days = func.month_count(end_of_period, day_mon_year)
        self.pay_for_day = func.annuity_payment(self.sum, self.procents, month = self.months)
        self.pay_for_month = func.annuity_payment(self.sum, self.procents, month=self.months)

class Annoy_payment(Credit):
    def full_payment(self):
        """Функция расчета размера платежа"""
        while self.sum > 0:
            str_date = func.next_date(self.now_date)
            print(f'На {str_date.day} {func.month_name(str_date.month)} {str_date.year} '
                  f'года размер ежемесячного платежа составит {round(self.pay_for_month, 2)}, '
                  f'остаток по кредиту составляет {round(self.sum, 2)}')
            self.sum -= self.pay_for_month
            self.now_date = str_date

if __name__ == '__main__':
    main = Credit()
