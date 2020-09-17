import datetime as dt
import pytest as pt

def date(self):
    if date is None:
        date = dt.datetime.today()
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        status = 0
        today = (dt.datetime.today()).date()
        for record in self.records:
            if record.date == (dt.datetime.today()).date():
                status += record.amount
        return status

    def get_week_stats(self):
        status = 0
        today = (dt.datetime.today()).date()
        week_ago = today - dt.timedelta(days=6)
        for record in self.records:
            if week_ago <= record.date <= today:
                status += record.amount
        return status




class Record:
   def __init__(self, amount, comment,date = None):
       
       self.date   
       self.amount = amount
       self.comment = comment

       if type(date) is str:
           self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
       else:
           self.date = date


class CashCalculator(Calculator):

    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1

    def currencies_obj(self):
        return {'руб': self.RUB_RATE,
                'Euro': self.EURO_RATE,
                'USD': self.USD_RATE}

    def get_today_cash_remained(self,currency):
        CURRENCIES = {
            "rub": ("руб", 1),
            "usd": ("USD", self.USD_RATE),
            "eur": ("Euro", self.EURO_RATE),
        }

        remained = round(self.get_today_stats() / CURRENCIES[currency][0],2 )

        if remained > 0:
            return f'На сегодня осталось {remained} {self.CURRENCIES[currency]}'
        if remained == 0:
            return f'Денег нет, держись'
        return f'Денег нет, держись: твой долг - {remained} {self.CURRENCIES[currency]}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_sum = self.get_today_stats()
        calories = self.limit - today_sum

        if calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал'
        else:
            return f'Хватит есть!'


















