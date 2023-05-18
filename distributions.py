import numpy as np
import matplotlib.pyplot as plt


class Distributions:
    def __init__(self):
        self.workday = self.working_day_distribution()
        self.friday = self.friday_distribution()
        self.weekend = self.weekend_distribution()

    def show(self, data):
        plt.hist(data, bins=24, alpha=0.5, label='gamma')
        plt.show()

    def working_day_distribution(self):
        morning_peak = np.random.normal(7.5*60, 1.6*60, 7000)
        all_day = np.random.uniform(0, 24*60, 1000)
        mid_day = np.random.normal(12*60, 4*60, 2000)
        evening_peak = np.random.normal(16.5*60, 1.7*60, 7000)
        data = np.concatenate((morning_peak, all_day, evening_peak, mid_day))
        data = data[data < 24*60]
        data = data[data >= 0]
        return data

    def friday_distribution(self):
        morning_peak = np.random.normal(7.5*60, 1.6*60, 7000)
        all_day = np.random.uniform(0, 24*60, 1000)
        mid_day = np.random.normal(12*60, 4*60, 2000)
        evening_peak = np.random.normal(16.5*60, 1.7*60, 7000)
        night_peak1 = np.random.normal(23.5*60, 1.3*60, 1000)
        night_peak2 = np.random.normal(0.5*60, 1.1*60, 700)
        data = np.concatenate(
            (morning_peak, all_day, evening_peak, mid_day, night_peak1, night_peak2))
        data = data[data < 24*60]
        data = data[data >= 0]
        return data

    def weekend_distribution(self):
        all_day = np.random.uniform(0, 24*60, 2000)
        mid_day = np.random.normal(12*60, 4*60, 3000)
        night_peak1 = np.random.normal(23.5*60, 1.3*60, 1000)
        night_peak2 = np.random.normal(0.5*60, 1.1*60, 700)
        data = np.concatenate((all_day, mid_day, night_peak1, night_peak2))
        data = data[data < 24*60]
        data = data[data >= 0]
        return data

    def passanger_amount(self, minute, weekday):
        data = None
        if weekday < 5:
            data = self.workday
        elif weekday == 5:
            data = self.friday
        else:
            data = self.weekend
        # self.show(data)
        data = data[data >= minute]
        data = data[data < minute + 1]
        return len(data)