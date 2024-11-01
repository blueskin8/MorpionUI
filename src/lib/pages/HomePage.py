import flet as ft
from lib.util.changePage import changePage
from lib.components.HomeButton import HomeButton
from lib.components.Title import Title

from lib.pages.PlayerVsIaPage import PlayerVsIaPage
from lib.pages.CreditsPage import CreditsPage

class HomePage:
    def __init__(self, page: ft.Page):
        page.title = "Projet 4 - Morpion Avancé"
        page.window_maximized = True
        page.bgcolor = "#282828"
        page.window_full_screen = True
        page.padding = 0
        page.window_focused = True
    
        width = page.window_width = 1920
        height = page.window_height = 1080
    
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
                spacing=50,
                controls=[
                    HomeButton(
                        action=lambda e: changePage(PlayerVsIaPage, page),
                        current_page=page,
                        text="Joueur contre IA"
                    ),
                    HomeButton(
                        action=lambda e: changePage(CreditsPage, page),
                        current_page=page,
                        text="Crédits"
                    ),
                    HomeButton(
                        action=lambda e: page.window_destroy(),
                        current_page=page,
                        text="Quitter"
                    )                
                ]
            )
        )
        self.page = page