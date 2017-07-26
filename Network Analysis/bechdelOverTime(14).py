from baseObjectOriented import peopleList, movieList
import csv

#all of this works with the top 14 people
'''
people = ["Arnon Milchan","Michael De Luca","Gary Barber","Michael Paseornek","Steven Soderbergh","Ryan Kavanaugh","Toby Emmerich","Roger Birnbaum","Bob Weinstein","Harvey Weinstein","Bruce Berman", "David M. Thompson","Scott Rudin","Steven Spielberg"]
y = [(i,[]) for i in range(1995, 2016)]
for i in range(len(peopleList)):
    #only want the top 14 centrality people
    if peopleList[i].name in people:
        movies = [t[0] for t in peopleList[i].movie]
        movies = sorted([(movie.year, movie.score, movie.title) for movie in movies])
        print(peopleList[i].name)
        years = sorted(list(set([a[0] for a in movies])))
        #will give us their average score per year
 
        for a in years:
            m = [t for t in movies if t[0] == a]
            if len(m) != 0:
                yScore = sum([b[1] for b in m]) / len(m)
                titles = [b[2] for b in m]
                print(a, yScore, titles)
        print()


        #for average of all 14 per year (averaging the av scores)
        for a in years:
            m = [t for t in movies if t[0] == a]
            if len(m) != 0:
                yscore = sum([b[1] for b in m]) / len(m)
                index = [b[0] for b in y].index(a)
                y[index][1].append(yscore)
for year in y:
    av = sum([score for score in year[1]]) / len(year[1])
    print(year[0], av)

        #for average of all movies by top 14 person by year
        for a in years:
            index = [b[0] for b in y].index(a)
            for movie in movies:
                if movie[0] == a:
                    y[index][1].append(movie[1])
for year in y:
    av = sum([score for score in year[1]]) / len(year[1])
    print(year[0], av)

'''
'''
#now examine this for all movies
years = [(i,[]) for i in range(1995, 2016)]
for movie in movieList:
    index = [a[0] for a in years].index(movie.year)
    years[index][1].append(movie.score)

for year in years:
    av = sum([score for score in year[1]]) / len(year[1])
    print(year[0], av)
'''

#want to examine those two top centrality women
women = ["Tessa Ross", "Laurie MacDonald"]
y = [(i, []) for i in range(1995, 2016)]
for i in range(len(peopleList)):
    # only want the top 14 centrality people
    if peopleList[i].name in women:
        movies = [t[0] for t in peopleList[i].movie]
        movies = sorted([(movie.year, movie.score, movie.title) for movie in movies])
        print(peopleList[i].name)
        years = sorted(list(set([a[0] for a in movies])))
        # will give us their average score per year

        for a in years:
            m = [t for t in movies if t[0] == a]
            if len(m) != 0:
                yScore = sum([b[1] for b in m]) / len(m)
                titles = [b[2] for b in m]
                print(a, yScore, titles)
        print()

        # for average of all 14 per year (averaging the av scores)
        for a in years:
            m = [t for t in movies if t[0] == a]
            if len(m) != 0:
                yscore = sum([b[1] for b in m]) / len(m)
                index = [b[0] for b in y].index(a)
                y[index][1].append(yscore)
for year in y:
    av = sum([score for score in year[1]]) / len(year[1])
    print(year[0], av)

    # for average of all movies by top 14 person by year
    for a in years:
        index = [b[0] for b in y].index(a)
        for movie in movies:
            if movie[0] == a:
                y[index][1].append(movie[1])
for year in y:
    av = sum([score for score in year[1]]) / len(year[1])
    print(year[0], av)
