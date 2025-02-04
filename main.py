# src/main.py
from src.core.gm import GM
from src.core.cli import cli


def main():
    gm = GM()
    cli.run()


if __name__ == "__main__":
    main()