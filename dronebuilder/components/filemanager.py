from os.path import dirname, join
from typing import Callable, Optional

from dronebuilder.utils.storage import setting
from kivymd.uix.filemanager import MDFileManager


class DroneFileManager:
    def __init__(
        self,
        opentype: str = "open",
        select_callback: Optional[Callable[[str], None]] = None,
    ):
        self._path = setting.get_last_path()
        self._file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.open_drone_file
            if opentype == "open"
            else self.new_drone_file,
            ext=[".yml", ".yaml"] if opentype == "open" else ["~"],
            current_path=self._path,
            show_hidden_files=True,
            selector="file" if opentype == "open" else "folder",
        )
        self._select_callback = select_callback

    def exit_manager(self, *args):
        self._file_manager.close()

    def open_drone_file(self, file):
        setting.set_last_path(dirname(file))
        setting.add_to_recent_files(file)
        if self._select_callback:
            self._select_callback(file)
        self.exit_manager()

    def new_drone_file(self, path):
        file = join(path, ".drone.yml")
        setting.set_last_path(path)
        setting.add_to_recent_files(file)
        if self._select_callback:
            self._select_callback(file)
        self.exit_manager()

    def show(self):
        self._file_manager.show(self._path)
