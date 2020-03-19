

class TourneyView:
    # def __init__(self):
    #     self.team_entity = TeamEntity()
    #     self.game_entity = GameEntity()

    def home_screen(self):
        print('Welcome to Tourney Seeds. What do you want to do?\n\n1. Add a game\n2. Delete a game')
        user_input = input('>')
        if user_input == '1' or '2':
            return user_input
        else:
            print('Please try again.')
            self.home_screen()

    def notifying_which_team(self,num):
        if num == 1:
            print("Let's start with the first team.\n")
        elif num == 2:
            print("Now, for the second team.\n")

    def add_game_team_year(self):
        print('Which season is the team from(1985-1989)?')
        year = int(input('>'))
        if year >= 1985 and year <= 1989:
            return year
        else:
            print('Please try again.')
            self.add_game_team1_year()

    def add_game_team_bracket(self):
        print('Which bracket is the team from(W,X,Y,Z)?')
        bracket = str.upper(input('>'))
        if bracket in ('W', 'X', 'Y', 'Z'):
            return bracket
        else:
            print('Please try again.')
            self.add_game_team1_bracket()

    def add_game_team_seed(self):
        print('What seed is the team (1-16)?')
        seed = int(input('>'))
        if seed >= 0 and seed <= 16:
            return seed
        else:
            print('Please try again.')
            self.add_game_team1_seed()

    def get_winner(self, team1, team2, game):
        print(f"The {team1.year} {team1.bracket}{team1.seed} seed versus the {team2.year} {team2.bracket}{team2.seed} seed. Riveting!\n Who wins this game? (team1, team2)")
        winner = input('>')
        if winner == 'team1' or winner == 'team2':
            return winner
        else:
            print('Please try again.')
            self.get_winner(team1, team2, game)

    def delete_game_screen(self):
        print('What is the id of the game you would like to delete?')
        game_id = input('>')
        return game_id


