import csv
from baseObjectOriented2 import peopleList
import operator

#reads in oscarTitles file in peopleReader list
with open('oscarTitles', 'rt') as csvfileR:
    oscarList = []
    pReader = csv.reader(csvfileR, delimiter='\t', quotechar='|')
    for row in pReader:
        oscarList.append(row[0])

'''
from baseGraph:
'''
import networkx as nx
from baseToCSV import hasSharedMovie, sharedMovies

oscarPeople = []
oscarMovies = []
for person in peopleList:
    movies = [a[0] for a in person.movie]
    for movie in movies:
        if movie.title in oscarList:
            oscarPeople.append(person)
            oscarMovies.append(movie)
            break

print(oscarPeople)


g = nx.Graph() #instantiate graph object

g.add_nodes_from(oscarPeople) #adds each person as a node

#now add in edges behind people
for i in range(len(oscarPeople)):
    source = oscarPeople[i]
    for j in range(i + 1, len(oscarPeople)):
        target = oscarPeople[j]
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


'''
from baseToCSV:
'''
'''
from baseToCSV import hasSharedMovie, sharedMovies

#writes a file 'oscarConnections.csv' that has all connections between all people
with open('oscarConnections.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 av","person2", "person2 av", "sharedTitles", "numSharedTitles"]
    peopleWriter.writerow(newRow)

    #goes through peopleList and picks up each person's connections to everyone else
    numShared = []
    for i in range(len(oscarPeople)):
        source = oscarPeople[i]
        for j in range(i + 1, len(oscarPeople)):
            target = oscarPeople[j]
            if hasSharedMovie(source, target) == True: #only writes row if there exists a connection
                sharedList = sharedMovies(source, target)
                sharedListTitles = [t.title for t in sharedList]
                totalBechdelScore = sum([movie.score for movie in sharedList])
                avBechdelScore = totalBechdelScore / len(sharedList)
                numShared.append(len(sharedList))
                if avBechdelScore == 3:
                    peopleWriter.writerow([source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList),avBechdelScore])

csvfileW.close()

zero = set()
one = set()
two = set()
three = set()
for movie in oscarMovies:
    if movie.score == 3:
        three.add(movie.title)
    elif movie.score == 2:
        two.add(movie.title)
    elif movie.score == 1:
        one.add(movie.title)
    else:
        zero.add(movie.title)

print("Threes: ", len(three))
for movie in sorted(list(three)):
    print(movie)
print()
print("Twos: ", len(two))
for movie in sorted(list(two)):
    print(movie)
print()
print("Ones: ", len(one))
for movie in sorted(list(one)):
    print(movie)
print()
print("Zeroes: ", len(zero))
for movie in sorted(list(zero)):
    print(movie)
'''
topCentralityPeeps = set()
n = 10

dictBetweenCentrality = nx.betweenness_centrality(g)

betweenKeys = []
for key in dictBetweenCentrality.keys():
    betweenKeys.append((dictBetweenCentrality[key], key))
betweenKeys = sorted(betweenKeys, key = operator.itemgetter(0)) #sorts them by centrality score
topBetween = betweenKeys[-n:] #grabs the top n people
for a,b in topBetween:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps


#this creates a dictionary, where each key is the person and their value is their centrality score
dictCloseCentrality = nx.closeness_centrality(g)

closeKeys = []
for key in dictCloseCentrality.keys():
    closeKeys.append((dictCloseCentrality[key], key))
closeKeys = sorted(closeKeys, key = operator.itemgetter(0))#sorts them by centrality score
topClose = closeKeys[-n:] #grabs the top n people
for a,b in topClose:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps


topCentralityPeeps = list(topCentralityPeeps)
score = []
for person in topCentralityPeeps:
    print(person, person.avScore, len(person.movie))
    score.append(person.avScore)
print("Average score: ", sum(score) / len(score))
