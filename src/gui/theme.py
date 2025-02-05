# src/gui/theme.py

"""
This class is responsible for creating the Theme that will be loaded by the ThemeManager.
"""

import dearpygui.dearpygui as dpg
import json

class Theme:
    def __init__(self, name):
        self.name = name
        self.properties = {}  # Stores the theme's properties (colors, styles, images).

    def set_property(self, widget_type, property_name, value):
        """Update a specific property for a widget type."""
        if widget_type not in self.properties:
            self.properties[widget_type] = {}
        self.properties[widget_type][property_name] = value


    def apply(self):
        """Apply the theme to the entire UI."""
        with dpg.theme() as theme:
            for widget_type, props in self.properties.items():
                with dpg.theme_component(widget_type):
                    for prop, value in props.items():
                        if isinstance(value, list):  # Colors
                            dpg.add_theme_color(prop, value)
                        elif isinstance(value, tuple):  # Style settings (size, padding)
                            dpg.add_theme_style(prop, *value)
        dpg.bind_theme(theme)

    def save(self, file_path):
        """Save theme to a file."""
        with open(file_path, "w") as f:
            json.dump(self.properties, f, indent=4)

    @classmethod
    def load(cls, file_path, name="Custom Theme"):
        """Load theme from a file."""
        with open(file_path, "r") as f:
            properties = json.load(f)
        theme = cls(name)
        theme.properties = properties
        return theme