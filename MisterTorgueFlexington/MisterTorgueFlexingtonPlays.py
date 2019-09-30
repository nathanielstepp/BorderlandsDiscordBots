#Torgue discord.Game options

# Might need to edit this with a timer,
# so that it changes every few hours/days,
# instead of just on initialization.


import random

def torguePlaying():
    game_options = ['Air Guitar',
                    '1812 Overture with REAL CANNONS',
                    'Splosion Man',
                    'Stardew Valley with C4 Mods',
                    'Fantasy Unicorn Simulator',
                    'P90X'
                    ]
    return random.choice(game_options)

