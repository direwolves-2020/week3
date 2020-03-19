from tourney_model import TeamEntity
from tourney_model import GameEntity
from tourney_view import TourneyView
from tourney_model import TourneyDAO






class Controller:
    def __init__(self, run = True):
        self.view = TourneyView()
        self.model = TourneyDAO()
        self.team1 = TeamEntity()
        self.team2 = TeamEntity()
        self.game_entity = GameEntity()
        if run:
            self.start_app()

    def start_app(self):
        self.home_screen()

    #At the home screen, you can either login or create an account
    #this function returns a tuple where the first value is 'existing' or 'new' and the user entity OBJECT
    def home_screen(self):
        home_screen_input = self.view.home_screen()
        #1 means they are logging in
        if home_screen_input == '1':
            self.get_team_info()
        elif home_screen_input == '2':
            self.delete_game()

    def get_team_info(self):
        #Getting the info for the first team
        self.view.notifying_which_team(1)
        self.team1.year = self.view.add_game_team_year()
        self.team1.bracket = self.view.add_game_team_bracket()
        self.team1.seed = self.view.add_game_team_seed()
        self.team1 = self.model.get_team_id(self.team1)

        #Getting the info for the second team
        self.view.notifying_which_team(2)
        self.team2.year = self.view.add_game_team_year()
        self.team2.bracket = self.view.add_game_team_bracket()
        self.team2.seed = self.view.add_game_team_seed()
        self.team2 = self.model.get_team_id(self.team2)

        #Send to game
        self.add_game()

    def add_game(self):
        self.game_entity.team1 = self.team1.id
        self.game_entity.team2 = self.team2.id
        winner = self.view.get_winner(self.team1, self.team2, self.game_entity)
        if winner == 'team1':
            self.game_entity.result = self.team1.id
        elif winner == 'team2':
            self.game_entity.result = self.team2.id
        
        #adding to DB
        self.model.create_game(self.game_entity)

    def delete_game(self):
        game_id = self.view.delete_game_screen()
        self.model.delete_game(game_id)
        




        















Controller()