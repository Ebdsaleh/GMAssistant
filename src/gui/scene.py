# src/gui/scene.py

"""
This class is responsible for creating Scenes to be loaded by the SceneManager class and presented inside of the
application window.
"""

import dearpygui.dearpygui as dpg


class Scene:
    def __init__(self, dpg, name="New Scene"):
        self.dpg = dpg
        self.name = name
        self.components = {}

    def get_name(self):
        return self.name

    def get_components(self):
        return self.components

    def get_component_by_name(self, name):
        for key, value in self.components.items():
            if key == name:
                return value
        return False

    def does_component_exist(self, name):
        for key in self.components.items():
            if key == name:
                return True
        return False

    def add_component(self, name, comp):
        for key in self.components.items():
            if key == name:
                return False
        self.components[name] = comp
        return True

    def remove_component(self, name):
        if self.does_component_exist(name):
            self.dpg.delete_item(self.components[name])
            del self.components[name]

    def show(self):
        for key, value in self.components.items():
            self.dpg.configure_item(value, show=True)

    def hide(self):
        for key, value in self.components.items():
            self.dpg.configure_item(value, show=False)

    def clear(self):
        for key, value in self.components.items():
            self.dpg.configure_item(value, show=False)
