import pandas as pd
import passanger_ride_generator as prg
import train_generator as tg
import event_generator as eg
import scheduled_section as ss
import real_section_generator as rsg


############## HOOBI tutorial section ##############
# types = ["delay", "breakdown"]
# x = np.random.randint(0, 2)
# types[x]
# delay = np.random.choice([0, 1], p=[0.9, 0.1])
############## HOOBI tutorial section ##############


#################################### PROTOTYPING #################################################

#################################### PROTOTYPING #################################################


#################################### DATA_GENERATION #################################################
timetable0 = pd.read_excel("timetable0.xlsx")  # datetime.time
timetable1 = pd.read_excel("timetable1.xlsx")  # datetime.time
timetable0 = timetable0.values.tolist()
timetable1 = timetable1.values.tolist()
timetables = [timetable0, timetable1]

train_gen = tg.TrainGenerator()
train_gen.generate_trains(100)
train_gen.to_csv()

event_gen = eg.EventGenerator()
event_gen.generate_events(100)
event_gen.to_csv()

scheduled_section_generator = ss.ScheduledSectionGenerator(2018, timetables)
scheduled_section_generator.generate_scheduled_sections()
scheduled_section_generator.to_csv()

real_section_generator = rsg.RealSectionGenerator(
    scheduled_section_generator.scheduled_sections, event_gen.events, train_gen.trains, 2018, 17, 100)
real_section_generator.generate_real_sections()
real_section_generator.to_csv()

passenger_gen = prg.PassangerGenerator(2018, timetables)
passenger_gen.generate_passanger_rides()
passenger_gen.to_csv()
