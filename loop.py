import random
from collections import defaultdict
import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter


outcomes = []
for i in range(0,1000,1):
    prisoners = [*range(1,101,1)]
    box_num = [*range(1,101,1)]

    boxes = {}

    random.shuffle(prisoners)

    for box in box_num:
        boxes[box] = prisoners[box -1]

    G = nx.DiGraph()
    G.add_edges_from(boxes.items())


    c = nx.recursive_simple_cycles(G)
    #plt.figure(figsize=(20,10)) 
    #nx.draw_networkx(G)

    cycles = sorted(c)

    #If we set default to true, and then switch it when a prisoner lands on a cycle longer than 50, it fails everybody.
    overall_success = "Success"

    #simulating prisoners by checking the length of the loop that they exist on. If it's too long, success = false.
    for prisoner in prisoners:
        found = False
        for c in cycles:
            if(prisoner in c):
                if(len(c) > 50): overall_success = "Unsuccessful"

    outcomes.append(overall_success)
unsuccessfuls = sum('Unsuccessful' in s for s in outcomes)
successfuls = sum('Success' in s for s in outcomes)
  
print("Unsuccessful:", unsuccessfuls, "Successful:", successfuls,  "Percentage Success:", round((successfuls / len(outcomes)) * 100,2), "%")