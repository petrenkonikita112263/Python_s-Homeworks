from sphere import Sphere
from guessing_game import GuessingGame

s = Sphere(1)
s.surface_area()
s.volume()
print(s)

g = GuessingGame()
g.reset_random()
g.guess()
