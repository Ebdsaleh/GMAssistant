# src/core/paths.py

"""
This file is to store program-wide paths.
"""
import os
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sessions_dir = os.path.join(root_dir, "sessions")
src_dir = os.path.join(root_dir, "src")
core_dir = os.path.join(src_dir, "core")
gui_dir = os.path.join(src_dir, "gui")
theme_dir = os.path.join(root_dir, "themes")
