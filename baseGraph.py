from baseObjectOriented import peopleList
import networkx as nx
from baseToCSV import hasSharedMovie, sharedMovies

g = nx.Graph() #instantiate graph object

g.add_nodes_from(peopleList) #adds each person as a node

#now add in edges behind people
for i in range(len(peopleList)):
    source = peopleList[i]
    for j in range(i + 1, len(peopleList)):
        target = peopleList[j]
        if hasSharedMovie(source, target) == True:
            #adds an edge if people have worked on same movie together
            g.add_edge(source, target)

            #add edge attribute of list of shared movies
            sharedList = sharedMovies(source, target)
            sharedListTitles = [t.title for t in sharedList]
            g.edge[source][target]['sharedList'] = sharedListTitles

            #add edge attribute of their collaboration score
            #collaboration score = average score of their shared movies
            totalBechdelScore = sum([movie.score for movie in sharedList])
            avBechdelScore = totalBechdelScore / len(sharedList)
            g.edge[source][target]['collaboration'] = avBechdelScore

print("Num of nodes: ",len(g.nodes())) #diagnostic, should be equal to len(peopleList)
print("Num of edges: ",len(g.edges())) #diagnostic, should be equal to rows in allConnections.csv

