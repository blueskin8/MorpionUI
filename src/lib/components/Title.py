import flet as ft

class Title(ft.Container):
    def __init__(self, current_page: ft.Page, title: str):
        super().__init__(
            width=current_page.window_width,
            height=current_page.window_height / 3,
            bgcolor="#66000000",
            alignment=ft.alignment.center,
            margin=ft.margin.all(0),
            padding=ft.padding.all(0),
            content=ft.Text(
                value=title,
                size=45,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            )
        )