import argparse
import sys

import bext

from pyquarium import render_aquarium, __version__, aquarium


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='pyquarium',
        description='ascii art aquarium for your terminal',
        epilog='<https://github.com/awinstonw/pyquarium/>'
    )
    parser.add_argument('-f', '--fish', nargs='?', default=8, type=int,
                        help='default=8, max=30, min=0')
    parser.add_argument('-b', '--bubblers', nargs='?', default=3, type=int,
                        help='default=3, max=15, min=0')
    parser.add_argument('-k', '--kelp', nargs='?', default=5, type=int,
                        help='default=5, max=15, min=0')
    parser.add_argument('fps', nargs='?', default=6, type=int,
                        help='default=6, max=45, min=1')
    parser.add_argument('-v', '--version', action='version',
                        version=f'%(prog)s version {__version__}')
    return parser.parse_args()


args= _get_args()
# Reasonable limits for most conditions.
args.fish = min(30, args.fish)
args.bubblers = min(15, args.bubblers)
args.kelp = min(15, args.kelp)
args.fps = min(45, max(1, args.fps))
try:
    print('\033[?25l', end="")
    render_aquarium(args.fish, args.bubblers, args.kelp, args.fps)
except KeyboardInterrupt:
    bext.goto(0, aquarium.BOTTOM_EDGE)
    print('\033[?25h', end="")
    sys.exit()
