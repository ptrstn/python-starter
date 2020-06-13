import argparse

from packagename import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Replace this text with your description"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    return parser.parse_args()


def main():
    print("Hello there.")


if __name__ == "__main__":
    main()
