import csv, sqlite3, re

conn = sqlite3.connect('team_database.db')
c = conn.cursor()

with open('/Users/Hudi/Documents/Byte Academy Python/week3/quiz3/TourneySeeds.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for col in csv_reader:
        #split the seed column into seed (letters) and bracket (numbers)
        c.execute(
            """ INSERT INTO team (year, bracket, seed) 
            VALUES (?, ?, ?) """,
            (col[0], col[1][0], col[1][1:3])
        )

        #delete the first row which has the CSV column header
        c.execute(
            """DELETE FROM team
               WHERE id = 1; """
        )


conn.commit()
c.close()

print("Database created")
