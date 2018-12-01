import csv

def readcsv(name):
    dic = {}
    with open(name) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            dic[row['source_id']] = (row['l'],row['b'])
    return dic

if __name__ == "__main__":
    print(readcsv('GaiaSource-1000172165251650944-1000424567594791808.csv'))