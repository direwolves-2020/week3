# MVC Sqlite

You will be asked to implement the following MVC application.
You are provided with a csv file ‘TourneySeeds.csv’ - (taken from kaggle.com data itself is not accessible without an account). This file has all the NCAA men’s basketball tournament participating teams from 1985-1989. Three columns are given: Year, seed information, team id. We will not be needing the last piece of data. Generally the yearly tournament has 64 teams divided into 4 brackets. Each bracket has 16 teams ranked from 1 to 16. The brackets are also ranked, so the 16th seed in the lowest bracket is considered the 64th seed. The tournament format consists of 4 rounds to decide the winner of each bracket, and then 2 more rounds to decide the champion. 

In your models, create two tables, one called `Team`, the other called `Game`. The `Team` table should have 4 columns: id, year, bracket, seed. The latter 2 corresponding to the data in the second column of the file. The `Game` table will have at least 5 columns: id, team1, team2, round, result. Team1 and team2 columns should be foreign keys referencing `Team` table. 
Create a seed file that seeds the `Team` table with the csv file. 

The app should have the following functionality:
 * models.py that connects to the db and has entity classes for Team and Game
 * seed file with seed data from csv
 * views.py and controller.py that allow the adding and deleting of Games and their results.  

Thus, the `Teams` table should be loaded from the data in the csv file and the `Games` table should be filled by using your application

Added bonus – Add the ability to update Teams: Their seed, their bracket etc. 

