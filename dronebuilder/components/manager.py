from typing import Optional

from kivy.uix.screenmanager import ScreenManager


class WindowManager(ScreenManager):
    current_filepath: Optional[str] = None
