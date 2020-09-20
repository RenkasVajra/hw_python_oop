import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        status = 0
        today = dt.date.today()
        for record in self.records:
            if record.date == today:
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
   def __init__(self, amount, comment, date=None):
       self.amount = amount
       self.comment = comment

       if date is not None:
           self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
       else:
           self.date = dt.date.today()


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1
    CURRENCIES = {
        "usd": {"RATE": USD_RATE, 'name': 'USD'},
        "rub": {"RATE": RUB_RATE, 'name': "руб"},
        "eur": {'RATE': EURO_RATE, 'name': 'Euro'}
    }

    def get_today_cash_remained(self, currency):

        balance = self.limit - self.get_today_stats()
        remained = round(balance / self.CURRENCIES[currency]["RATE"], 2)
        amount = self.CURRENCIES[currency]["name"]
        abs1 = abs(remained)
        if balance > 0:
            return f'На сегодня осталось {remained} {amount}'
        if balance == 0:
            return f'Денег нет, держись'
        return f'Денег нет, держись: твой долг - {abs1} {amount} '


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_sum = self.get_today_stats()
        calories = self.limit - today_sum

        if calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал'
        return f'Хватит есть!'

