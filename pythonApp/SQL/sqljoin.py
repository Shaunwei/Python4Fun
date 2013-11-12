import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("""SELECT DISTINCT population.city, population.population,
		regions.region FROM population INNER JOIN regions
		ON population.city = regions.city ORDER by
population.city ASC""")
	rows = c.fetchall()
	for r in rows:
		print r


