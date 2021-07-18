from os.path import expanduser, split

from dronebuilder.components.filemanager import DroneFileManager
from dronebuilder.utils.storage import setting
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class RecentFileListItem(OneLineListItem):
    def __init__(self, filepath):
        directory, filename = split(filepath)
        user_home = expanduser("~")
        if directory.startswith(user_home):
            directory = "~" + directory[len(user_home) :]
        item_text = (
            f"{filename} [color=#888][i][size=14sp]{directory}[/size][/i][/color]"
        )
        super().__init__(text=item_text)
        self.theme_text_color = "Custom"
        self.text_color = (0.8, 0.8, 0.8, 1)
        self._filepath = filepath

    @property
    def filepath(self):
        return self._filepath


class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=Clock.create_trigger(self._create_recent_file_items))

    def _create_recent_file_items(self, *args):
        for filepath in setting.get_recent_files():
            list_item = RecentFileListItem(filepath)
            list_item.bind(on_release=self._item_selected)
            self.ids.recent_files_container.add_widget(list_item)

    def _item_selected(self, list_item: RecentFileListItem) -> None:
        self.open_drone_file(list_item.filepath)

    def browse_open_drone_file(self) -> None:
        manager = DroneFileManager(
            opentype="open", select_callback=self.select_drone_file
        )
        manager.show()

    def browse_new_drone_file(self) -> None:
        manager = DroneFileManager(
            opentype="new", select_callback=self.select_drone_file
        )
        manager.show()

    def select_drone_file(self, filepath: str) -> None:
        self.manager.current_filepath = filepath
        self.manager.current = "config"
