"""CLI for running the aquarium."""

import argparse

from pyquarium import render_aquarium, __version__


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='pyquarium',
        description='ascii art aquarium for your terminal',
        epilog='<https://github.com/awinstonw/pyquarium/>'
    )
    parser.add_argument('-f', '--fish', nargs='?', default=8, type=int,
                        help='number of fish; default=8')
    parser.add_argument('-b', '--bubblers', nargs='?', default=1, type=int,
                        help='number of bubblers; default=1')
    parser.add_argument('-k', '--kelp', nargs='?', default=5, type=int,
                        help='number of kelp strands; default=5')
    parser.add_argument('-c', '--castle', action='store_true',
                        help='include the castle; default=off')
    parser.add_argument('fps', nargs='?', default=6, type=int,
                        help='refresh rate; default=6, min=1')
    parser.add_argument('-v', '--version', action='version',
                        version=f'%(prog)s version {__version__}')
    return parser.parse_args()


args = _get_args()
render_aquarium(args.fish, args.bubblers, args.kelp, args.castle, args.fps)
