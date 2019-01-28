# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
import math
import random

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
    
        
        return SoccerAction(Vector2D(random.randint(-1,1),random.randint(-1,1)),Vector2D(random.randint(-1,1),random.randint(-1,1)))

class FonceurStrategy(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    

     def compute_strategy(self, state, id_team, id_player):
        if(id_team ==2):
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            
      
        return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position, goal - state.ball.position)


#class DefenseurStrategy(Strategy):
 #   def _init_(self):
  #      Strategy._init_(self, "Defenseur")
   #     
    #def compute_strategy(self, state, id_team, id_player):

# Create teams
         
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("Random", RandomStrategy()) 
team2.add("manel", FonceurStrategy()) 
team2.add("reggey", FonceurStrategy()) 
team1.add("ramesh", RandomStrategy()) # Random strategy
team1.add("zizou", RandomStrategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)