import sqlite3
import datetime
from sys import argv

connection = sqlite3.connect("trening.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

def create_table(connection):
	connection.execute("""CREATE TABLE IF NOT EXISTS training (
						exercise TEXT NOT NULL,
						weight REAL NOT NULL,
						series1 INTEGER NOT NULL,
						series2 INTEGER NOT NULL,
						series3 INTEGER NOT NULL,
						start_time timestamp,
						end_time timestamp);""")

all_exercises = ("Przysiady ze sztangą na barkach", "Martwy ciąg", "Wykroki", "Wznosy pięt", "Brzuszki na ławce skośnej", "Deska", "Podciąganie nachwytem", 
	"Wyciskanie sztangi w leżeniu", "Wiosłowanie", "Wyciskanie sztangi nad głowę", "Wznosy przedramion", "Wznosy tułowia w oparciu tylnym", "Ściskacz",
	"Rozpiętki", "Wyciskanie sztangi zza karku", "Wznosy przedramion z hantlami", "Pompki zwykłe")

fbw = ("Przysiady ze sztangą na barkach", "Martwy ciąg", "Podciąganie nachwytem", "Wznosy przedramion z hantlami", "Wyciskanie sztangi zza karku", "Rozpiętki", 
	"Pompki zwykłe", "Brzuszki na ławce skośnej")


def print_exercises(bodypart):
	start = datetime.datetime.now()
	for exercise in bodypart:
		error = False
		cursor = connection.execute("SELECT max(rowid), weight, series1, series2, series3 FROM training WHERE exercise = ?", (exercise,)).fetchone()
		print(exercise)
		print("\t" + "Ostatnio:", cursor[1], "kg", cursor[2], cursor[3], cursor[4])
		weight = input("\t" + "Ciężar: ")

		if weight == "q":
			continue
		else:
			try:
				weight = float(weight)
			except ValueError:
				print("Błędny format danych. Ćwiczenie nie zostało zapisane.")
				error = True

		if not error:
			starttime = datetime.datetime.now()
			series1 = input("\t" + "Seria 1: ")
			series2 = input("\t" + "Seria 2: ")
			series3 = input("\t" + "Seria 3: ")
			endtime = datetime.datetime.now()

			series = []
			for el in (series1, series2, series3):
				try:
					el = int(el)
				except ValueError:
					print("Błędny format danych. Ćwiczenie nie zostało zapisane.")
					error = True
					break
				else:
					series.append(el)

		if not error:
			values = (exercise, weight, series[0], series[1], series[2], starttime, endtime)
			connection.execute("INSERT INTO training VALUES(?, ?, ?, ?, ?, ?, ?)", values)
			connection.commit()

	quest = input("Czy chcesz zakończyć trening (y/n)? ")
	if quest == "y":
	    end = datetime.datetime.now()
	    duration = end - start
	    print("Trening trwał", duration)
	    cursor = connection.execute("SELECT end_time FROM training")
	    trainings = []
	    for row in cursor:
	    	trainings.append(datetime.date(row[0].year, row[0].month, row[0].day))

	    print("Gratulacje! Ukończyłeś właśnie ", len(set(trainings)), "trening!")



create_table(connection)


print_exercises(fbw)
