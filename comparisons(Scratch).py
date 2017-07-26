import csv
from baseObjectOriented import peopleList, f, m
from baseGraph import nx, g
'''
with open('numMoviesVsAvBech14.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person", "numMovies", "avBechdelScore"]
    peopleWriter.writerow(newRow)

    people = ["Arnon Milchan", "Michael De Luca", "Gary Barber", "Michael Paseornek", "Steven Soderbergh","Ryan Kavanaugh", "Toby Emmerich", "Roger Birnbaum", "Bob Weinstein", "Harvey Weinstein", "Bruce Berman","David M. Thompson", "Scott Rudin", "Steven Spielberg"]

    for person in peopleList:
        if person.name in people:
            peopleWriter.writerow([person.name, person.numMovies(), person.avScore])
'''
'''
#create a csv file of all females
with open('femaleList.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person", "numMovies", "avBechdelScore"]
    peopleWriter.writerow(newRow)

    for person in f:
        peopleWriter.writerow([person.name, person.numMovies(), person.avScore])
csvfileW.close()

#create a csv file of all males
with open('maleList.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person", "numMovies", "avBechdelScore"]
    peopleWriter.writerow(newRow)

    for person in m:
        peopleWriter.writerow([person.name, person.numMovies(), person.avScore])
csvfileW.close()
'''
nullList = []
for person in peopleList:
    if person not in m and person not in f:
        nullList.append(person)
print("There are ", len(nullList), " people in peopleList with no gender information.")
print("This is ", len(nullList) / len(peopleList) * 100, " percent of peopleList.")

'''
#create a csv file of all people with NULL as their gender
with open('nullList.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person", "numMovies", "avBechdelScore"]
    peopleWriter.writerow(newRow)

    for person in nullList:
        peopleWriter.writerow([person.name, person.numMovies(), person.avScore])
csvfileW.close()
'''

'''
dictDegreeCentrality = nx.degree_centrality(g)
with open('centralityVsAvBech.csv', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    newRow = ["person", "gender","numMovies", "avBechdelScore", "degreeCentralityScore"]
    peopleWriter.writerow(newRow)

    for person in peopleList:
        peopleWriter.writerow([person.name, person.gender, person.numMovies(), person.avScore, dictDegreeCentrality[person]])
csvfileW.close()

'''

fNumMovies = sorted([num for num in [len(a.movie) for a in f] if num != 1])
mNumMovies = sorted([num for num in [len(a.movie) for a in m] if num != 1])
sumF = sum([len(a.movie) for a in f]) / len(f)
sumM = sum([len(a.movie) for a in m]) / len(m)

print("females: ", sumF, fNumMovies)
print("males: ", sumM, mNumMovies)