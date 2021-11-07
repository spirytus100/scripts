import sqlite3
import datetime, os


if not os.path.exists("carfuel.db"):
	conn = sqlite3.connect("carfuel.db")
	conn.execute("CREATE TABLE IF NOT EXISTS carfuel (fuel_price REAL, fuel_amount REAL, mileage INT, fueling_date TIMESTAMP)")
	conn.commit()
else:
	conn = sqlite3.connect("carfuel.db")

fuel_price = input("Cena paliwa: ")
fuel_amount = input("Ilość paliwa: ")
mileage = input("Przebieg: ")

quest = input("Czy zapisać dane: ")
if quest == "y":
    sql_insert = "INSERT INTO carfuel (fuel_price, fuel_amount, mileage, fueling_date) VALUES (?, ?, ?, ?)"
    conn.execute(sql_insert, (float(fuel_price), float(fuel_amount), int(mileage), datetime.datetime.now()))
    conn.commit()
else:
	print("Dane nie zostały zapisane.")

prices = []
amount = []
mileage = []
dates = []

cursor = conn.execute("SELECT * FROM carfuel")
for row in cursor:
	prices.append(row[0])
	amount.append(row[1])
	mileage.append(row[2])
	dates.append(row[3])

mildif = []
if len(mileage) >= 2:
	for i in range(0, len(mileage)):
		if i == len(mileage)-1:
			break
		fuel_per_km = amount[i+1] / (mileage[i+1] - mileage[i])
		price_per_km = prices[i] * fuel_per_km
		print(dates[i], "Spalanie na 100 km:", round(fuel_per_km*100, 2), "litrów,", "Cena wyjazdu na wieś:", round(price_per_km*126, 2), "zł")
else:
	print("Zbyt mała ilość danych.")



