import os
import argparse



def start_waage(args):
    from waage.main import main
    main()

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="command")


    start_anybus_p = subparsers.add_parser("main", help="Startet das Programm")
    start_anybus_p.set_defaults(func=start_waage)

    args = parser.parse_args()
    args.func(args)
