from baseObjectOriented import peopleList
import csv
people = ["Arnon Milchan","Michael De Luca","Gary Barber","Michael Paseornek","Steven Soderbergh","Ryan Kavanaugh","Toby Emmerich","Roger Birnbaum","Bob Weinstein","Harvey Weinstein","Bruce Berman", "David M. Thompson","Scott Rudin","Steven Spielberg"]
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
