import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar


def working_day_distribution():
    morning_peak = np.random.normal(7.5, 1.6, 7000)
    all_day = np.random.uniform(0, 24, 1000)
    mid_day = np.random.normal(12, 4, 2000)
    evening_peak = np.random.normal(16.5, 1.7, 7000)
    data = np.concatenate((morning_peak, all_day, evening_peak, mid_day))
    data = data[data < 24]
    data = data[data >= 0]
    return data


def friday_distribution():
    morning_peak = np.random.normal(7.5, 1.6, 7000)
    all_day = np.random.uniform(0, 24, 1000)
    mid_day = np.random.normal(12, 4, 2000)
    evening_peak = np.random.normal(16.5, 1.7, 7000)
    night_peak1 = np.random.normal(23.5, 1.3, 1000)
    night_peak2 = np.random.normal(0.5, 1.1, 700)
    data = np.concatenate(
        (morning_peak, all_day, evening_peak, mid_day, night_peak1, night_peak2))
    data = data[data < 24]
    data = data[data >= 0]
    # plt.hist(data, bins=1440, alpha=0.5, label='gamma')
    # plt.show()
    return data


def weekend_distribution():
    all_day = np.random.uniform(0, 24, 2000)
    mid_day = np.random.normal(12, 4, 3000)
    data = np.concatenate((all_day, mid_day))
    data = data[data < 24]
    data = data[data >= 0]
    # plt.hist(data, bins=1440, alpha=0.5, label='gamma')
    # plt.show()
    return data


class PassangerRide:
    def __init__(self, entry_section_id, exit_section_id, id, entry_time, exit_time):
        self.entry_section_id = entry_section_id
        self.exit_section_id = exit_section_id
        self.id = id
        self.entry_time = entry_time
        self.exit_time = exit_time

    def __str__(self):
        # return all attributes in csv
        return f"{self.entry_section_id},{self.exit_section_id},{self.id},{self.entry_time},{self.exit_time}"


class PassangerGenerator:
    sections = [1, 3, 2, 1, 3, 1, 2, 2, 1, 3, 1,
                2, 3, 1, 3, 1]  # station0->1, station1->2

    def __init__(self, year):
        self.id = 0
        self.num_sections = 16
        self.passanger_rides = []
        self.pasanger_rides_length = 0
        self.calendar_obj = calendar.Calendar()
        # generate calendar tuples for the year
        self.calendar_tuples = self.calendar_obj.yeardatescalendar(year, 12)
        # reshape calendar tuples to a list of dates
        self.dates = [
            date for month in self.calendar_tuples for week in month for day in week for date in day]

    def generate_passanger_rides(self):
        for date in self.dates:
            # self.pasanger_rides_length = len(self.passanger_rides) # debug
            dist = None
            if date.weekday() == 5 or date.weekday() == 6:
                dist = weekend_distribution()
            elif date.weekday() == 4:
                dist = friday_distribution()
            else:
                dist = working_day_distribution()
            # plt.hist(dist, bins=1440, alpha=0.5, label='gamma')   # debug
            # plt.show()    # debug
            for minute_floor in range(1440):
                # distribution is in hours, we are interested in 1 minute intervals
                minute_ceil = minute_floor + 1
                condition = (dist >= minute_floor) & (dist < minute_ceil)
                # num_passangers = np.count_nonzero(condition)
                num_passangers = np.extract(condition, dist).size
                hour = int(minute_floor/60)
                minute = minute_floor % 60
                self.generate_ride(date, num_passangers, hour, minute)

    # załadować excela, zobaczyć najbliższy pociąg i dopiero liczyć czas przejazdu
    def generate_ride(self, date, num_passangers, hour, minute):
        for i in range(num_passangers):
            exit_section_id = entry_section_id = np.random.randint(
                1, self.num_sections + 1)
            while exit_section_id == entry_section_id:
                exit_section_id = np.random.randint(0, self.num_sections)
            if entry_section_id < exit_section_id:
                travel_time = sum(
                    self.sections[entry_section_id:exit_section_id])
            else:
                travel_time = sum(
                    self.sections[exit_section_id:entry_section_id])
            entry_time = calendar.datetime.datetime(
                date.year, date.month, date.day, hour, minute, np.random.randint(0, 60))
            exit_time = entry_time + \
                calendar.datetime.timedelta(minutes=travel_time)
            exit_sec = entry_time.second
            while exit_sec == entry_time.second:
                exit_sec = np.random.randint(0, 60)
            exit_time = exit_time.replace(second=exit_sec)
            # print(entry_time) # debug
            # print(exit_time) # debug
            passenger_ride = PassangerRide(
                entry_section_id, exit_section_id, self.id, entry_time, exit_time)
            self.passanger_rides.append(passenger_ride)
            self.id += 1
