# src/gui/title_screen.py

"""
This class is responsible for creating the title screen.
"""

from src.gui.scene import Scene
from src.core.utils import actual_width, actual_height, scale_factor
import dearpygui.dearpygui as scene_dpg

class CreateSessionView(Scene):
    def __init__(self, dpg=scene_dpg, parent=None):
        super().__init__(dpg, name="create_session_view")
        self.dpg = dpg
        self.parent = parent
        self.create()

    def create(self):
        self.dpg.add_text("Create Session:", parent=self.parent.view_container, pos=(10, 10))
        self.dpg.add_text(
            "Enter the session name:", pos=(10, 50),
            parent=self.parent.view_container, show=True
        )
        session_name = self.dpg.add_input_text(
            pos=(220, 50), multiline=False, width=200,
            height=30, parent=self.parent.view_container,
            show=True
        )
        confirm_button = self.dpg.add_button(label="Confirm", pos=(450, 50), parent=self.parent.view_container)

        ruleset_text = self.dpg.add_text("Ruleset:", pos=(10, 100), parent=self.parent.view_container)
        ruleset_selection = self.dpg.add_radio_button(
            items=["Default - (No Ruleset)", "D&D 5e",
                   "Savage Worlds Deluxe Edition",
                   "Savage Worlds Adventure Edition (SWADE)",
                   "Starfinder"],
            parent=self.parent.view_container, pos=(10, 130), show=True)


class LoadSessionView(Scene):
    def __init__(self,dpg=scene_dpg, parent=None):
        super().__init__(dpg, name="load_session_view")
        self.dpg = dpg
        self.parent = parent
        self.create()

    def create(self):
        self.dpg.add_text("Load Session:", parent=self.parent.view_container, pos=(10, 10))
        self.dpg.add_text("Available Sessions:", parent=self.parent.view_container, pos=(10, 50))
        self.dpg.add_button(label="Confirm", pos=(450, 50), parent=self.parent.view_container)
        self.dpg.add_listbox(
            items=["session 1", "session 2", "session 3"], parent=self.parent.view_container, pos=(10, 100))

class JoinSessionView(Scene):
    def __init__(self, dpg=scene_dpg, parent=None):
        super().__init__(dpg, name="join_session_view")
        self.dpg = dpg
        self.parent = parent
        self.create()

    def create(self):
        self.dpg.add_text("Join Session:", parent=self.parent.view_container)


class OptionsView(Scene):
    def __init__(self, dpg=scene_dpg, parent=None):
        super().__init__(dpg, name="options_view")
        self.dpg = dpg
        self.parent = parent
        self.create()

    def create(self):
        self.dpg.add_text("Options:", parent=self.parent.view_container)


class DynamicViewPort(Scene):
    print("Initializing DynamicView...")
    def __init__(self, dpg=scene_dpg):
        super().__init__(dpg, name="dynamic_view")
        self.dpg = dpg
        self.name = "dynamic_view"
        self.view_container = None
        self.section_text_id = None
        self.current_view = None
        self.create()

    def create(self):
        self.view_container = self.dpg.add_window(
            label="dynamic_view", width=800, height=600,
            pos=(actual_width / 2 - 350, actual_height / 5), no_title_bar=True, no_move=True)
        self.add_component("view_container", self.view_container)

    def clear_view(self):
        """Clear all widgets from the view container."""
        if self.view_container:
            try:
                self.dpg.delete_item(self.view_container, children_only=True)
            except Exception as e:
                print(f"Error clearing view: {e}")

    def set_view(self, view):
        """Set a new view in the dynamic viewport."""
        self.clear_view()
        self.current_view = view
        view.create()  # Create the

class ButtonBox(Scene):
    print("Initializing ButtonBox...")
    def __init__(self, dpg=scene_dpg, dynamic_viewport=None):
        super().__init__(dpg, name="button_box")
        self.dynamic_viewport  = dynamic_viewport
        self.dpg = dpg
        self.name = "button_box"
        self.container = None
        self.create()

    def create(self):
        self.container = self.dpg.add_window(
            label="menu_buttons", pos=(300, 300), width=300, height=400, no_background=True, no_title_bar=True,
            no_move=True)
        self.dpg.add_text("Menu Buttons", parent=self.container)

        # Create the buttons and their callbacks
        buttons = [
            ("Create Session", self.on_create_clicked),
            ("Load Session", self.on_load_clicked),
            ("Join Session", self.on_join_clicked),
            ("Options", self.on_options_clicked),
            ("Exit", self.on_exit_clicked)
        ]
        for label, callback in buttons:
            button = self.dpg.add_button(label=label, parent=self.container, width=250, height=50,callback=callback)
            self.add_component(label, button)

    def on_create_clicked(self):
        self.dynamic_viewport.clear_view()
        self.dynamic_viewport.set_view(CreateSessionView(self.dpg, self.dynamic_viewport))

    def on_load_clicked(self):
        self.dynamic_viewport.clear_view()
        self.dynamic_viewport.set_view(LoadSessionView(self.dpg, self.dynamic_viewport))

    def on_join_clicked(self):
        self.dynamic_viewport.clear_view()
        self.dynamic_viewport.set_view(JoinSessionView(self.dpg, self.dynamic_viewport))

    def on_options_clicked(self):
        self.dynamic_viewport.clear_view()
        self.dynamic_viewport.set_view(OptionsView(self.dpg, self.dynamic_viewport))

    def on_exit_clicked(self):
        self.dynamic_viewport.clear_view()
        try:
            self.dpg.stop_dearpygui()
        except Exception as e:
            print(f"Error during shutdown: {e}")


class TitleScreen(Scene):
    def __init__(self, dpg=scene_dpg):
        print("Initialising TitleScreen....")
        super().__init__(dpg, "title_screen")
        self.dpg = dpg
        self.name = "title_screen"
        self.window = None
        self.dynamic_window = None
        self.button_box = None
        self.create_session_view = None
        self.create()
        self.hide()

    def create(self):
        self.window = self.dpg.add_window(label="Title Screen", pos=(0, 0), width=actual_width, height=actual_height,
                                          no_title_bar=True, no_move=True)
        text_id = self.dpg.add_text("Welcome to the Game Master Assistant", parent=self.window,
                                    pos=(actual_width / 2, 10))
        self.dynamic_window = DynamicViewPort(self.dpg)
        self.button_box = ButtonBox(self.dpg, self.dynamic_window)
        self.add_component("test_window", self.window)
        self.add_component("button_box", self.button_box)
        self.add_component("dynamic_window", self.dynamic_window)
