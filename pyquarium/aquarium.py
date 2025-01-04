"""Constants for the window size and valid fish art styles, and classes
for all the possible aqarium members.
"""

import random

import bext

RIGHT_EDGE, HEIGHT = bext.size()
LEFT_EDGE = 0
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 1
# All entries in the dict for an individual fish type must have the same
# string length.
FISH_TYPE = [
    {'right': ['><>'],          'left': ['<><']},
    {'right': ['>||>'],         'left': ['<||<']},
    {'right': ['>))>'],         'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'],        'left': ['<==-<']},
    {'right': [r'>\\>'],        'left': ['<//<']},
    {'right': ['><)))*>'],      'left': ['<*(((><']},
    {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
    {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
    {'right': ['><XXX*>'],      'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>',
               '-._.-._^=>', '._.-._.^=>'],
      'left': ['<=^-._.-._', '<=^.-._.-.',
               '<=^_.-._.-', '<=^._.-._.']},
    {'right': ['}>=b>'],        'left': ['<d=<{']},
    {'right': [')+++}Xb>'],     'left': ['<dX{+++(']},
]


class Fish():
    """Fish class for all the fish in the aquarium."""

    def __init__(self, x: int, y: int):
        """Initialize a fish at cordinates x, y.

        Keyword arguments:
        x -- x coodrinate.
        y -- y coordinate
        """
        fish_colors = ('red', 'green', 'yellow', 'blue', 'purple', 'cyan')
        type = random.choice(FISH_TYPE)
        color_pattern = random.choice(('random', 'head-tail', 'single'))
        self.length = len(type['right'][0])
        if color_pattern == 'random':
            colors = []
            for i in range(self.length):
                colors.append(random.choice(fish_colors))
        if color_pattern == 'single' or color_pattern == 'head-tail':
            colors = [random.choice(fish_colors)] * self.length
        if color_pattern == 'head-tail':
            headTailColor = random.choice(fish_colors)
            colors[0] = headTailColor
            colors[-1] = headTailColor
        self.right = type['right']
        self.left = type['left']
        self.color = colors
        self.h_speed = random.randint(1, 6)
        self.v_speed = random.randint(5, 15)
        self.h_bearing_count = random.randint(10, 60)
        self.v_bearing_count = random.randint(2, 20)
        self.bearing_right = random.choice((True, False))
        self.descending = random.choice((True, False))
        self.x = x
        self.y = y
        self.counter = 1

    def swim(self):
        """Calculate the random swimming motion of the fish by adjusting
        its x and y.
        """
        if self.counter % self.h_speed == 0:
            if self.bearing_right:
                if self.x != RIGHT_EDGE - self.length:
                    self.x += 1
                else:
                    self.bearing_right = False
                    self.color.reverse()
            else:
                if self.x != LEFT_EDGE:
                    self.x -= 1
                else:
                    self.bearing_right = True
                    self.color.reverse()
        self.h_bearing_count -= 1
        if self.h_bearing_count == 0:
            self.h_bearing_count = random.randint(10, 60)
            self.bearing_right = not self.bearing_right
        if self.counter % self.v_speed == 0:
            if self.descending:
                if self.y != BOTTOM_EDGE - 1:
                    self.y += 1
                else:
                    self.descending = False
            else:
                if self.y != TOP_EDGE:
                    self.y -= 1
                else:
                    self.descending = True
        self.v_bearing_count -= 1
        if self.v_bearing_count == 0:
            self.v_bearing_count = random.randint(2, 20)
            self.descending = not self.descending
        self.counter += 1

    def draw(self):
        """Draw the fish on the terminal window."""
        bext.goto(self.x, self.y)
        if self.bearing_right:
            fishText = self.right[self.counter % len(self.right)]
        else:
            fishText = self.left[self.counter % len(self.left)]
        for i, fishPart in enumerate(fishText):
            bext.fg(self.color[i])
            print(fishPart, end='')

    def clear(self):
        """Clear the fish from the terminal window."""
        bext.goto(self.x, self.y)
        print(' ' * len(self.left[0]), end='')


class Bubbler:
    """Class for all the bubble nucleation points in the aquarium."""

    def __init__(self, x: int):
        """Initialize a bubbler at coordinate x.

        Keyword arguments:
        x -- x coodrinate.
        """
        self.x = x
        self.bubbles = []

    def burble(self):
        """Calculate the random bubbling from the bubbler."""
        if random.randint(1, 5) == 1:
            self.bubbles.append(self.Bubble(self.x))
        for i in range(len(self.bubbles) - 1, -1, -1):
            if self.bubbles[i].y == TOP_EDGE:
                del self.bubbles[i]
        for bubble in self.bubbles:
            bubble.float()

    class Bubble:
        """Class for the individual bubbles emanating from a Bubbler."""

        def __init__(self, x: int):
            """Initialize a bubble at coordinate x

            Keyword arguements:
            x -- x coordinate.
            """
            self.x = x
            self.y = BOTTOM_EDGE

        def float(self):
            """Calculate the random floating motion of the bubble."""
            diceRoll = random.randint(1, 6)
            if self.y != BOTTOM_EDGE:  # Bubble up from a fixed point.
                if (diceRoll == 1) and (self.x != LEFT_EDGE + 1):
                    self.x -= 1
                elif (diceRoll == 2) and (self.x != RIGHT_EDGE - 1):
                    self.x += 1
            self.y -= 1

        def draw(self):
            """Draw the bubble on the terminal window."""
            bext.fg('white')
            bext.goto(self.x, self.y)
            print(random.choice(('o', 'O')), end='')

        def clear(self):
            """Clear the bubble from the terminal window."""
            bext.goto(self.x, self.y)
            print(' ', end='')


class Kelp:
    """Class for all the kelp strands in the aquarium."""

    def __init__(self, x: int):
        """Initialize a kelp strand at coordinate x.

        Keyword arguments:
        x -- x coordinate.
        """
        self.segments = [random.choice(['(', ')']) for i
                         in range(random.randint(6, HEIGHT - 1))]
        self.x = x

    def sway(self):
        """Calculate the random swaying motion of the kelp strand."""
        for i, segment in enumerate(self.segments):
            if random.randint(1, 20) == 1:
                if segment == '(':
                    self.segments[i] = ')'
                elif segment == ')':
                    self.segments[i] = '('

    def draw(self):
        """Draw the kelp strand on the terminal window."""
        bext.fg('green')
        for i, segment in enumerate(self.segments):
            if segment == '(':
                bext.goto(self.x, BOTTOM_EDGE -1 - i)
            elif segment == ')':
                bext.goto(self.x + 1, BOTTOM_EDGE -1 - i)
            print(segment, end='')

    def clear(self):
        """Clear the kelp strand from the terminal window."""
        for i in range(len(self.segments)):
            bext.goto(self.x, HEIGHT - 2 - i)
            print('  ', end='')
