import sqlite3, csv, re

db = 'bball'

conn = sqlite3.connect(db)
c = conn.cursor()
#dropping tables if they exist for easy wiping/reseeding
conn.execute(
    """
    DROP TABLE if exists Teams;
    """
)
conn.execute(
    """
    CREATE TABLE Teams(
        id INTEGER PRIMARY KEY,
        year INTEGER,
        bracket TEXT, 
        seed INTEGER
    );""")

conn.execute(
    """
    DROP TABLE if exists Games; 
    """
)
conn.execute(
    """
    CREATE TABLE Games (
        id INTEGER PRIMARY KEY, 
        team1 INTEGER, 
        team2 INTEGER, 
        round INTEGER, 
        result TEXT,
        CONSTRAINT fk_Teams
            FOREIGN KEY (team1)
            REFERENCES Teams (ID)
        CONSTRAINT fk_Teams
            FOREIGN KEY (team2)
            REFERENCES Teams (ID)
    );""")

conn.commit()


#Seeding 

with open("/home/scottie/Documents/week3/week3/quiz3/TourneySeeds.csv", "r") as seed_file:
    csv_seed = csv.reader(seed_file) 
    for column in csv_seed: 
        c.execute(
            """
            INSERT INTO Teams (year, bracket, seed)
            VALUES (?,?,?)
            """,
            (column[0], column[1][0], column[1][1:3])
        ) 
    
    c.execute(
        """
        DELETE FROM Teams
        Where id = 1;
        """
    )

conn.commit()
c.close()

print("Success")