# src/gui/scene_manager.py


""""
This class is responsible for initialising  and transitioning scenes from the application window.
"""

from src.gui.title_screen import TitleScreen


class SceneManager:
    def __init__(self, app_window):
        self.app_window = app_window
        self.scene_list = []
        self.populate_scene_list()
        self.current_scene = None

    def populate_scene_list(self):
        title = TitleScreen(self.app_window.dpg)
        self.scene_list.append(title)

    def load_scene(self, scene_name):
        if self.current_scene:
            self.current_scene.clear()
        for scene in self.scene_list:
            if scene_name == scene.name:
                try:
                    self.current_scene = scene
                    print(f"Scene created: {self.current_scene}")
                    self.current_scene.show()
                except Exception as e:
                    print(f"Error while creating scene: {e}")
