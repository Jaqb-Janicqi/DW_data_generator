import csv
list=[]
for i in range(17):
    list.append(i)

def to_csv(list):
    with open("stations.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["id"])
        for i in list:
            writer.writerow([i])

to_csv(list)