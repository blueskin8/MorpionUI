import flet as ft
from lib.components.Title import Title
from lib.util.changePage import changePage

class CreditsPage:
    def __init__(self, page: ft.Page):
        page.title = "Projet 4 - Morpion Avancé - Crédits"
        page.window_maximized = True
        page.bgcolor = "#282828"
        page.window_full_screen = True
        page.padding = 0
        page.window_focused = True
    
        width = page.window_width = 1920
        height = page.window_height = 1080

        from lib.pages.HomePage import HomePage
    
        page.add(
            Title(
                current_page=page,
                title="Projet 4 - Morpion Avancé"
            ),
            ft.Column(
                expand=True,
                width=width,
                height=height / 3 * 2,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text(
                        value="Développé par Alban GARCIA",
                        size=40,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        width=width
                    ),
                    ft.Text(
                        value="à l'aide de Thomas JULIEN-BITON",
                        size=40,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        width=width
                    ),
                    ft.Text(
                        value="en utilisant Flet, une librairie d'ui basée sur Flutter de Google",
                        size=40,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        width=width
                    ),
                    ft.Text(
                        value="Merci d'avoir joué",
                        size=40,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        width=width
                    ),
                    ft.Text(
                        value="© 2024 - FouinardC - Tous droits réservés",
                        size=40,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        width=width
                    ),
                    ft.ElevatedButton(
                        content=ft.Text(
                            value="Retourner au menu principal",
                            size=40,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.WHITE
                        ),
                        on_click=lambda e: changePage(page=HomePage, current_page=page)
                    )
                ]
            )
        )
        self.page = page