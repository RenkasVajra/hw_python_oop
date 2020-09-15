import datetime as dt
# columns (переменные)

limit = 2500


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    # Add in operation list(добавление в лист операций)
    def add_record(self, record):
        self.records.append(record)
    # Spent in a day (потрачено за день)
    def get_today_stats(self, records):
        now_time = dt.datetime.now()
        today_status = 0
        for record in self.records:

            if records.date == now_time:
                today_status += record.amount
        return today_status
    # Spent in a week (считает затраты за неделю)
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.today().date()
        delta_date = today - dt.timedelta(days=7)

        for record in self.records:
            if week_ago < record.date <= today:

                week_stats += record.amount
        return delta_date

   # Support class(вспомогательный класс)
class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = now_time
        self.comment = comment

        if type(date) is str:
            moment = dt.datetime.strptime(date, '%d.%m.%Y')
            self.date = moment.date()
        else:
            self.date = date

# Counts the number of calories spent
# (считает потраченные калории)
class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        today_calor_spent = super().get_today_stats()
        calor = self.limit - today_calor_spent
        if self.limit > today_nolim:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calor} кКал')
        else:
            print('Хватит есть!')
    def week_calories(self,get_week_stats,week_result):
        self.week_result = get_week_stats
        return f'За последнюю неделю всего получено {week_result} кКал'
# Calculate money spends
class CashCalculator(Calculator):
    def get_today_cash_remained(self,cours,limit,today_stats,cash,difference):
        EURO_RATE = 89
        USD_RATE = 75
        RUB_RATE = 1
        difference = limit - today_stats
        cours = {'USD':{'name':'USD','rate':self.USD_RATE},
                 'EUR':{'name':'EUR','rate':self.EURO_RATE},
                 'RUB':{'name':'RUB','rate':self.RUB_RATE}}


        if difference < limit:
            remainder = float
            return f'На сегодня осталось {difference} {cours}'

        elif difference >= limit:
            cash = float(abs(cash))
            return f'Денег нет, держись: твой долг {cash} {currency}'
        else:
            return f'Денег нет, держись'
# Week spends money
    def cash_spend_week(self, get_week_stats, cours):
        cash_spend = float(get_week_stats())

        return f'На неделе ты потратил {cash_spend} {cours}'
