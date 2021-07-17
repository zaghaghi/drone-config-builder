from os.path import exists, expanduser
from typing import List

from kivy.storage.jsonstore import JsonStore


class SettingStore(JsonStore):
    RECENT_FILES: str = "recent_files"
    RECENT_PATH: str = "recent_path"
    DEFAULT_RECENT_FILES_COUNT: int = 10

    def __init__(self):
        super().__init__("settings.json", indent=2)
        if not exists("settings.json"):
            self.create_default_values()

    def create_default_values(self) -> None:
        self.put(
            self.RECENT_FILES,
            files=[],
            recent_files_count=self.DEFAULT_RECENT_FILES_COUNT,
        )
        self.put(self.RECENT_PATH, path=expanduser("~"))

    def get_recent_files(self) -> List[str]:
        return self.get(self.RECENT_FILES).get("files", [])

    def add_to_recent_files(self, file: str) -> None:
        recent_files = self.get(self.RECENT_FILES)
        recent_files_list = recent_files["files"]
        if file in recent_files_list:
            recent_files_list.remove(file)
        recent_files_list.insert(0, file)
        recent_files_count = recent_files.get(
            "recent_files_count", self.DEFAULT_RECENT_FILES_COUNT
        )
        if len(recent_files_list) > recent_files_count:
            recent_files_list = recent_files_list[:recent_files_count]
        recent_files["files"] = recent_files_list
        self.put(self.RECENT_FILES, **recent_files)

    def get_last_path(self) -> str:
        return self.get(self.RECENT_PATH).get("path", expanduser("~"))

    def set_last_path(self, path: str) -> None:
        self.put(self.RECENT_PATH, path=path)


setting = SettingStore()
