import flet as ft
from Views.HomeView import HomeView

def main(page: ft.Page):
    home_view = HomeView(page)

    page.views.append(home_view.build())
    page.update()

ft.app(target=main)

