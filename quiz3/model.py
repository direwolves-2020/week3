import sqlite3
db = 'bball'
conn = sqlite3.connect(db)

class Team: 
    def __init__(self): 
        self.id = None
        self.year = None
        self.bracket = None
        self.seed = None

class Game: 
    def __init__(self): 
        self.id = None
        self.team1 = None 
        self.team2 = None
        self.round = None
        self.result = None

class DAO: 
    def __init__(self): 
        self.game = Game()

#should I make the methods with no self static? 
    def get_team(team_id):
        c = conn.cursor()

        team_info = c.execute(
            f"""
            SELECT * FROM Teams 
            Where id = "{team_id}";
            """
        )
       
        return team_info.fetchall()
        c.close()

    def new_game(round, result, team1, team2): 
        c = conn.cursor()
        c.execute(
            f"""
            INSERT INTO Games (team1, team2, round, result)
            VALUES ("{team1}", "{team2}", "{round}", "{result}");
            """
        )
        conn.commit()
        c.close()

    def delete_game(game_id): 
        c = conn.cursor()
        c.execute(
            f"""
            DELETE FROM Games WHERE id = "{game_id}" 
            """
        )
        conn.commit()
        c.close()
