# src/gui/app_window.py

"""
This class will contain application window. This file will expose a singleton called app_handle which can be used
for other classes to access items inside the application's presentation.
"""

import dearpygui.dearpygui as dpg
from src.core.utils import actual_width, actual_height
from src.gui.scene_manager import SceneManager

class AppWindow:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppWindow, cls).__new__(cls)

            return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialize = True
            self.dpg = dpg
            self.theme_manager = None
            self.scene_manager = None

    def init_ui(self):
        self.dpg.create_context()
        self.dpg.set_global_font_scale(1.25)
        self.dpg.create_viewport(title="Game Master Assistant", width=actual_width, height=actual_height)
        # self.theme_manager = ThemeManager()
        self.scene_manager = SceneManager(self)
        self.scene_manager.load_scene("title_screen")
        self.dpg.setup_dearpygui()
        self.dpg.show_viewport()
        self.dpg.start_dearpygui()

        def close(self):
            self._instance.dpg.destroy_context()


app_handle = AppWindow()