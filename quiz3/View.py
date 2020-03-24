class View: 

    def home_screen(): 
        result = input(
        """
        Welcome to the Bracket Builder!
        Please enter the number associated with what you want to do: 
        1 - View a teams info 
        2 - Add a game 
        3 - Delete a game
        """
        )
        if result == "1" or result == "2" or result == "3":
            return result 
        else: 
            print("Invalid input, please enter a number between 1 and 3.")

    def get_team_info(): 
        team_id = input("Please enter the team id of the team you want info for: ")
        return team_id

    def get_game_round(): 
        game_round = input("Enter the round for the Game: ")
        return game_round
    
    def get_team1(): 
        team1 = input("Enter the first team's id: ")
        return team1
    
    def get_team2(): 
        team2 = input("Enter the second team's id: ")
        return team2

    def get_result(): 
        result = input("Enter the games result: ")
        return result 
    
    def game_status(): 
        print("Your action was successful")

    def delete_game(): 
        game = input("Enter the id for the game to delete: ")
        return game


