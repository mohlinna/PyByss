#!/usr/bin/env python

# A game of PyByss with AI players only.
# This is to test out the game engine before 
# the human interface is done.
from game import Game
from simple_ai_player import SimpleAiPlayer

ai_pachino = SimpleAiPlayer("AI Pacino")
ai_gore = SimpleAiPlayer("AI Gore")
ai_franken = SimpleAiPlayer("AI Franken")
ai_green = SimpleAiPlayer("AI Green")

the_players = [ai_pachino, ai_gore]
the_game = Game(the_players)