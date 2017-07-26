from baseGraph import g, peopleList, nx
import csv
from baseToCSV import hasSharedMovie, sharedMovies

cliques = list(nx.find_cliques(g)) #finds all cliques
print("There are ", len(cliques), " cliques.")

#method from Datacamp intro to network analysis in python videos
def maximal_cliques(graph, n):
    """
    Finds all maximal cliques in graph that are of size `n`.
    """
    mcs = []
    for clique in list(nx.find_cliques(graph)):
        if len(clique) >= n:
            mcs.append(clique)
    return mcs

#want to examine the larger cliques
n = 10
topCliques = maximal_cliques(g, n)
print("There are ", len(topCliques), " cliques that have ", n, "+ people in them.")


#now we'll look at cliques with stronger edges (multiple collaborations required for each edge to count)
a = 6 #minimum number of people in the clique
b = 3 #minimum number of collaborations/shared movies for an edge to count
strongCliques = []
for clique in cliques:
    if len(clique) >= a:
        temp = set()
        for i in range(len(clique)):
            source = clique[i]
            count = 0
            for j in range(i+1, len(clique)):
                target = clique[j]
                if len(g.edge[source][target]['sharedList']) < b:
                    break
                else:
                    count += 1
            if count == len(clique) - i - 1:
                temp.add(source)
        if len(temp) >= a:
            strongCliques.append(list(temp))

print("There are ", len(strongCliques), " cliques with at least ", a, " members with edge strengths of at least ", b, ".")

'''
#get the names and common movies for each 'strong' clique
for clique in strongCliques:
    print([peep.name for peep in clique])
    sharedList = set(g[clique[0]][clique[1]]['sharedList'])
    for i in range(1, len(clique) - 1):
        sharedList = sharedList.intersection(set(g[clique[i]][clique[i+1]]['sharedList']))
    print(sharedList)
'''

#now write these 'strong' clique connections into a file for Cytoscape
with open('seriesCliques.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 av","person2", "person2 av", "sharedTitles", "numSharedTitles"]
    peopleWriter.writerow(newRow)

    #goes through peopleList and picks up each person's connections to everyone else
    numShared = []
    for clique in strongCliques:
        for i in range(len(clique)):
            source = clique[i]
            for j in range(i + 1, len(clique)):
                target = clique[j]
                sharedList = sharedMovies(source, target)
                sharedListTitles = [t.title for t in sharedList]
                totalBechdelScore = sum([movie.score for movie in sharedList])
                avBechdelScore = totalBechdelScore / len(sharedList)
                numShared.append(len(sharedList))
                peopleWriter.writerow([source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList),avBechdelScore])

csvfileW.close()
