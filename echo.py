import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    parser = create_parser()

    if not args:
        return open("./USAGE", "r").read()

    namespace = parser.parse_args(args)
    text = namespace.text

    if namespace.upper:
        text = text.upper()
    if namespace.lower:
        text = text.lower()
    if namespace.title:
        text = text.title()

    return text


if __name__ == '__main__':
    result = main(sys.argv[1:])
    print(result)
