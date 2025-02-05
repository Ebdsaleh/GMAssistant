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
        # Ensure the themes directory exists
        if not os.path.exists(theme_dir):
            os.mkdir(theme_dir)
            self.load_default_themes()
        self.load_themes()

    def load_themes(self):

        """Load all themes from the themes directory"""
        for file in os.listdir(theme_dir):
            if file.endswith(".json"):
                theme_name = file.replace(".json", "")
                theme_path = os.path.join(theme_dir, file)
                self.themes[theme_name] = Theme.load(theme_path, theme_name)

    def save_theme(self, theme):
        """Save a theme to the themes directory"""
        theme_path = os.path.join(theme_dir, f"{theme.name}.json")
        theme.save(theme_path)

    def load_default_themes(self):
        """Load predefined themes (Light and Dark)."""
        dark_theme = Theme("Dark Theme")
        dark_theme.set_property(dpg.mvAll, dpg.mvThemeCol_WindowBg, [30, 30, 30])
        dark_theme.set_property(dpg.mvAll, dpg.mvThemeCol_Text, [255, 255, 255])

        light_theme = Theme("Light Theme")
        light_theme.set_property(dpg.mvAll, dpg.mvThemeCol_WindowBg, [240, 240, 240])
        light_theme.set_property(dpg.mvAll, dpg.mvThemeCol_Text, [0, 0, 0])

        self.save_theme(dark_theme)
        self.save_theme(light_theme)
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

