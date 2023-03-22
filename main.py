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

# timetable0 = pd.read_excel("timetable0.xlsx") # datetime.time
# timetable1 = pd.read_excel("timetable1.xlsx") # datetime.time
# timetable0 = timetable0.values.tolist()
# timetable1 = timetable1.values.tolist()
# timetables = [timetable0, timetable1]
# passenger_gen = prg.PassangerGenerator(2018, timetables)


#################################### PROTOTYPING #################################################
passenger_gen = prg.PassangerGenerator(2018)
passenger_gen.generate_passanger_rides()

#################################### PROTOTYPING #################################################

#################################### DATA_GENERATION #################################################