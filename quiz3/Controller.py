from View import View
from Model import GameDAO, Game, Team

class Controller:
    def __init__(self):
        self.view = View()
        self.model = GameDAO()
        self.team1 = Team()
        self.team2 = Team()
        self.game = Game()

    
    def start(self):
        #show all the app options
        choice = View.show_home_screen()
        if choice == "1":
            self.get_all_game_data()
        if choice == "2":
            self.get_all_team_data()
        if choice == "3":
            self.get_team_data()
        if choice == "4":
            self.add_new_game()
        if choice == "5":
            self.delete_game()


    def restart(self):
        #ensures that the app runs continously
        choice = input("\nPress 0 to restart app. ")
        if choice == "0":
            c.start()
        self.restart()


    def get_all_game_data(self):
        #prints all games in the game table
        View.show_game_headers()
        for row in GameDAO.get_all_game_data():
            print(row)
        

    def get_last_added_game(self):
        #adds all the games to a list and just prints the last added one  
        l = []
        for row in GameDAO.get_all_game_data():
            l.append(row)
        print(l.pop())


    def get_team_data(self):
        #gets user input for team id 
        team_id = View.get_team_data()     
        View.show_team_headers()
        print(GameDAO.get_team(team_id))


    def get_all_team_data(self):
        #prints all the teams in the team table
        View.show_team_headers()
        for row in GameDAO.get_all_team_data():
            print(row)


    def add_new_game(self):
        #gets all the data to add a new game
        game = Game()
        game.game_round = View.get_game_round()
        game.team1 = View.get_team1()
        game.team2 = View.get_team2()
        game.result = View.get_result()

        GameDAO.add_game(game.game_round, game.team1, game.team2, game.result)

        View.add_game()
        #displays the just added game
        View.show_game_headers()
        self.get_last_added_game()


    def delete_game(self):
        #gets user input for the game to delete
        id_for_deletion = View.delete_game()
        GameDAO.delete_game(id_for_deletion)
        View.game_deleted(id_for_deletion)


if __name__ == "__main__":
    c = Controller()
    c.start()
    c.restart()
    