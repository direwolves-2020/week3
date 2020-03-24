from View import View
from model import DAO, Team, Game 

class Controller: 

    def __init__(self): 
        self.view = View()
        self.model = DAO()
        self.team1 = Team()
        self.team2 = Team()
        self.game = Game()

    def run(self): 
        result = View.home_screen()
        if result == "1": 
            self.get_team_info()
        if result == "2": 
            self.add_game()
        if result == "3": 
            self.delete_game()

    def get_team_info(self): 
        team_id = View.get_team_info()
        print(DAO.get_team(team_id))

    def add_game(self):
        game = Game()
        game.team1 = View.get_team1()
        game.team2 = View.get_team2()
        game.game_round = View.get_game_round()
        game.result = View.get_result()

        DAO.new_game(game.game_round, game.result, game.team1, game.team2)
        View.game_status()
    
    def delete_game(self): 
        game = View.delete_game()
        DAO.delete_game(game)
        View.game_status()



        

session = Controller()
session.run()