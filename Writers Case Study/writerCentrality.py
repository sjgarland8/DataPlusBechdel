from baseObjectOriented import peopleList, movieList
import networkx as nx
from baseToCSV import hasSharedMovie, sharedMovies
import operator
import csv

#create a list of all writers from peopleList and only include writers (and writer credits)
writerList = []
for person in peopleList:
    movies = [a for a in person.movie if a[1] == "w"]
    if len(movies) != 0:
        writerList.append(person)
print(len(writerList))
#just for giggles, do the same for directors and producers
'''
directorList = []
for person in peopleList:
    movies = [a for a in person.movie if a[1] == "d"]
    if len(movies) != 0:
        directorList.append(person)
print(len(directorList))

producerList = []
for person in peopleList:
    movies = [a for a in person.movie if a[1] == "p"]
    if len(movies) != 0:
        producerList.append(person)
print(len(producerList))
'''
#CREATES GRAPH OF WRITERS
#taken from baseGraph, rewritten to work with peopleList
g = nx.Graph() #instantiate graph object

g.add_nodes_from(writerList) #adds each person as a node

#now add in edges behind people
for i in range(len(writerList)):
    source = writerList[i]
    for j in range(i + 1, len(writerList)):
        target = writerList[j]
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

print("Num of nodes: ",len(g.nodes())) #diagnostic, should be equal to len(writerList)
print("Num of edges: ",len(g.edges()))

'''
#FINDS CENTRALITY SCORES
#taken from centralityScores.py


#use dictionaries for degree, closeness, and betweenness centrality
#find top n people in each category
#BEWARE: DICTIONARIES TAKE A LOOOOOOONG TIME TO CREATE/RUN

topCentralityPeeps = set() #there's a lot of overlap, so this has to be a set to avoid that

n = 50 #can change at will, will take top n of each category

#this creates a dictionary, where each key is the person and their value is their centrality score
dictDegreeCentrality = nx.degree_centrality(g)

degreeKeys = []
for key in dictDegreeCentrality.keys():
    degreeKeys.append((dictDegreeCentrality[key], key))
degreeKeys = sorted(degreeKeys, key = operator.itemgetter(0)) #sorts them by centrality score
topDegree = degreeKeys[-n:] #snap up the top n people
print("Top Degree Centrality:")
for a,b in topDegree:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps
    print(b.name, b.avScore)


#this creates a dictionary, where each key is the person and their value is their centrality score
dictBetweenCentrality = nx.betweenness_centrality(g)

betweenKeys = []
for key in dictBetweenCentrality.keys():
    betweenKeys.append((dictBetweenCentrality[key], key))
betweenKeys = sorted(betweenKeys, key = operator.itemgetter(0)) #sorts them by centrality score
topBetween = betweenKeys[-n:] #grabs the top n people
print("Top Betweenness Centrality:")
for a,b in topBetween:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps
    print(b.name, b.avScore)

#this creates a dictionary, where each key is the person and their value is their centrality score
dictCloseCentrality = nx.closeness_centrality(g)

closeKeys = []
for key in dictCloseCentrality.keys():
    closeKeys.append((dictCloseCentrality[key], key))
closeKeys = sorted(closeKeys, key = operator.itemgetter(0))#sorts them by centrality score
topClose = closeKeys[-n:] #grabs the top n people
print("Top Closeness Centrality:")
for a,b in topClose:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps
    print(b.name, b.avScore)

topCentralityPeeps = list(topCentralityPeeps)

#print names of topCentralityPeeps
print("There are ", len(topCentralityPeeps), "people who have top ", n, "centrality scores.")
print("Their names are: ")
for peep in topCentralityPeeps:
    print(peep.name + " " + str(peep.avScore))


#what about the average Bechdel score for these highly connected people?
#hypothesis: as these are the peeps who will be in that aforementioned 'bump', I'm guessing these av scores will be
#in the 1.75-2.75 range
totalAvScore = sum([t.avScore for t in topCentralityPeeps]) / len(topCentralityPeeps)
degreeAvScore = sum([b.avScore for a,b in topDegree]) / n
betweenAvScore = sum([b.avScore for a,b in topBetween]) / n
closeAvScore = sum([b.avScore for a,b in topClose]) / n

print("totalAvScore is: ", totalAvScore)
print("degreeAvScore is: ", degreeAvScore)
print("betweenAvScore is: ", betweenAvScore)
print("closeAvScore is: ", closeAvScore)

#Note: The average average Bechdel score for all people is roughly 2.23.

#Note: This program takes roughly half an hour to run.

#Look at gender distribution of topCentralityPeeps:
f = []
m = []
for peep in topCentralityPeeps:
    if peep.gender == "m":
        m.append(peep)
    elif peep.gender == "f":
        f.append(peep)
print("Out of the ", len(topCentralityPeeps), " top centrality people (top 50 of each category), ", len(f), " of them are female and ", len(m), " are male.")
print("Female av score: ", sum([t.avScore for t in f]) / len(f))
print("Male av score: ", sum([t.avScore for t in m]) / len(m))
'''
'''
#taken from baseToCSV.py
#writes a file 'writerConnections.csv' that has all connections between all people
with open('writerStrongConnections.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 av","person2", "person2 av", "sharedTitles", "numSharedTitles"]
    peopleWriter.writerow(newRow)

    #goes through writerList and picks up each person's connections to everyone else

    #all connections counted
    numShared = []
    for i in range(len(writerList)):
        source = writerList[i]
        for j in range(i + 1, len(writerList)):
            target = writerList[j]
            if hasSharedMovie(source, target) == True: #only writes row if there exists a connection
                sharedList = sharedMovies(source, target)
                sharedListTitles = [t.title for t in sharedList]
                totalBechdelScore = sum([movie.score for movie in sharedList])
                avBechdelScore = totalBechdelScore / len(sharedList)
                numShared.append(len(sharedList))
                peopleWriter.writerow([source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList),avBechdelScore])
    '''
'''
    #only strong connections counted
    numShared = []
    for i in range(len(writerList)):
        source = writerList[i]
        for j in range(i + 1, len(writerList)):
            target = writerList[j]
            if hasSharedMovie(source, target) == True:  # only writes row if there exists a connection
                sharedList = sharedMovies(source, target)
                if len(sharedList) > 2:
                    sharedListTitles = [t.title for t in sharedList]
                    totalBechdelScore = sum([movie.score for movie in sharedList])
                    avBechdelScore = totalBechdelScore / len(sharedList)
                    numShared.append(len(sharedList))
                    peopleWriter.writerow(
                        [source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList), avBechdelScore])

csvfileW.close()
'''

#and now we get to cliques
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
a = 5 #minimum number of people in the clique
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

for clique in strongCliques:
    print([a.name for a in clique])

with open('seriesCliques.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 av","person2", "person2 av", "sharedTitles", "numSharedTitles"]
    peopleWriter.writerow(newRow)

    #goes through peopleList and picks up each person's connections to everyone else
    numShared = []
    for clique in topCliques:
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
#most of these seemed to be animated films, plus a few Marvel films sprinkled in
