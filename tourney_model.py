import sqlite3

db = 'tourney.db'
conn = sqlite3.connect(db)



class TeamEntity:
    def __init__(self):
        self.id = None
        self.year = None
        self.bracket = None
        self.seed = None

class GameEntity:
    def __init__(self):
        self.id = None
        self.team1 = None
        self.team2 = None
        self.round = None
        self.result = None


class TourneyDAO:
    def __init__(self):
        self.game_entity = GameEntity()

    def get_team_id(self, team_entity):
        c = conn.cursor()
        search = c.execute(
        f"""
        SELECT * from Team
        WHERE year = {team_entity.year} 
        AND bracket = '{team_entity.bracket}'
        AND seed = {team_entity.seed}
        ;
        """
        )

        info = c.fetchall()
        c.close()

        team_entity.id = info[0][0]

        return team_entity

    def create_game(self, game):
        c = conn.cursor()
        inserting = c.execute(
                f"""
                INSERT INTO Game (team1, team2, result)
                VALUES ("{game.team1}", "{game.team2}", "{game.result}"
                ); """)

        conn.commit()
        c.close()
    
    def delete_game(self, game):
        c = conn.cursor()
        inserting = c.execute(
                f"""
                DELETE FROM Game WHERE id = {game};
                """)

        conn.commit()
        c.close()