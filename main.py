import pandas as pd
import passanger_ride as pr
from train_generator import TrainGenerator as tg, Train as t
from scheduled_section import ScheduledSection, ScheduledSectionGenerator as ssg
import real_section as rs
import distributions as dist
import time
import datetime
import numpy as np


tic = time.perf_counter()
snapshots_made = 0


def snapshot(trains, scheduled_sections, ride_id, real_sections, passanger_rides):
    with open(f'data/trains{snapshots_made}.csv', 'w', encoding='UTF-8') as file1:
        for train in trains:
            file1.write(str(train) + '\n')
    with open(f'data/scheduled_sections{snapshots_made}.csv', 'w', encoding='UTF-8') as file2:
        for scheduled_section in scheduled_sections:
            file2.write(str(scheduled_section) + '\n')
    with open(f'data/real_sections{snapshots_made}.csv', 'w', encoding='UTF-8') as file3:
        for real_section in real_sections:
            file3.write(str(real_section) + '\n')
    with open(f'data/passanger_rides{snapshots_made}.csv', 'w', encoding='UTF-8') as file4:
        for passanger_ride in passanger_rides:
            file4.write(str(passanger_ride) + '\n')
    with open(f'data/rides{snapshots_made}.csv', 'w', encoding='UTF-8') as file5:
        for ride in range(ride_id + 1):
            file5.write(str(ride) + '\n')


simulation_start_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
current_time = simulation_start_time
simulation_end_time = datetime.datetime(2021, 1, 5, 0, 0, 0)
section_times = [1, 3, 2, 1, 3, 1, 2, 2, 1, 3,
                 1, 2, 3, 1, 3, 1]  # station0->1, station1->2

timetable0 = pd.read_excel("timetable0.xlsx")  # datetime.time
timetable1 = pd.read_excel("timetable1.xlsx")  # datetime.time
timetable0 = timetable0.values.tolist()
timetable1 = timetable1.values.tolist()
timetables = [timetable0, timetable1]  # datetime.time

distributions = dist.Distributions()

train_generator = tg(50, section_times)

scheduled_sections = []
scheduled_section_id = 0

passanger_rides = []

real_sections = []
metro_line = [[] for _ in range(len(section_times))]
real_section_id = 0
ride_id = 0
passanger_id = 0
minute = 0
while current_time < simulation_end_time:
    for station in metro_line:  # generate passangers for each station
        passanger_amount = distributions.passanger_amount(
            minute, current_time.weekday() + 1)
        for _ in range(passanger_amount):
            start_station_id = None
            end_station_id = None
            while start_station_id == end_station_id:
                start_station_id = np.random.randint(0, len(section_times))
                end_station_id = np.random.randint(0, len(section_times))
            passanger = pr.PassangerRide(
                passanger_id, start_station_id, end_station_id, current_time)
            station.append(passanger)
            passanger_id += 1
    # if current_time.time() is in timetable, start a new ride
    for timetable_id in range(len(timetables)):
        for scheduled_ride in timetables[timetable_id]:
            if current_time.time() == scheduled_ride[0]:
                # make snapshot in such way that scd changes between time periods
                if len(train_generator.free_trains) <= 0 and snapshots_made == 0:
                    snapshot(train_generator.trains, scheduled_sections, ride_id, real_sections, passanger_rides)
                    train_generator.update_trains()
                    snapshots_made += 1
                train = train_generator.get_free_train()
                direction_of_ride = 1 if timetable_id == 0 else -1
                start_station = 0 if direction_of_ride == 1 else len(
                    section_times) - 1
                sections = []
                section_start_station = start_station
                arrival_time = current_time
                for i in range(len(section_times)):
                    section_end_station = section_start_station + direction_of_ride
                    arrival_time = arrival_time + \
                        datetime.timedelta(minutes=section_times[i])
                    sections.append(ScheduledSection(
                        scheduled_section_id, section_start_station, section_end_station, arrival_time))
                    scheduled_section_id += 1
                    scheduled_sections.append(sections[-1])
                train.start_ride(start_station, ride_id,
                                 direction_of_ride, current_time, sections)
                ride_id += 1
    # for each train, check if it is on the station, if so, (un)board passangers and move to next station
    for train in train_generator.trains:
        if train.is_on_station(current_time):
            real_sections.append(train.next_station(
                metro_line, real_section_id, passanger_rides))
            real_section_id += 1
        if train.is_free == True:
            train_generator.free_train(train)
    minute += 1
    current_time += datetime.timedelta(minutes=1)

snapshot(train_generator.trains, scheduled_sections,
         ride_id, real_sections, passanger_rides)
print(f"Rides made: {ride_id}")  # debug


toc = time.perf_counter()
print(f"Generated data in {toc - tic:0.4f} seconds")
