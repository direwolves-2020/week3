from Model import Game

class View:

    def show_home_screen():
        choice = input(
        """
        What would you like to do?
        Select from the following options 1, 2, 3, or 4:
            1 - View all games
            2 - View all teams
            3 - View specific team 
            4 - Add a game
            5 - Delete a game
        """
        )
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5. ")
            

    def get_game_data():
        print("\nHere are all the games: ")
        
    def show_game_headers():    
        print("\nGame ID, Game Round, Team 1, Team 2, Game Result")


    def get_team_data():
        team_id = input("Enter the id of the team you'd like info on: ")
        return team_id
    

    def show_team_headers():
        print("\nTeam ID, Year, Seed, Bracket")


    def get_game_round():
        game_round = input("Enter the round number: ")
        return game_round


    def get_team1():
        team1 = input("Enter Team 1 name: ")
        return team1


    def get_team2():
        team2 = input("Enter Team 2 name: ")
        return team2


    def get_result():
        result = input("Enter the result: ")
        return result


    def add_game():
        print("\nGame added. Here is the game: ")


    def delete_game():
        id_for_deletion = input("Select a game id to delete: ")
        return id_for_deletion


    def game_deleted(deleted_game_id):
        print("Game {} deleted.".format(deleted_game_id))
