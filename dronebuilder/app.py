from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class WindowManager(ScreenManager):
    ...


class MainApp(MDApp):
    def build(self):
        resource_add_path("dronebuilder/screens")
        return Builder.load_file("manager.kv")


if __name__ == "__main__":
    MainApp().run()
