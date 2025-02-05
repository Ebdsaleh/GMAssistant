# src/gui/title_screen.py

"""
This class is responsible for creating the title screen.
"""

from src.gui.scene import Scene
from src.core.utils import actual_width, actual_height
import dearpygui.dearpygui as scene_dpg

class DynamicViewPort(Scene):
    print("Initializing DynamicView...")
    def __init__(self, dpg=scene_dpg):
        super().__init__(dpg, name="dynamic_view")
        self.dpg = dpg
        self.name = "dynamic_view"
        self.view_container = None
        self.section_text_id = None
        self.create()

    def create(self):
        self.view_container = self.dpg.add_window(
            label="dynamic_view", width=800, height=600,
            pos=(actual_width / 2 - 350, actual_height / 5), no_title_bar=True, no_move=True)
        self.section_text_id = self.dpg.add_text(label="Content will display here dynamically.",
                                                 parent=self.view_container)
        self.add_component("view_container", self.view_container)
        self.add_component("section_text", self.section_text_id)

    def clear_section_text(self):
        if self.section_text_id:
            self.dpg.set_value(self.section_text_id, "")

    def set_section_text(self, new_text):
        print(f"set_section_text: {new_text}")
        if self.section_text_id:
            self.dpg.set_value(self.section_text_id, new_text)


class ButtonBox(Scene):
    print("Initializing ButtonBox...")
    def __init__(self, dpg=scene_dpg):
        super().__init__(dpg, name="button_box")
        self.dpg = dpg
        self.name = "button_box"
        self.container = None
        self.create()

    def create(self):
        self.container = self.dpg.add_window(
            label="menu_buttons", pos=(300, 300), width=300, height=400, no_background=True, no_title_bar=True,
            no_move=True)
        text_id = self.dpg.add_text("Menu Buttons", parent=self.container)
        btn_create_session = self.dpg.add_button(
            label="Create Session", parent=self.container, width=250, height=50)
        btn_load_session = self.dpg.add_button(
            label="Load Session", parent=self.container, width=250, height=50)
        btn_join_session = self.dpg.add_button(
            label="Join Session", parent=self.container, width=250, height=50)
        btn_options = self.dpg.add_button(
            label="Options", parent=self.container, width=250, height=50)
        btn_exit = self.dpg.add_button(
            label="Exit", parent=self.container, width=250, height=50)
        self.add_component("container", self.container)
        self.add_component("text", text_id)
        self.add_component("create_button", btn_create_session)
        self.add_component("load_button", btn_load_session)
        self.add_component("join_button", btn_join_session)
        self.add_component("options_button", btn_options)
        self.add_component("exit_button", btn_exit)

    def set_create_button_callback(self, callback_func):
        button = self.get_component_by_name("create_button")
        self.dpg.configure_item(button, callback=callback_func)

    def set_load_button_callback(self, callback_func):
        button = self.get_component_by_name("load_button")
        self.dpg.configure_item(button, callback=callback_func)

    def set_join_button_callback(self, callback_func):
        button = self.get_component_by_name("join_button")
        self.dpg.configure_item(button, callback=callback_func)

    def set_options_button_callback(self, callback_func):
        button = self.get_component_by_name("options_button")
        self.dpg.configure_item(button, callback=callback_func)

    def set_exit_button_callback(self, callback_func):
        button = self.get_component_by_name("exit_button")
        self.dpg.configure_item(button, callback=callback_func)



class TitleScreen(Scene):
    def __init__(self, scene_dpg):
        print("Initialising TitleScreen....")
        super().__init__(scene_dpg, "title_screen")
        self.dpg = scene_dpg
        self.name = "title_screen"
        self.window = None
        self.dynamic_window = None
        self.button_box = None
        self.create()
        self.hide()

    def create(self):
        self.window = self.dpg.add_window(label="Title Screen", pos=(0, 0), width=actual_width, height=actual_height,
                                          no_title_bar=True, no_move=True)
        text_id = self.dpg.add_text("Welcome to the Game Master Assistant", parent=self.window,
                                    pos=(actual_width / 2, 10))
        self.button_box = ButtonBox(self.dpg)
        self.dynamic_window = DynamicViewPort(self.dpg)
        self.add_component("test_window", self.window)
        self.add_component("text", text_id)
        self.add_component("button_box", self.button_box)
        self.add_component("dynamic_window", self.dynamic_window)
        self.get_component_by_name("button_box").set_create_button_callback(self.on_create_clicked)
        self.get_component_by_name("button_box").set_load_button_callback(self.on_load_clicked)
        self.get_component_by_name("button_box").set_join_button_callback(self.on_join_clicked)
        self.get_component_by_name("button_box").set_options_button_callback(self.on_options_clicked)
        self.get_component_by_name("button_box").set_exit_button_callback(self.on_exit_clicked)

    def on_create_clicked(self):
        self.dynamic_window.clear_section_text()
        self.dynamic_window.set_section_text("Create Session:")

    def on_load_clicked(self):
        self.dynamic_window.clear_section_text()
        self.dynamic_window.set_section_text("Load Session:")

    def on_join_clicked(self):
        self.dynamic_window.clear_section_text()
        self.dynamic_window.set_section_text("Join Session:")

    def on_options_clicked(self):
        self.dynamic_window.clear_section_text()
        self.dynamic_window.set_section_text("Options:")

    def on_exit_clicked(self):
        self.clear()
        quit(0)
