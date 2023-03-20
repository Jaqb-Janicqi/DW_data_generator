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
    return data

def friday_distribution():
    morning_peak = np.random.normal(7.5, 1.6, 7000)
    all_day = np.random.uniform(0, 24, 1000)
    mid_day = np.random.normal(12, 4, 2000)
    evening_peak = np.random.normal(16.5, 1.7, 7000)
    night_peak1 = np.random.normal(23.5, 1.3, 1000)
    night_peak2 = np.random.normal(0.5, 1.1, 700)
    data = np.concatenate((morning_peak, all_day, evening_peak, mid_day, night_peak1, night_peak2))
    data = data[data < 24]
    data = data[data > 0]
    # plt.hist(data, bins=1440, alpha=0.5, label='gamma')
    # plt.show()
    return data

def weekend_distribution():
    all_day = np.random.uniform(0, 24, 2000)
    mid_day = np.random.normal(12, 4, 3000)
    data = np.concatenate((all_day, mid_day))
    data = data[data < 24]
    data = data[data > 0]
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
    def __init__(self, year):
        self.id = 0
        self.num_stations = 16
        self.passanger_rides = []
        self.calendar_obj = calendar.Calendar()
        # generate calendar tuples for the year
        self.calendar_tuples = self.calendar_obj.yeardatescalendar(year, 12)
        self.weekend = weekend_distribution()
        self.working_day = working_day_distribution()

    def generate_passanger_rides(self, num_passangers, weekday):
        for i in range(num_passangers):
            for minute in range(1440):
                if weekday == 5 or weekday == 6:
                    self.x = weekend_distribution[minute]
                else:
                    self.x = working_day_distribution[minute]
                if self.x > 0 and self.x < 24:
                    entry_section_id = np.random.randint(1, self.num_stations + 1)
                    exit_section_id = np.random.randint(1, self.num_stations + 1)
                    while exit_section_id == entry_section_id:
                        exit_section_id = np.random.randint(1, self.num_stations)
                    passenger_ride = PassangerRide(entry_section_id, exit_section_id, self.id, None, None)
                    self.passanger_rides.append(passenger_ride)
                    self.id += 1

# passenger_gen = PassangerGenerator(2018)
# print (passenger_gen.calendar_tuples[0][0][0][0])
# print (passenger_gen.calendar_tuples[0][0][0][0].weekday())
# print (passenger_gen.calendar_tuples[0][0][0][1].weekday())
# print (passenger_gen.calendar_tuples[0][0][0][6])

# print (passenger_gen.calendar_tuples[0][0][0][0].year)
# print (passenger_gen.calendar_tuples[0][0][0])
dist = weekend_distribution()

hist, bins = np.histogram(dist, bins=1439)
print(hist.size)
print(bins[0].shape)

