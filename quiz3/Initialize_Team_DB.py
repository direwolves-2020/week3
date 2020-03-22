import sqlite3

conn = sqlite3.connect('team_database.db')

conn.execute(
    """
    DROP TABLE if exists team;
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year TEXT,
        bracket TEXT,
        seed TEXT
    );
    """
)

conn.execute(
    """
    DROP TABLE if exists game;
    """
)

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS game (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_round TEXT,
        result TEXT,
        team1 TEXT,
        team2 TEXT,
        FOREIGN KEY(team1) REFERENCES team(id),
        FOREIGN KEY(team2) REFERENCES team(id)
        );
    """   
)  

conn.close()