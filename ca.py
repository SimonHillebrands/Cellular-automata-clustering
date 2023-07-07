import numpy as np

class Rule:
  def __init__(self,states,death_rule,survival_rule,birth_rule):
    self.states = states
    self.death_rule = death_rule
    self.survival_rule = survival_rule
    self.birth_rule =birth_rule

class Grid:
    grid = np.zeros((300,300))
    def __init__(self,rule):
        self.rule = rule
    def update(self):
        new_grid = np.zeros(self.grid.shape)
        for i in range(1,self.grid.shape[0]-1):
            for j in range(1,self.grid.shape[1]-1):
                neighborhood = self.grid[i-1:i+2,j-1:j+2]
                new_grid[i,j] = self.generate(neighborhood,self.rule.states,self.rule.death_rule,self.rule.survival_rule,self.rule.birth_rule)
        self.grid = new_grid
    def get_grid(self):
        return(self.grid)
    def set_grid(self,grid):
        self.grid = grid
    def generate(self,neighborhood,states,death_rule,survival_rule, birth_rule):
        cell = neighborhood[1][1]
        live_cells = np.sum((neighborhood == len(states)) .astype(int))
        #case 1 cell is alive
        if(cell == states[-1]):
            if(live_cells in survival_rule):
                return(cell)
            elif(live_cells in death_rule):
                return(states[0])
            else:
                return(states[states.index(cell)-1])
        #case2 cell is dying
        elif(cell != states[0]):
            return(states[states.index(cell)-1])
        #case 3 cell is dead
        else:
            if(live_cells in birth_rule):
                return(states[-1])
            else:
                return(cell)

game_of_life = Rule([0,1], [1,4], [2,3],[3])

