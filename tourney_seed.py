import sqlite3
import pandas as pd

db = 'tourney.db'

conn = sqlite3.connect(db)
c = conn.cursor()
conn.execute(
	"""
	CREATE TABLE Team (
		id INTEGER PRIMARY KEY,
		year INTEGER, 
		bracket TEXT,
		seed INTEGER
	);""")

conn.execute(
    """
	CREATE TABLE Game (
		id INTEGER PRIMARY KEY,
		team1 INTEGER,
		team2 INTEGER,
		round INTEGER,
		result TEXT
	); """)

conn.commit()


#############################################################################
#Seeding

df = pd.read_csv('TourneySeeds.csv')

#I first need to split this seed column to the different brackets -- ('[0-9]') regex also works
new = df['Seed'].str.split(pat = '(\d+)',n = 1, expand = True)
#Needed to include these two steps because 'new' was making 3 columns. the third column was empty whitespace and I couldn't figure out why it was happening or how to avoid it
df['bracket'] = new[0]
df['seed'] = new[1]
#deleting unused & old columns
df.drop(columns = ['Seed', 'Team'], inplace = True)

#reading dataframe into database
for index, row in df.iterrows():
	c.execute(
		"""
		INSERT INTO Team ("year", "bracket", "seed")
		VALUES (?, ?, ?)
		""",(row['Season'], row['bracket'], row['seed'])
	)
conn.commit()
conn.close()

print("Your database named", db, "was succesfully created")