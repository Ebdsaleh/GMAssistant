# src/gui/theme_manager.py

"""
This class is responsible for storing and loading themes
"""
import dearpygui.dearpygui as dpg
from src.gui.theme import Theme
from src.core.paths import theme_dir
import os


class ThemeManager:
    def __init__(self):
        self.themes = {}  # Stores themes by name
        self.load_default_themes()

    def load_default_themes(self):
        """Load predefined themes (Light and Dark)."""
        dark_theme = Theme("Dark Theme")
        dark_theme.set_property(dpg.mvAll, dpg.mvThemeCol_WindowBg, [30, 30, 30])
        dark_theme.set_property(dpg.mvAll, dpg.mvThemeCol_Text, [255, 255, 255])

        light_theme = Theme("Light Theme")
        light_theme.set_property(dpg.mvAll, dpg.mvThemeCol_WindowBg, [240, 240, 240])
        light_theme.set_property(dpg.mvAll, dpg.mvThemeCol_Text, [0, 0, 0])

        self.themes["Dark Theme"] = dark_theme
        self.themes["Light Theme"] = light_theme

    def add_theme(self, theme):
        """Add a new theme to the manager."""
        if theme.name in self.themes:
            print(f"Theme '{theme.name}' already exists.")
        else:
            self.themes[theme.name] = theme

    def switch_theme(self, theme_name):
        """Switch to a given theme if it exists."""
        if theme_name in self.themes:
            self.themes[theme_name].apply()
        else:
            print(f"Theme '{theme_name}' not found.")

    def save_theme(self, theme_name, file_path):
        """Save a theme to a JSON file."""
        if theme_name in self.themes:
            self.themes[theme_name].save(file_path)
        else:
            print(f"Theme '{theme_name}' not found.")

    def load_theme(self, file_path):
        """Load a theme from a JSON file."""
        if os.path.exists(file_path):
            theme = Theme.load(file_path)
            self.add_theme(theme)
            return theme
        else:
            print(f"File '{file_path}' not found.")
            return None