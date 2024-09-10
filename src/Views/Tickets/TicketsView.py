import flet as ft
from components.Date.DateSelectorComponent import DateSelectorComponent

class TicketsView():
    def __init__(self, page: ft.Page):
        self.page = page
        self._data_inicial = DateSelectorComponent()

    def build(self):
        return ft.View(
            "/tickets",
            controls= [
                ft.Text("Tickets"),
                ft.Row(
                    controls= [
                        self._data_inicial.build()          
                    ]
                )
            ]
        )