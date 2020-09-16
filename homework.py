import datetime as dt
import pytest as pt

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
   def __init__(self, amount, comment,date = (dt.datetime.today()).date()):
       self.amount = amount
       self.comment = comment

       if type(date) is str:
           self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
       else:
           self.date = date


class CashCalculator(Calculator):
    EURO_RATE = 70
    USD_RATE = 60
    CURRENCIES = {
        "usd":{"RATE":USD_RATE,'name': 'USD'},
        "rub":{"RATE": 1, 'name': "руб"},
        "eur":{'RATE': EURO_RATE, 'name':'Euro'}
        }

    def get_today_cash_remained(self,currency):
        remained = self.limit - self.get_today_stats()

        if remained > 0:
            return f'На сегодня осталось {remained} {currency}'
        elif remained == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {remained} {currency}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()

        if balance > 0:
            print (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал')
        else:
            print (f'Хватит есть!')












