from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.title = "Drone Config Editor"
        resource_add_path("dronebuilder/screens")
        return Builder.load_file("manager.kv")


if __name__ == "__main__":
    MainApp().run()
