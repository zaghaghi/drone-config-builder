from typing import Optional

from kivymd.uix.screen import MDScreen


class ConfigScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._drone_config_path: Optional[str] = None

    def on_pre_enter(self, *args):
        self.ids.filepath.text = self.manager.current_filepath
        self._drone_config_path = self.manager.current_filepath
