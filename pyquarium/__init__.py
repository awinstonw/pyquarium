"""pyquarium, by Alexander Walters <https://github.com/awinstonw>,
adapted from Al Sweigart's, <https://alsweigart.com>, fishtank.py script
in *The Big Book of Small Python Projects*. The code has been refactored
to be more object oriented and I made some minor edits to the visual
presentation of the sandy bottom and the logic for determining where the
individual aquarium member objects spawn and in what z-order, and how
the screen is refreshed.
Additionally, I added a CLI.
Book available: <https://nostarch.com/big-book-small-python-programming>
"""

import random
import sys
import time

import bext

import pyquarium.aquarium as aq

__version__ = 'v1.1.0'

def render_aquarium(fish: int, bubblers: int, kelp: int, fps: int):
    """Print a moving aquarium to the terminal.

    Keyword arguments:
    fish -- the number of fish to show.
    bubblers -- the number of bubble generators to show.
    kelp -- the number of kelp strands.
    fps -- the speed of the simulation.
    """
    # Longest fish in the type dictionary to avoid spawning a fish
    # ouside the terminal boundary.
    max_length = 0
    for type in aq.FISH_TYPE:
        if len(type['right'][0]) > max_length:
            max_length = len(type['right'][0])

    fish_list = [aq.Fish(random.randint(0, aq.RIGHT_EDGE - max_length),
                         random.randint(0, aq.BOTTOM_EDGE - 1))
                 for i in range(fish)]
    # Avoid putting the kelp and bubblers at the same column.
    randoms = [*range(aq.LEFT_EDGE + 1, aq.RIGHT_EDGE - 1)]
    random.shuffle(randoms)
    bubblers_list = [aq.Bubbler(i) for i in randoms[:bubblers]]
    kelp_list = [aq.Kelp(i) for i in randoms[bubblers:bubblers + kelp]]

    bext.bg('black')
    bext.clear()
    while True:
        # Draw the aquarium members with the kelp at the back, the fish
        # in the middle, and the bubbles up front.
        for kelp in kelp_list:
            kelp.sway()
            kelp.draw()
        for fish in fish_list:
            fish.swim()
            fish.draw()
        for bubbler in bubblers_list:
            bubbler.burble()
            for bubble in bubbler.bubbles:
                bubble.draw()
        # Draw '░' but give a margin for printed control characters.
        bext.fg('yellow')
        bext.goto(0, aq.BOTTOM_EDGE)
        print(chr(9617) * (aq.RIGHT_EDGE - 2), end='')

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(1 / fps)
        bext.clear()
        sys.stdout.flush()
