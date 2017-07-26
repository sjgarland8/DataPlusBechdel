import networkx as nx
import matplotlib.pyplot as plt
import csv

'''
Set up and draw character network of Pacific Rim.
'''

g = nx.Graph() #instantiate graph



'''
This includes all characters who speak.
'''

characters = ["Construction foreman", "Construction worker", "Yancy Becket", "Raleigh Becket", "Chuck Hansen", "beach grandfather", "beach grandson", "Herc Hansen", "Ops Tendo Choi", "tech", "Mako Mori", "Stacker Pentecost", "Dr. Newton Geiszler", "Dr. Hermann Gottlieb", "shelter woman", "L. Cole", "L. Taylor", "Hannibal Chau", "Chau shop worker", "Chau worker", "Wei Tang brothers", "Sasha Kaidenovsky", "Alexis Kaidenovsky"]

g.add_nodes_from(characters)

#single outside connections
g.add_edge("Construction foreman", "Construction worker")
g.add_edge("Sasha Kaidenovsky", "Alexis Kaidenovsky")
g.add_edge("beach grandfather", "beach grandson")

raleighPeeps = ["Construction foreman", "Yancy Becket", "Chuck Hansen", "Ops Tendo Choi", "Mako Mori", "Dr. Hermann Gottlieb", "Stacker Pentecost", "Dr. Newton Geiszler", "Herc Hansen", "Chuck Hansen"]
for peep in raleighPeeps:
    g.add_edge("Raleigh Becket", peep)

tendoPeeps = ["tech", "Yancy Becket", "Raleigh Becket", "Chuck Hansen", "Herc Hansen", "Dr. Newton Geiszler", "Stacker Pentecost", "Dr. Hermann Gottlieb", "Mako Mori"]
for peep in tendoPeeps:
    g.add_edge("Ops Tendo Choi", peep)

makoPeeps = ["Ops Tendo Choi", "Raleigh Becket", "Chuck Hansen", "Herc Hansen", "Stacker Pentecost"]
for peep in makoPeeps:
    g.add_edge("Mako Mori", peep)

hermannPeeps = ["Ops Tendo Choi", "Raleigh Becket", "Stacker Pentecost", "Herc Hansen", "Dr. Newton Geiszler"]
for peep in hermannPeeps:
    g.add_edge("Dr. Hermann Gottlieb", peep)

newtPeeps = ["Chuck Hansen", "Herc Hansen", "Raleigh Becket", "Ops Tendo Choi", "Stacker Pentecost", "Dr. Hermann Gottlieb", "shelter woman", "Hannibal Chau", "Chau shop worker"]
for peep in newtPeeps:
    g.add_edge("Dr. Newton Geiszler", peep)

hercPeeps = ["Chuck Hansen", "Raleigh Becket", "Ops Tendo Choi", "Mako Mori", "Stacker Pentecost", "Dr. Hermann Gottlieb", "Dr. Newton Geiszler"]
for peep in hercPeeps:
    g.add_edge("Herc Hansen", peep)

chuckPeeps = ["Raleigh Becket", "Ops Tendo Choi", "Mako Mori", "Stacker Pentecost", "Herc Hansen", "Dr. Newton Geiszler"]
for peep in chuckPeeps:
    g.add_edge("Chuck Hansen", peep)

hannibalPeeps = ["Dr. Newton Geiszler", "Chau shop worker", "Chau worker"]
for peep in hannibalPeeps:
    g.add_edge("Hannibal Chau", peep)

stackerPeeps = ["L. Cole", "L. Taylor", "Herc Hansen", "Chuck Hansen", "Raleigh Becket", "Yancy Becket", "Ops Tendo Choi", "Mako Mori", "Dr. Hermann Gottlieb", "Wei Tang brothers", "Sasha Kaidenovsky", "Alexis Kaidenovsky", "Dr. Newton Geiszler"]
for peep in stackerPeeps:
    g.add_edge("Stacker Pentecost", peep)

#nx.draw(g)
#plt.show()

'''
This includes only those with names
'''
'''
characters = ["Yancy Becket", "Raleigh Becket", "Chuck Hansen", "Herc Hansen", "Ops Tendo Choi", "Mako Mori", "Stacker Pentecost", "Dr. Newton Geiszler", "Dr. Hermann Gottlieb", "L. Cole", "L. Taylor", "Hannibal Chau", "Wei Tang brothers", "Sasha Kaidenovsky", "Alexis Kaidenovsky"]

g.add_nodes_from(characters)

#single outside connections
g.add_edge("Sasha Kaidenovsky", "Alexis Kaidenovsky")

raleighPeeps = ["Yancy Becket", "Chuck Hansen", "Ops Tendo Choi", "Mako Mori", "Dr. Hermann Gottlieb", "Stacker Pentecost", "Dr. Newton Geiszler", "Herc Hansen", "Chuck Hansen"]
for peep in raleighPeeps:
    g.add_edge("Raleigh Becket", peep)

tendoPeeps = ["Yancy Becket", "Raleigh Becket", "Chuck Hansen", "Herc Hansen", "Dr. Newton Geiszler", "Stacker Pentecost", "Dr. Hermann Gottlieb", "Mako Mori"]
for peep in tendoPeeps:
    g.add_edge("Ops Tendo Choi", peep)

makoPeeps = ["Ops Tendo Choi", "Raleigh Becket", "Chuck Hansen", "Herc Hansen", "Stacker Pentecost"]
for peep in makoPeeps:
    g.add_edge("Mako Mori", peep)

hermannPeeps = ["Ops Tendo Choi", "Raleigh Becket", "Stacker Pentecost", "Herc Hansen", "Dr. Newton Geiszler"]
for peep in hermannPeeps:
    g.add_edge("Dr. Hermann Gottlieb", peep)

newtPeeps = ["Chuck Hansen", "Herc Hansen", "Raleigh Becket", "Ops Tendo Choi", "Stacker Pentecost", "Dr. Hermann Gottlieb", "Hannibal Chau"]
for peep in newtPeeps:
    g.add_edge("Dr. Newton Geiszler", peep)

hercPeeps = ["Chuck Hansen", "Raleigh Becket", "Ops Tendo Choi", "Mako Mori", "Stacker Pentecost", "Dr. Hermann Gottlieb", "Dr. Newton Geiszler"]
for peep in hercPeeps:
    g.add_edge("Herc Hansen", peep)

chuckPeeps = ["Raleigh Becket", "Ops Tendo Choi", "Mako Mori", "Stacker Pentecost", "Herc Hansen", "Dr. Newton Geiszler"]
for peep in chuckPeeps:
    g.add_edge("Chuck Hansen", peep)

hannibalPeeps = ["Dr. Newton Geiszler"]
for peep in hannibalPeeps:
    g.add_edge("Hannibal Chau", peep)

stackerPeeps = ["L. Cole", "L. Taylor", "Herc Hansen", "Chuck Hansen", "Raleigh Becket", "Yancy Becket", "Ops Tendo Choi", "Mako Mori", "Dr. Hermann Gottlieb", "Wei Tang brothers", "Sasha Kaidenovsky", "Alexis Kaidenovsky", "Dr. Newton Geiszler"]
for peep in stackerPeeps:
    g.add_edge("Stacker Pentecost", peep)
'''


'''
Find and print out all cliques.
'''
cliques = nx.find_cliques(g)
for clique in cliques:
    if len(clique) > 2:
        print(clique)

'''
Investigate centrality scores of the characters.
'''

dictCloseness = nx.closeness_centrality(g)
closeScores = sorted([(b,a) for a,b in dictCloseness.items()])
print(closeScores)

dictBetweenness = nx.betweenness_centrality(g)
betweenScores = sorted([(b,a) for a,b in dictBetweenness.items()])
print(betweenScores)


'''
Writes csv file for Cytoscape visualization
'''

with open('pacificRim.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["source", "target"]
    peopleWriter.writerow(newRow)
    for (a,b) in list(g.edges()):
        peopleWriter.writerow([a,b])
