
import nashpy as nash

nash.__version__

import numpy as np

#chicken game- normal form representation. 2 players: A and B.
A = np.array([[6, 2], [8, 0]])
B = np.array([[6, 8], [2, 0]])
chicken_game=nash.Game(A,B)
chicken_game

#utility if both players play their first strategy (aggressive)
sigma_r = np.array([1, 0])
sigma_c = np.array([1, 0])
chicken_game[sigma_r,sigma_c]

#utility if both players randomise over both strategies uniformly (0.5A,0.5P)
sigma_r=np.array([0.5,0.5])
sigma_c=np.array([0.5,0.5])
chicken_game[sigma_r,sigma_c]

#use support enumeration algorithm in nashpy to generate equilibria of the game (2 PSNE, 1 MSNE)
equilibria=chicken_game.support_enumeration()
for eq in equilibria:
    print(eq)






