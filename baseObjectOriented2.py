
import csv

#reads in masterDataset.txt file in peopleReader list
with open('masterDataset.txt', 'rt') as csvfileR:
    peopleReader = []
    pReader = csv.reader(csvfileR, delimiter='\t', quotechar='|')
    for row in pReader:
        endRow = row[6:]
        peopleReader.append(row)

movieList = [] #will create a list of all movies

#creates the class Movie and allows us to access each movie's variables
class Movie:
    def __init__(self, title, imdb, budget, domBoxOffice, intBoxOffice, score, year, writers, directors, producers, femTalkPerc, femWPerc, femDPerc, femPPerc, overallFemPerc):
        self.title = title
        self.imdb = imdb
        self.budget = budget
        self.domBoxOffice = domBoxOffice
        self.boxOffice = intBoxOffice
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
    def numMovies(self):
        count = 0
        for movie in [a for a in self.movie]:
            count+=1
        return count

def getString(string):
    a = -1
    for i in range(len(string)):
        if string[i].isalpha() == True:
            a = i
            break
    if a == -1:
        return "Null"
    for j in range(len(string) - 1, 0, -1):
        if string[j].isalpha() == True:
            b = j
            break
    return string[a:b+1]





count = 0

for row in peopleReader:
    if count > 0: #don't want the headers being stored

        #instantiates Movie object and appends it to movieList
        movieList.append(Movie(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), row[7], row[8], row[9], float(row[10]), float(row[11]), float(row[12]), float(row[13]), float(row[14])))

        #breaks apart list of writers and creates a People object for each person
        writers = movieList[count-1].writers.split(", ")
        if writers != ['']:
            #print(writers)

            for i in range(0,len(writers),2):
                name = getString(writers[i])
                if name == "Null":
                    break
                name = name.split("  ")
                name = " ".join(name)
                gender = getString(writers[i+1])
                #print(name,gender)

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

        directors = movieList[count-1].directors.split(", ")
        if directors != ['']:
            #print(directors)

            for i in range(0,len(directors),2):
                name = getString(directors[i])
                if name == "Null":
                    break
                name = name.split("  ")
                name = " ".join(name)
                gender = getString(directors[i+1])
                #print(name,gender)
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
        producers = movieList[count-1].producers.split(", ")
        if producers != ['']:
            #print(producers)

            for i in range(0,len(producers),2):
                name = getString(producers[i])
                if name == "Null":
                    break
                name = name.split("  ")
                name = " ".join(name)
                gender = getString(producers[i+1])
                #print(name,gender)
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

#average Bechdel score of all movies
avBech = sum([m.score for m in movieList]) / len(movieList)
print("The average Bechdel score of all movies is: ", avBech)

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


'''
import csv
import statistics

with open('masterDataset.txt', 'rt') as csvfileR:
    peopleReader = []
    pReader = csv.reader(csvfileR, delimiter='\t', quotechar='|')
    for row in pReader:
        peopleReader.append(row)

# with open('oscars.txt', 'rt') as csvfileR3:
#     oscarsReader = []
#     oReader = csv.reader(csvfileR3, delimiter = '\t', quotechar = '|')
#     for row in oReader:
#         oscarsReader.append(row)

topGrossThresholds = [20, 24, 20.5, 20, 21, 23, 24, 33, 28, 25, 30, 31, 24, 29, 26, 28, 30, 18, 25, 26, 17]

movieList = []


class Movie:

    def __init__(self, title, imdb, budget, domBoxOffice, intlBoxOffice, score, year, writers, directors, producers, femaleCharPerc, femaleTalkPerc, femWriterPerc, femDirecPerc, femProduPerc, femOvPerc):
        self.title = title
        self.imdb = int(imdb)
        self.budget = float(budget)
        self.domBoxOffice = float(domBoxOffice)
        self.intlBoxOffice = float(intlBoxOffice)
        self.score = int(score)
        self.year = int(year)
        self.writers = writers
        self.directors = directors
        self.producers = producers
        self.femaleTalkPercentage = float(femaleTalkPerc)
        self.femaleCharPercentage = float(femaleCharPerc)
        self.femaleWriterPercentage = float(femWriterPerc)
        self.femaleDirectorPercentage = float(femDirecPerc)
        self.femaleProducerPercentage = float(femProduPerc)
        self.overallFemalePercentage = float(femOvPerc)

    def moviePrint(self):
        print("Title: " + self.title + "\tBox Office: " + str(self.intlBoxOffice) + "\tScore: " + str(
            self.score) + "\tYear: " + str(self.year) + "\tWomen Talk Percentage: " + str(
            self.femaleTalkPercentage) + "\t ")


count = 0
for row in peopleReader:
    if count > 0:
        movieList.append(Movie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
    count += 1

csvfileR.close()
for row in movieList:
    print(row.title)



with open('MedianIntlGross.txt', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    score0 = []
    score1 = []
    score2 = []
    score3 = []
    for movie in movieList:
        if movie.score == 0: score0.append(movie.intlBoxOffice)
        else:
            if movie.score == 1: score1.append(movie.intlBoxOffice)
            else:
                if movie.score == 2: score2.append(movie.intlBoxOffice)
                else:
                    if movie.score == 3: score3.append(movie.intlBoxOffice)

    peopleWriter.writerow(["Median Intl Gross ($) for Score 0", "Median Intl Gross ($) for Score 1", "Median Intl Gross ($) for Score 2", "Median Intl Gross ($) for Score 3"])
    peopleWriter.writerow([statistics.median(score0), statistics.median(score1), statistics.median(score2), statistics.median(score3)])
    peopleWriter.writerow(
        ["Mean Intl Gross ($) for Score 0", "Mean Intl Gross ($) for Score 1", "Mean Intl Gross ($) for Score 2",
         "Mean Intl Gross ($) for Score 3"])
    peopleWriter.writerow(
        [statistics.mean(score0), statistics.mean(score1), statistics.mean(score2), statistics.mean(score3)])
csvfileW.close()
'''
'''
with open('BechdelScoreFreqsByYear.txt', 'wt') as csvfileW:
    peopleWriter = csv.writer(csvfileW, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    firstRange0 = []
    firstRange1 = []
    firstRange2 = []
    firstRange3 = []
    secondRange0 = []
    secondRange1 = []
    secondRange2 = []
    secondRange3 = []
    thirdRange0 = []
    thirdRange1 = []
    thirdRange2 = []
    thirdRange3 = []
    fourthRange0 = []
    fourthRange1 = []
    fourthRange2 = []
    fourthRange3 = []
    fifthRange0 = []
    fifthRange1 = []
    fifthRange2 = []
    fifthRange3 = []
    sixthRange0 = []
    sixthRange1 = []
    sixthRange2 = []
    sixthRange3 = []
    seventhRange0 = []
    seventhRange1 = []
    seventhRange2 = []
    seventhRange3 = []
    eighthRange0 = []
    eighthRange1 = []
    eighthRange2 = []
    eighthRange3 = []
    ninthRange0 = []
    ninthRange1 = []
    ninthRange2 = []
    ninthRange3 = []

    for movie in movieList:
        if movie.year in range(1970, 1975):
            if movie.score == 0: firstRange0.append(movie)
            if movie.score == 1: firstRange1.append(movie)
            if movie.score == 2: firstRange2.append(movie)
            if movie.score == 3: firstRange3.append(movie)
        if movie.year in range(1975, 1980):
            if movie.score == 0: secondRange0.append(movie)
            if movie.score == 1: secondRange1.append(movie)
            if movie.score == 2: secondRange2.append(movie)
            if movie.score == 3: secondRange3.append(movie)
        if movie.year in range(1980, 1985):
            if movie.score == 0: thirdRange0.append(movie)
            if movie.score == 1: thirdRange1.append(movie)
            if movie.score == 2: thirdRange2.append(movie)
            if movie.score == 3: thirdRange3.append(movie)
        if movie.year in range(1985, 1990):
            if movie.score == 0: fourthRange0.append(movie)
            if movie.score == 1: fourthRange1.append(movie)
            if movie.score == 2: fourthRange2.append(movie)
            if movie.score == 3: fourthRange3.append(movie)
        if movie.year in range(1990, 1995):
            if movie.score == 0: fifthRange0.append(movie)
            if movie.score == 1: fifthRange1.append(movie)
            if movie.score == 2: fifthRange2.append(movie)
            if movie.score == 3: fifthRange3.append(movie)
        if movie.year in range(1995, 2000):
            if movie.score == 0: sixthRange0.append(movie)
            if movie.score == 1: sixthRange1.append(movie)
            if movie.score == 2: sixthRange2.append(movie)
            if movie.score == 3: sixthRange3.append(movie)
        if movie.year in range(2000, 2005):
            if movie.score == 0: seventhRange0.append(movie)
            if movie.score == 1: seventhRange1.append(movie)
            if movie.score == 2: seventhRange2.append(movie)
            if movie.score == 3: seventhRange3.append(movie)
        if movie.year in range(2005, 2010):
            if movie.score == 0: eighthRange0.append(movie)
            if movie.score == 1: eighthRange1.append(movie)
            if movie.score == 2: eighthRange2.append(movie)
            if movie.score == 3: eighthRange3.append(movie)
        if movie.year in range(2010, 2016):
            if movie.score == 0: ninthRange0.append(movie)
            if movie.score == 1: ninthRange1.append(movie)
            if movie.score == 2: ninthRange2.append(movie)
            if movie.score == 3: ninthRange3.append(movie)

    peopleWriter.writerow(["Year Range", "Number with Score 0", "Number with Score 1", "Number with Score 2", "Number with Score 3"])
    peopleWriter.writerow(["1970-1974", len(firstRange0), len(firstRange1), len(firstRange2), len(firstRange3)])
    peopleWriter.writerow(["1975-1979", len(secondRange0), len(secondRange1), len(secondRange2), len(secondRange3)])
    peopleWriter.writerow(["1980-1984", len(thirdRange0), len(thirdRange1), len(thirdRange2), len(thirdRange3)])
    peopleWriter.writerow(["1985-1989", len(fourthRange0), len(fourthRange1), len(fourthRange2), len(fourthRange3)])
    peopleWriter.writerow(["1990-1994", len(fifthRange0), len(fifthRange1), len(fifthRange2), len(fifthRange3)])
    peopleWriter.writerow(["1995-1999", len(sixthRange0), len(sixthRange1), len(sixthRange2), len(sixthRange3)])
    peopleWriter.writerow(["2000-2004", len(seventhRange0), len(seventhRange1), len(seventhRange2), len(seventhRange3)])
    peopleWriter.writerow(["2005-2009", len(eighthRange0), len(eighthRange1), len(eighthRange2), len(eighthRange3)])
    peopleWriter.writerow(["2010-2015", len(ninthRange0), len(ninthRange1), len(ninthRange2), len(ninthRange3)])

csvfileW.close()
'''
'''
    def calculateAvgScores(type):
        for p in range(0, 11):
            i = p / 10
            sumScores = 0
            moviesWithTargetMetric = []
            for movie in movieList:
                metric = 0
                if True:
                    if type == 'w':
                        metric = movie.femaleWriterPercentage
                    else:
                        if type == 'd':
                            metric = movie.femaleDirectorPercentage
                        else:
                            if type == 'p':
                                metric = movie.femaleProducerPercentage
                            else:
                                if type == 'c':
                                    metric == movie.femaleCharPercentage
                                else:
                                    if type == 't':
                                        metric = movie.femaleTalkPercentage
                                    else:
                                        metric = movie.overallFemalePercentage
                if round(metric, 1) == i:
                    moviesWithTargetMetric.append(movie)
            num = len(moviesWithTargetMetric)
            for x in moviesWithTargetMetric:
                if x.score >= 0:
                    sumScores += x.score
            if num != 0:
                score = sumScores / num
            else:
                score = -5
            peopleWriter.writerow([i, score])


    def scoresWithTalkTime():
        for p in range(0, 11):
            i = p / 10
            sumScores = 0
            moviesWithTargetMetric = []
            for movie in movieList:
                # print(type(movie.femaleTalkPercentage))
                if round(movie.femaleCharPercentage, 1) == i:
                    moviesWithTargetMetric.append(movie)
            num = len(moviesWithTargetMetric)
            for x in moviesWithTargetMetric:
                sumScores += x.score
            if num != 0:
                score = sumScores / num
            else:
                score = -5
            peopleWriter.writerow([i, score])


    def calculateAvgTalkTime(type, year, top):
        for p in range(0, 11):
            i = p / 10
            sumTalkTimes = 0
            moviesWithTargetMetric = []
            for movie in movieList:
                metric = 0
                if True:
                    if type == 'w':
                        metric = movie.femaleWriterPercentage
                    else:
                        if type == 'd':
                            metric = movie.femaleDirectorPercentage
                        else:
                            if type == 'p':
                                metric = movie.femaleProducerPercentage
                            else:
                                if type == 'c':
                                    metric = movie.femaleCharPercentage
                                else:
                                    metric = movie.overallFemalePercentage

                if round(metric, 1) == i:
                    if movie.femaleTalkPercentage != -1.5:
                        if movie.year == year:
                            if top == True:
                                if movie.boxOffice >= topGrossThresholds[1995 - year] * 1000000:
                                    moviesWithTargetMetric.append(movie)
                                    print("* " + movie.title + " " + str(movie.boxOffice))
                            if top == False:
                                moviesWithTargetMetric.append(movie)
                                print(movie.title + " " + str(movie.boxOffice))
            num = len(moviesWithTargetMetric)
            for x in moviesWithTargetMetric:
                sumTalkTimes += x.femaleTalkPercentage
            if num != 0:
                score = sumTalkTimes / num
            else:
                score = -5
            peopleWriter.writerow([i, score])


    def calculateAvgCharPercent(type, year, top):
        for p in range(0, 11):
            i = p / 10
            sumNumChars = 0
            moviesWithTargetMetric = []
            for movie in movieList:
                metric = 0
                if True:
                    if type == 'w':
                        metric = movie.femaleWriterPercentage
                    else:
                        if type == 'd':
                            metric = movie.femaleDirectorPercentage
                        else:
                            if type == 'p':
                                metric = movie.femaleProducerPercentage
                            else:
                                metric = movie.overallFemalePercentage
                if round(metric, 1) == i:
                    if movie.femaleCharPercentage != -1.5:
                        moviesWithTargetMetric.append(movie)
            num = len(moviesWithTargetMetric)
            for x in moviesWithTargetMetric:
                sumNumChars += x.femaleCharPercentage
            if num != 0:
                score = sumNumChars / num
            else:
                score = -5
            peopleWriter.writerow([i, score])


    peopleWriter.writerow(["Percent Female Talk Time", "Score"])
    calculateAvgScores('t')
    peopleWriter.writerow(["\n", '\n'])
    peopleWriter.writerow(['Percent Female Characters', 'Score'])
    calculateAvgScores('c')
'''