import argparse
import sys

from pyquarium import render_aquarium


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='pyquarium')
    parser.add_argument('-f', '--fish', nargs='?', default=8, type=int)
    parser.add_argument('-b', '--bubblers', nargs='?', default=3, type=int)
    parser.add_argument('-k', '--kelp', nargs='?', default=4, type=int)
    parser.add_argument('fps', nargs='?', default=6, type=int)
    return parser.parse_args()


args= _get_args()
try:
    render_aquarium(args.fish, args.bubblers, args.kelp, args.fps)
except KeyboardInterrupt:
    sys.exit()
