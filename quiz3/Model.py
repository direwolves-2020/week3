import csv, sqlite3

class Team:
    def __init__(self):
        self.team_id = None
        self.year = None
        self.bracket = None
        self.seed = None
         

class Game:
    def __init__(self):
        self.game_id = None
        self.game_round = None
        self.result = None
        self.team1 = None
        self.team2 = None
    

class GameDAO:

    def get_all_game_data():
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        c.execute(
            """ SELECT * FROM game;
            """    
        )
        result = c.fetchall()
        c.close()
        return result


    def get_game_data(game_id):
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" SELECT * FROM game
                WHERE id = "{game_id}";;
            """    
        )

        result = c.fetchall()
        c.close()
        return result


    def get_team(team_id):
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM team 
                WHERE id = "{team_id}";
            """
        )
        return result.fetchall()


    def get_all_team_data():
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        c.execute(
            """ SELECT * FROM team 
            """    
        )

        result = c.fetchall()
        c.close()
        return result


    def add_game(game_round, result, team1, team2):
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" INSERT INTO game (game_round, team1, team2, result)
            VALUES ("{game_round}", "{team1}", "{team2}" , "{result}");
            """    
        )

        conn.commit()
        c.close()


    def delete_game(game_id):
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" DELETE FROM game WHERE id = "{game_id}" """    
        )
        
        conn.commit()
        c.close()

