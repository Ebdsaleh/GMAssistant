# src/core/utils.py

"""
This file is for utility functions that are frequently used.
"""

from datetime import datetime
import random
import sys
import os
from src.core.paths import root_dir, sessions_dir
list_states = ["initial", "D4", "D6", "D8", "D10"]


def get_screen_resolution():
    if sys.platform == 'win32':
        import ctypes
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    elif sys.platform == 'darwin': # macOS
        import subprocess
        output = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to get position of every window of desktop']).decode('utf-8')
        width = int(output.splitlines()[1].split(',')[3].strip().replace('}', ''))
        height = int(output.splitlines()[2].split(',')[3].strip().replace('}', ''))
        return width, height
    else: # Linux
        import subprocess
        width = standard_width
        height = standard_height
        output = subprocess.check_output(['xrandr']).decode('utf-8').split('\n')
        for line in output:
            if 'connected' in line:
                resolution = line.split()[0]
                width, height = map(int, resolution.split('x'))
                break
        return width, height

standard_width = 1920
standard_height = 1080
actual_width = get_screen_resolution()[0]
actual_height = get_screen_resolution()[1]
scale_factor = min((actual_width / standard_width), (actual_height / standard_height))


class Message:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Instantiating the Message class')
            cls._instance = super(Message, cls).__new__(cls)
            cls._instance.outputs = {"default": {}}
            cls._instance.log_path = ""
            print(f'Returning {cls._instance}')
            return cls._instance

    @property
    def instance(self):
        return self._instance

    def update_log_path(self, path):
        self._instance.log_path = os.path.join(path, 'log.txt')

    def add_output(self, name:str,  output, add_to_default=True):
        if add_to_default:
            self.outputs["default"][name] = output
        self.outputs[name] = output

    def __call__(self, message, *modes):
        if len(modes) == 0:
            for key, value in self.outputs["default"].items():
                value(message)
        else:
            for mode in modes:
                self.outputs[mode](message)

    def remove_output(self, output_name):
        if output_name in self.outputs:
            del self.outputs[output_name]
            del self.outputs["default"][output_name]
            self._instance(f"Succesfully removed {output_name} from outputs.")
        else:
            self._instance(f"{output_name} not found in list of outputs.")


msg_instance = Message()
msg_instance.add_output("console", print)
msg_instance.add_output("log", lambda x: open(msg_instance.log_path, 'a').write(x+'\n'))
# Message().add_output(lambda x: open(os.path.join(session_dir, 'logs', 'log.txt'), 'a').write(x+'\n'))


def generate_new_random_seed():
    factor = random.randint(1, 1234)
    new_seed = int(datetime.now().timestamp())
    if factor % 2 == 0:
        new_seed += factor
    else:
        new_seed -= factor
    return new_seed
