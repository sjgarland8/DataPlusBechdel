import csv
from baseObjectOriented2 import peopleList, movieList

#returns True if two people objects collaborated on a movie together
def hasSharedMovie(person1, person2):
    list1 = [t[0] for t in person1.movie]
    list2 = [t[0] for t in person2.movie]
    for element in list1:
        if element in list2:
            return True
    return False

#returns list of movie objects (that two people objects collaborated on)
def sharedMovies(person1, person2):
    set1 = set([t[0] for t in person1.movie]) #taking out .title from t[0] here, must add in later
    set2 = set([t[0] for t in person2.movie])
    shared = set1.intersection(set2)
    listShared = list(shared)
    return listShared

#writes a file 'allConnections.csv' that has all connections between all people
with open('allConnections2.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person1", "person1 av","person2", "person2 av", "sharedTitles", "numSharedTitles"]
    peopleWriter.writerow(newRow)

    #goes through peopleList and picks up each person's connections to everyone else
    numShared = []
    for i in range(len(peopleList)):
        source = peopleList[i]
        for j in range(i + 1, len(peopleList)):
            target = peopleList[j]
            if hasSharedMovie(source, target) == True: #only writes row if there exists a connection
                sharedList = sharedMovies(source, target)
                sharedListTitles = [t.title for t in sharedList]
                totalBechdelScore = sum([movie.score for movie in sharedList])
                avBechdelScore = totalBechdelScore / len(sharedList)
                numShared.append(len(sharedList))
                peopleWriter.writerow([source, source.avScore, target, target.avScore, sharedListTitles, len(sharedList),avBechdelScore])

csvfileW.close()