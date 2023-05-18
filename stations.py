import csv
list=['Kabaty', 'Natolin', 'Imielin','Stoklosy','Ursynow','Sluzew','Wilanowska','Wierzbno','Raclawicka','Pole Mokotowskie','Politechnika','Centrum Nauki Kopernik','Stadion Narodowy','Dworzec Wilenski','Szwedzka','Targowek Mieszkaniowy','Trocka','Mlociny']

def to_csv(list):
    with open("stations.csv", "w", newline='', encoding= "utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        for i in range(len(list)):
            writer.writerow([i, list[i]])

to_csv(list)