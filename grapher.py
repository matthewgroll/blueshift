import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

# create a nested list of ID, longitude, latitude
import csv

lim = 100


def readcsv(name):
    id_l_b = [[], [], [], [], []]
    with open(name) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row['parallax'] and row['phot_g_mean_flux']:
                id_l_b[0].append(row['source_id'])
                id_l_b[1].append(float(row['l']))
                id_l_b[2].append(float(row['b']))
                id_l_b[3].append(1/(float(row['parallax'])))
                id_l_b[4].append(float(row['phot_g_mean_flux']))

    return id_l_b


# l is galactic longitude
# b is galactic latitude

star_dicts = readcsv('GaiaSource-1000172165251650944-1000424567594791808.csv')
