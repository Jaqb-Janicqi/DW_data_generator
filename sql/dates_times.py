import calendar


class Time:
    def __init__(self, Id, hour, minute, second):
        self.Id = Id
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.Id},{self.hour},{self.minute},{self.second}"


class TimeGenerator:
    def __init__(self):
        self.times = []
        self.id = 0

    def generate_times(self):
        time_id = 0
        for hour in range(0, 24):
            for minute in range(0, 60):
                for second in range(0, 60):
                    time = Time(time_id, hour, minute, second)
                    self.times.append(time)
                    time_id += 1

    def to_csv(self):
        num = 0
        with open("times.csv", "w") as file:
            for time in self.times:
                if num != 0:
                    file.write('\n')
                file.write(str(time))
                num += 1


class Date:
    def __init__(self, Id, year, month, day):
        self.Id = Id
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = calendar.weekday(year, month, day)
        self.is_business_day = 1 if self.day_of_week not in ['Saturday', 'Sunday'] else 0
        self.season = self.get_season(month)

    def get_season(self, month):
        if month in [1, 2, 12]:
            return 'winter'
        if month in [3, 4, 5]:
            return 'spring'
        if month in [6, 7, 8]:
            return 'summer'
        if month in [9, 10, 11]:
            return 'autumn'

    def __str__(self):
        return f"{self.Id},{self.year},{self.month},{self.day},{self.day_of_week},{self.is_business_day},{self.season}"


class DateGenerator:
    def __init__(self):
        self.dates = []
        self.id = 0

    def generate_dates(self, start_year, end_year):
        date_id = 0
        calendar_obj = calendar.Calendar()
        for year in range(start_year, end_year):
            for month in range(1, 13):
                for day in calendar_obj.itermonthdates(year, month):
                    date = Date(date_id, day.year, day.month, day.day)
                    duplicate = False
                    for date_obj in self.dates:
                        if date_obj.day == date.day and date_obj.month == date.month and date_obj.year == date.year:
                            duplicate = True
                            break
                    if not duplicate:
                        self.dates.append(date)                    
                    date_id += 1

    def to_csv(self):
        num = 0
        with open("dates.csv", "w") as file:
            for date in self.dates:
                if num != 0:
                    file.write('\n')
                file.write(str(date))
                num += 1


time_generator = TimeGenerator()
time_generator.generate_times()
time_generator.to_csv()

date_generator = DateGenerator()
date_generator.generate_dates(2018, 2021)
date_generator.to_csv()
