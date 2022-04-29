from datetime import datetime

def month_count(end_of_period, day_mon_year):
    now_date = datetime(*day_mon_year)
    end_date = datetime(*end_of_period)
    return ((end_date.year - now_date.year) * 12 + (end_date.month - now_date.month)), end_date - now_date

def month_name(number):
    month = ['января', 'февраля', 'марта', 'апреля',
             'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    return month[number-1]