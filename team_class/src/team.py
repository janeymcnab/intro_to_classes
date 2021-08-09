class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, current_player):
        return self.players.count(current_player) > 0
    
    def play_game(self, game_win):
        if game_win:
            self.points += 3
    
    def get_points(self):
        return self.points