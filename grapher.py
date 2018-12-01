import numpy as np
import matplotlib.pyplot as plt
import csv

# create a nested list of ID, longitude, latitude
import csv


def readcsv(name):
    id_l_b = [[], [], []]
    with open(name) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            id_l_b[0].append(row['source_id'])
            id_l_b[1].append(float(row['l']))
            id_l_b[2].append(float(row['b']))
    return id_l_b


if __name__ == "__main__":
    print(readcsv('GaiaSource-1000172165251650944-1000424567594791808.csv'))

# l is galactic longitude
# b is galactic latitude

star_dicts = readcsv('GaiaSource-1000172165251650944-1000424567594791808.csv')

plt.plot([star_dicts[1]], [star_dicts[2]], 'ro', markersize=1)
plt.axis([158, 160, 22, 24])
plt.show()





