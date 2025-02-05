# src/gui/theme_builder.py
"""This class is responsible for creating, modifying and applying themes."""

import dearpygui.dearpygui as dpg
from src.gui.theme_manager import ThemeManager
from src.gui.theme import Theme


class ThemeBuilder:
    def __init__(self):
        self.theme_manager = ThemeManager()
        self.current_theme = None
        self.create_ui()

    def create_ui(self):
        with dpg.window(label="Theme Builder", width=600, height=500, no_collapse=True):
            dpg.add_text("Select Theme:")
            self.theme_selector = dpg.add_combo(
                items=list(self.theme_manager.themes.keys()),
                callback=self.on_theme_selected,
                default_value="Dark Theme"
            )
            dpg.add_separator()

            dpg.add_text("Modify Colors:")
            self.color_picker = dpg.add_color_picker(
                default_value=[255, 255, 255, 255],
                callback=self.on_color_changed
            )

            dpg.add_button(label="Save Theme", callback=self.save_theme)

    def on_theme_selected(self, sender, app_data):
        theme_name = app_data
        self.current_theme = self.theme_manager.themes.get(theme_name, None)
        print(f"Selected theme: {theme_name}")

    def on_color_changed(self, sender, app_data):
        if self.current_theme:
            self.current_theme.set_property(dpg.mvAll, dpg.mvThemeCol_Text, app_data[:3])
            self.current_theme.apply()
            print(f"Updated text color to: {app_data[:3]}")

    def save_theme(self):
        if self.current_theme:
            self.theme_manager.save_theme(self.current_theme.name, f"{self.current_theme.name}.json")
            print(f"Theme '{self.current_theme.name}' saved.")