import flet as ft

class DateSelectorComponent:
    def __init__(self):
        self._seletor = ft.TextButton(
            "Selecione a Data",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.selecionar_data
        )
        self._data = None
    
        self.date = ft.DatePicker(
                on_change=self.definir_data
        )

    def definir_data(self, e):
        self._seletor.text = e.data
        self._seletor.update()

    def selecionar_data(self, e):
        self.date.open = True
        self.date.update()
    
    def build(self):
        return ft.Column(
            controls=[
                self._seletor,  # Botão que abre o DatePicker
                self.date  # O DatePicker deve estar na árvore de controles
            ]
        )