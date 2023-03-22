import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import passanger_ride_generator as prg


############## HOOBI tutorial section ##############
# types = ["delay", "breakdown"]
# x = np.random.randint(0, 2)
# types[x]
# delay = np.random.choice([0, 1], p=[0.9, 0.1])
############## HOOBI tutorial section ##############


#################################### PROTOTYPING#################################################
passenger_gen = prg(2018)
passenger_gen.prg()
print(passenger_gen.id)
# pandas to csv
# df = pd.DataFrame(passenger_gen.passanger_rides)
# df.to_csv("passanger_rides.csv", index=False, header=False)
#################################### PROTOTYPING#################################################

# passenger_gen.to_csv()
timetables = pd.read_excel("timetables.xlsx")
timetable0 = timetables[2:91] # datetime.time
timetable1 = timetables[96:185]
print(timetable0.shape)
timetables = [timetable0, timetable1]
passenger_gen = prg.PassangerGenerator(2018, timetables)
passenger_gen.generate_passanger_rides()
# print(timetables[0])
#################################### PROTOTYPING #################################################

#################################### DATA_GENERATION #################################################