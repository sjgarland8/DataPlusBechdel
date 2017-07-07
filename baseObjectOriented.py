import csv

#reads in movieData file in peopleReader list
with open('movieData', 'rt') as csvfileR:
    peopleReader = []
    pReader = csv.reader(csvfileR, delimiter='\t', quotechar='|')
    for row in pReader:
        endRow = row[6:]
        peopleReader.append(row)

movieList = [] #will create a list of all movies

#creates the class Movie and allows us to access each movie's variables
class Movie:
    def __init__(self, title, imdb, boxOffice, score, year, writers, directors, producers, femTalkPerc, femWPerc, femDPerc, femPPerc, overallFemPerc):
        self.title = title
        self.imdb = imdb
        self.boxOffice = boxOffice
        self.score = int(score)
        self.year = int(year)
        self.writers = writers
        self.directors = directors
        self.producers = producers
        self.femTalkPerc = femTalkPerc
        self.femWriterPerc = femWPerc
        self.femDirectorPerc = femDPerc
        self.femProducerPerc = femPPerc
        self.overallFemProductionPerc = overallFemPerc

    def __str__(self):
        return(str(self.title))
    def moviePrint(self):
        print("Title: " + self.title + "\tBox Office: " + str(self.boxOffice) + "\tScore: " + str(self.score) + "\tYear: " + str(self.year))

peopleList = [] #will create a list of all people involved in the movies

#creates the class People and allows us to access each person's variables (name, gender, what movies they've been in, and what role they had in production)
class People:
    def __init__(self, name, gender, movie, role):
        self.name = name
        self.gender = gender
        self.movie = [(movie, role)]
        self.avScore = movie.score
    def __str__(self):
        return(str(self.name))
    def peoplePrint(self, printBool):
        stringMovie = "["
        count = 0
        for x in self.movie:
            if count != len(self.movie) - 1:
                stringMovie = stringMovie + x[0].title + ", "
            else:
                stringMovie = stringMovie + x[0].title + "]"
            count += 1
        if printBool:
            print("Name: " + self.name + "\tGender: " + self.gender + "\tMovies: " + stringMovie + "\tScore: " + str(
            self.avScore))
        else:
            return("Name: " + self.name + "\tGender: " + self.gender + "\tMovies: " + stringMovie + "\tScore: " + str(
            self.avScore))



count = 0

for row in peopleReader:
    if count > 0: #don't want the headers being stored

        #instantiates Movie object and appends it to movieList
        movieList.append(Movie(row[0], row[1], int(row[2]), float(row[3]), int(row[4]), row[5], row[6], row[7], float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12])))

        #breaks apart list of writers and creates a People object for each person
        writers = movieList[count-1].writers.split("], ")
        for w in writers:
            if w == "[]":
                break
            w = w.strip().split(", ")
            if w[0][:3] == "[[\\":
                name = w[0][4:-1]
            if w[0][:2] == "[[":
                name = w[0][3:-1]
            elif w[0][0] == "[":
                name = w[0][2:-1]
            else:
                name = w[0][1:-1]
            gender = w[1][2]
            name = name.split("  ")
            name = " ".join(name)
            #instantiates People object for new people and appends to peopleList
            if (name not in [p.name for p in peopleList]):
                person = People(name, gender, movieList[count-1], "w")
                peopleList.append(person)
            #for repeat people, finds person in peopleList, appends the movie to their list, and recalculate their average score
            else:
                index = [p.name for p in peopleList].index(name)
                person = peopleList[index]
                person.movie.append((movieList[count-1], "w"))
                if (movieList[count-1].title not in [t[0] for t in set([movie for movie in person.movie])]):
                    person.avScore = (person.avScore*(len(person.movie)-1)+person.movie[-1][0].score)/len(person.movie)

        #does the exact same thing for directors as writers
        directors = movieList[count - 1].directors.split("], ")
        for d in directors:
            if d == "[]":
                 break
            d = d.strip().split(", ")
            if d[0][:3] == "[[\\":
                 name = d[0][4:-1]
            if d[0][:2] == "[[":
                 name = d[0][3:-1]
            elif d[0][0] == "[":
                 name = d[0][2:-1]
            else:
                 name = d[0][1:-1]
            gender = d[1][2]
            name = name.split("  ")
            name = " ".join(name)
            if (name not in [d.name for d in peopleList]):
                 person = People(name, gender, movieList[count - 1], "d")
                 peopleList.append(person)
            else:
                 index = [d.name for d in peopleList].index(name)
                 person = peopleList[index]
                 person.movie.append((movieList[count - 1], "d"))
                 if (movieList[count - 1].title not in [t[0] for t in set([movie for movie in person.movie])]):
                       person.avScore = (person.avScore * (len(person.movie) - 1) + person.movie[-1][0].score) / len(person.movie)

        #does the exact same thing for producers as writers
        producers = movieList[count - 1].producers.split("], ")
        for p in producers:
            if p == "[]":
                 break
            p = p.strip().split(", ")
            if p[0][:3] == "[[\\":
                 name = p[0][4:-1]
            if p[0][:2] == "[[":
                 name = p[0][3:-1]
            elif p[0][0] == "[":
                 name = p[0][2:-1]
            else:
                 name = p[0][1:-1]
            gender = p[1][2]
            name = name.split("  ")
            name = " ".join(name)
            if (name not in [p.name for p in peopleList]):
                person = People(name, gender, movieList[count - 1], "p")
                peopleList.append(person)
            else:
                index = [p.name for p in peopleList].index(name)
                person = peopleList[index]
                person.movie.append((movieList[count - 1], "p"))
                if (movieList[count - 1].title not in [t[0] for t in set([movie for movie in person.movie])]):
                      person.avScore = (person.avScore * (len(person.movie) - 1) + person.movie[-1][0].score) / len(person.movie)
    count+=1


csvfileR.close()

print("peopleList length: ", len(peopleList)) #diagnostic, should get 10493

print("movieList length: ", len(movieList)) #diagnostic, should get 2467

#average Bechdel score of everybody
avBechAll = sum([p.avScore for p in peopleList]) / len(peopleList)
print("The average average Bechdel score is: ", avBechAll)

f =[]
m = []
for person in peopleList:
    if person.gender == "f":
        f.append(person)
    elif person.gender == "m":
        m.append(person)


avF = sum([p.avScore for p in f]) / len(f)
avM = sum([p.avScore for p in m]) / len(m)
print("The average average Bechdel score for females is: ", avF)
print("There are ", len(f), " females out of ", len(peopleList), " people.")
print("The average average Bechdel score for males is: ", avM)
print("There are ", len(m), " males out of ", len(peopleList), " people.")
