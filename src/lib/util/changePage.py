import flet as ft

def changePage(page, current_page: ft.Page):
    current_page.clean()
    page(current_page)