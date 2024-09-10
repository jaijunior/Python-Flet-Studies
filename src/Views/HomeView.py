import flet as ft
from .ConfigView import ConfigView
from .Tickets.TicketsView import TicketsView

class HomeView():
    def __init__(self, page: ft.Page):
        self.page = page
        self.tasks = []
        self.new_task = ft.TextField(hint_text="O que precisa ser feito?", expand=True)

    def add_task(self, e):
    # # Cria uma nova tarefa e adiciona na lista
    # task_item = TaskItemView(self.page, self.new_task.value)
    # self.tasks.append(task_item.build())
    # self.page.update()
    # self.new_task.value = ""
        pass

    def abrir_config(self, e):
        config_view = TicketsView(self.page)
        self.page.views.append(config_view.build())
        self.page.go("/tickets")

    def build(self):
        # Retorna a interface principal da tela To-Do
        return ft.View(
            "/todo",
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.ElevatedButton("Adicionar", on_click=self.abrir_config)
                    ]
                ),
                ft.Column(self.tasks, spacing=10),
            ]
        )