"""
Programer: Saurav Pokharel
Date: 10/15/2024
Description: Calculate Golf Score. 
"""
class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        wins = float(self.wins)
        return wins/ (wins + float(self.losses))
    
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print(f'Win percentage: {win_percentage:.2f}')
        
        if win_percentage >= .5:
            print('Congratulations, team', self.name, 'has a winning average!')
        else:
            print('Team', self.name, 'has a losing average.')


teamWomensVolleyball = Team()

print(teamWomensVolleyball.name)

print('Welcome to the winning percentage calulator.')
team_name = "Women's Volleyball"
team_wins = int(input('How many wins does the team have?:'))
team_losses = int(input('How many losses does the team have?:'))

teamWomensVolleyball.name = team_name
teamWomensVolleyball.wins = team_wins
teamWomensVolleyball.losses = team_losses

teamWomensVolleyball.print_standing()