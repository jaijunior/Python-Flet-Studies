import flet as ft

class ConfigView():
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.View(
            "/config",
            controls = [
                ft.TextField(password=True)
            ]
         )
