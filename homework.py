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
    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1
    CURRENCIES = {
        "usd":{"RATE":USD_RATE,'name': 'USD'},
        "rub":{"RATE": RUB_RATE, 'name': "руб"},
        "eur":{'RATE': EURO_RATE, 'name':'Euro'}
        }

     def get_today_cash_remained(self, currency):
        remains = abs(self.limit - self.get_today_stats())
        for cash in self.currencies.keys():
            if cash == currency:
                rate = cash[1]
                cash_remains = round((remains / rate), 2)
                money_name = cash[0]
                if cash_remains > 0:
                    return f"На сегодня осталось {cash_remains} {money_name}"
                elif cash_remains == 0:
                    return f"Денег нет, держись"
                return f"Денег нет, держись: твой долг {cash_remains} {money_name}"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.limit - self.get_today_stats()

        if calories < self.limit:
            print (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал')
        else:
            print (f'Хватит есть!')




