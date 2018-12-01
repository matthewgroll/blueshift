import csv

def readcsv(name):
    id_l_b=[[],[],[]]
    with open(name) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            id_l_b[0].append(row['source_id'])
            id_l_b[1].append(row['l'])
            id_l_b[2].append(row['b'])
    return id_l_b

if __name__ == "__main__":
    print(readcsv('GaiaSource-1000172165251650944-1000424567594791808.csv'))