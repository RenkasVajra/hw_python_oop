import datetime as dt
import pytest as pt

class Calculator:
    limit = 2500
    def __init__(self,limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self,records):
        now_time = dt.datetime.now()
        today_status = 0
        for record in records:

            if records.date == now_time:
                today_status += record.amount
        return today_status

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.today()
        delta_date = today - dt.timedelta(days=7)
        for record in self.records:
            if delta_date <= record.date <= today:
                week_stats += record.amount
        return delta_date




class Record:
   def __init__(self, amount, comment,date = (dt.datetime.today()).date()):
       self.amount = amount
       self.comment = comment
       if type(date) is str:
           self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
       else:
           self.date = date


class CashCalculator(Calculator):
    EURO_RATE = 80
    USD_RATE = 75
    RUB_RATE = 1
    CURRENCIES = {
        "rub": ["руб", 1],
        "usd": ["USD", USD_RATE],
        "eur": ["Euro", EURO_RATE],
    }

    def get_today_cash_remained(self,currency):


        remained = self.limit - self.get_today_status()
        if remained < self.limit:
            return f'На сегодня осталось {remained} {currency}'
        elif remainednder == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {remained} {currency}'

    def get_week_cash_remained(self,currency):
        weekly_remain = self.get_week_stats()
        return f'За последнюю неделю было потрачено {weekly_remain} {currency}'
class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал')
        else:
            print(f'Хватит есть!')
