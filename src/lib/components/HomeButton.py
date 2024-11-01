import flet as ft

class HomeButton(ft.Container):
    def __init__(self, action, current_page: ft.Page, text: str):

        def on_hover(e):
            if e.data == "true":
                e.control.content.color = ft.colors.GREY_600
            else:
                e.control.content.color = ft.colors.WHITE
            e.control.content.update()

        super().__init__(
            content=ft.Text(
                value=text,
                size=40,
                weight=ft.FontWeight.NORMAL,
                width=current_page.window_width,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
            ),
            on_click=action,
            on_hover=on_hover
        )