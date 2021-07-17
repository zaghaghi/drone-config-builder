from os.path import dirname, join

from dronebuilder.utils.storage import setting
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager


class DroneFileManager:
    def __init__(self, opentype: str = "open"):
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

    def exit_manager(self, *args):
        self._file_manager.close()

    def open_drone_file(self, file):
        setting.set_last_path(dirname(file))
        setting.add_to_recent_files(file)
        toast(file)
        self.exit_manager()

    def new_drone_file(self, path):
        setting.set_last_path(path)
        setting.add_to_recent_files(join(path, ".drone.yml"))
        toast(path)
        self.exit_manager()

    def show(self):
        self._file_manager.show(self._path)
