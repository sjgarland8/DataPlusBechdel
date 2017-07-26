from baseGraph import peopleList, g, nx
import operator

#use dictionaries for degree, closeness, and betweenness centrality
#find top 10 people in each category
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
for a,b in topDegree:
    topCentralityPeeps.add(b) #add each person with a top n centrality score to topCentralityPeeps


#this creates a dictionary, where each key is the person and their value is their centrality score
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


'''
Write a file 'topCentralityAllConnections.csv' which includes all topCentralityPeeps
and their connections to everyone else.
Writing file code similar to that in baseToCSV.py.
'''
'''
with open('topCentralityAllConnections.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 average", "person2", "person 2 average", "shared movies", "number of shared movies", "collaboration average"]
    peopleWriter.writerow(newRow)

    numShared = []
    for i in range(len(peopleList)):
        source = peopleList[i]
        if source in topCentralityPeeps:
            for j in range(i + 1, len(peopleList)):
                target = peopleList[j]
                if hasSharedMovie(source,target) == True:
                    sharedList = sharedMovies(source, target)
                    sharedListTitles = [t.title for t in sharedList]
                    totalBechdelScore = sum([movie.score for movie in sharedList])
                    avBechdelScore = totalBechdelScore / len(sharedList)
                    numShared.append(len(sharedList))
                    peopleWriter.writerow([source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList),avBechdelScore])

csvfileW.close()
'''
'''
#print names of topCentralityPeeps
print("There are ", len(topCentralityPeeps), "people who have top ", n, "centrality scores.")
print("Their names are: ")
for peep in topCentralityPeeps:
    print(peep.name, peep.avScore, peep.numMovies() )

'''
#what about the average Bechdel score for these highly connected people?
#hypothesis: as these are the peeps who will be in that aforementioned 'bump', I'm guessing these av scores will be
#in the 1.75-2.75 range
totalAvScore = sum([t.avScore for t in topCentralityPeeps]) / len(topCentralityPeeps)
#degreeAvScore = sum([b.avScore for a,b in topDegree]) / n
betweenAvScore = sum([b.avScore for a,b in topBetween]) / n
closeAvScore = sum([b.avScore for a,b in topClose]) / n

print("totalAvScore is: ", totalAvScore)
#print("degreeAvScore is: ", degreeAvScore)
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
print("Out of the ", len(topCentralityPeeps), " top centrality people (top 10 of each category), ", len(f), " of them are female and ", len(m), " are male.")
if len(f) == 0:
    print("There are no females.")
else:
    print("Female av score: ", sum([t.avScore for t in f]) / len(f))
print("Male av score: ", sum([t.avScore for t in m]) / len(m))

'''
Results for top 50 of each category:
totalAvScore is:  2.08
degreeAvScore is:  2.05
betweenAvScore is:  2.14
closeAvScore is:  2.01
Out of the  76  top centrality people (top 50 of each category),  6  of them are female and  70  are male.
Female av score:  2.30
Male av score:  2.06
'''

'''
To answer Paul's question of how far down the list do you have to go to find women in the top centrality scores?
'''
topFems = []
print("Degree Centrality:")
for i in range(50):
    a,b = topDegree[49-i]
    if b.gender == "f":
        topFems.append(b)
    print(i, b.gender, b.name, a)

print()

print("Betweenness Centrality:")
for i in range(50):
    a,b = topBetween[49 - i]
    if b.gender == "f":
        topFems.append(b)
    print(i, b.gender, b.name, a)

print()

print("Closeness Centrality:")
for i in range(50):
    a,b = topClose[49-i]
    if b.gender == "f":
        topFems.append(b)
    print(i, b.gender, b.name, a)

for fem in topFems:
    print(fem.name, fem.avScore, len(fem.movie))