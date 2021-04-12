class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.placing = placing = 0
        self.kills = kills = 0
        
    def new_training(self, placing, kills):
        self.placing += placing
        self.kills += kills
    
    def Points_for_placing(self, placing):
        list_points = [12, 9, 8, 7, 6, 5 , 4 , 3, 2, 1, 0 , 0]
        return list_points[placing -1]

    #area of show properties
    def show_members(self):
        for c in self.members:
            if self.members.index(c) == len(self.members) - 1:
                print(c)
            else:
                print(c, end=', ')

    def show_training(self):
        points = self.Points_for_placing(self.placing)
        points += self.kills
        print(f'Points: {points}\nKills: {self.kills}.')
            

