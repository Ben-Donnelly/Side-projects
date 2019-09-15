from networkx import get_edge_attributes, get_node_attributes, draw, draw_networkx_edge_labels, Graph,\
    draw_networkx_labels, draw_networkx_nodes
from matplotlib import pyplot as plt
from itertools import combinations
from haversine import haversine
from time import time
from numpy import genfromtxt
import numpy as np
import re

start = time()
x = genfromtxt(r"C:\\Users\\Ben Donnelly\\Desktop\\coordinates.txt", delimiter=',', dtype=None, usecols=np.arange(0, 2))
for_later = {}
with open('C:\\Users\\Ben Donnelly\\Desktop\\coordinates.txt', 'r') as f:
    xi = (re.findall('[A-Za-z]+', f.read()))

d = { i : xi[i] for i in range(0, len(xi) ) }
# print(d)
# quit()

coordinates_list = []
for i in x:
    coordinates_list.append((tuple(i)))

dis_dic = {}  # dictionary for distances between points
count = 0

for i in coordinates_list:  # adds distances between co-ordinates to dis_dic
    for j in coordinates_list:

        dists = round(haversine(i, j), 5)
        if dists != 0.0 and dists not in dis_dic.values():
            # Ensures no duplicates (e.g. 1->2 & 2->1) and no 0 distances (e.g. 1->1, 2->2 e.t.c.)
            dis_dic[count] = dists  # Serial number = key
            count += 1

G = Graph()

for idx, val in enumerate(coordinates_list):
    G.add_node(idx, pos=val)

mix = list(combinations((i for i in range(G.number_of_nodes())), 2))
# List for all combinations of points for linking each point together in graph

G.add_edges_from(mix)

for ind, i in enumerate(dis_dic):
    G.add_weighted_edges_from([(mix[ind][0], mix[ind][1], dis_dic[ind])])

pos = get_node_attributes(G, 'pos')
plt.figure("Road trip", figsize=(50, 50))
draw(G, pos)
labels = get_edge_attributes(G, 'weight')
draw_networkx_edge_labels(G, pos, edge_labels=labels)

draw_networkx_labels(G, pos, font_size=10, font_color='k')
draw_networkx_nodes(G, pos, node_color='#14E032', alpha=1.0)
#plt.show()


tour = [0] * 31
count = 0
county_nums = [0] * 31
p = 0
prev_node = 0
while 0.0 in tour:
    cost = 10000
    for i, j in G.adj[p].items():
        if j['weight'] < cost:
            cost = j['weight']
            county_nums[count] = i
            tour[count] = d[i]
            p = i
    count += 1
    G.remove_node(prev_node)
    prev_node = p

tour.insert(0, "Dublin")
tour.append("Dublin")
print(tour)
print(county_nums)
end = time()
print(end - start)
