# src/main.py
from src.core.gm import GM
from src.core.cli import cli
from src.gui.app_window import app_handle

def main():
    gm = GM()
    cli.run()
    #initialize Dearpygui
    app_handle.init_ui()
    app_handle.close()



if __name__ == "__main__":
    main()