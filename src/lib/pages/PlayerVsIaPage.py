import flet as ft
from lib.util.changePage import changePage
from lib.components.Title import Title
from lib.classes.Morpion import MorpionGame
from time import sleep

class PlayerVsIaPage:
    def __init__(self, page: ft.Page):
        self.size = 0
        page.title = "Projet 4 - Morpion Avancé - Joueur contre IA"
        page.window_maximized = True
        page.bgcolor = "#282828"
        page.window_full_screen = True
        page.padding = 0
        page.window_focused = True

        self.game = MorpionGame()

        page.add(
            Title(
                current_page=page,
                title="Joueur contre IA"
            ),
            self.create_grid()
        )

        self.page = page

    def create_grid(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Text(
                                    value="Tour du joueur",
                                    size=40,
                                    color=ft.colors.WHITE,
                                    text_align=ft.TextAlign.CENTER,
                                    width=800
                                ),
                                margin=ft.margin.symmetric(vertical=40)
                            ),
                            ft.Row([self.create_button(1), self.create_button(2), self.create_button(3), self.size_button(0), ft.Text(
                                value="Pions restants",
                                size=40,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                                width=500
                            )]),
                            ft.Row([self.create_button(4), self.create_button(5), self.create_button(6), self.size_button(1), ft.Text(
                                value=f"Blanc : {self.game.white_pawns[0]} ◽, {self.game.white_pawns[1]} ◻️, {self.game.white_pawns[2]} ⬜",
                                size=40,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                                width=500
                            )]),
                            ft.Row([self.create_button(7), self.create_button(8), self.create_button(9), self.size_button(2), ft.Text(
                                value=f"Noir : {self.game.black_pawns[0]} ◾, {self.game.black_pawns[1]} ◼️, {self.game.black_pawns[2]} ⬛",
                                size=40,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                                width=500
                            )]),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                )
            ]
        )

    def actualise_page(self):
        for i in range(3):
            for j in range(3):
                self.page.controls[1].controls[0].content.controls[i+1].controls[j].content.value = self.game.get_visual(i*3+j+1)
                self.page.controls[1].controls[0].content.controls[i+1].controls[j].content.update()

    def on_winner(self):
        self.page.controls[1].controls[0].content.controls[0].content.value = "Match nul, personne n'a gagné !" if self.game.winner == "nul" else f"Le joueur {"blanc" if self.game.winner == 'b' else "noir"} a gagné !"
        self.page.controls[1].controls[0].content.controls[0].content.update()
        self.game.state = "end"
        for i in range(3):
            self.page.controls[1].controls[0].content.controls[i+1].clean()
            self.page.controls[1].controls[0].content.controls[i+1].update()
        from lib.pages.HomePage import HomePage
        self.page.controls[1].controls[0].content.spacing = 40
        self.page.controls[1].controls[0].content.controls[0].content.margin = ft.margin.all(0)
        self.page.controls[1].controls[0].content.controls[0].content.update()
        self.page.controls[1].controls[0].content.controls[1] = ft.ElevatedButton(
            content=ft.Text(
                value="Revenir au menu principal",
                size=40,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE
            ),
            on_click=lambda e: changePage(page=HomePage, current_page=self.page),
        )
        self.page.controls[1].controls[0].content.controls[2] = ft.ElevatedButton(
            content=ft.Text(
                value="Rejouer",
                size=40,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE
            ),
            on_click=lambda e: changePage(page=PlayerVsIaPage, current_page=self.page),
        )
        self.page.controls[1].controls[0].content.update()

    def update_remaining_pawns(self):
        self.page.controls[1].controls[0].content.controls[2].controls[4].value = f"Blanc : {self.game.white_pawns[0]} ◽, {self.game.white_pawns[1]} ◻️, {self.game.white_pawns[2]} ⬜"
        self.page.controls[1].controls[0].content.controls[3].controls[4].value = f"Noir : {self.game.black_pawns[0]} ◾, {self.game.black_pawns[1]} ◼️, {self.game.black_pawns[2]} ⬛"
        self.page.controls[1].controls[0].content.controls[2].controls[4].update()
        self.page.controls[1].controls[0].content.controls[3].controls[4].update()

    def on_click(self, event: ft.ControlEvent, case: int):
        if self.game.state == "playing":
            if self.game.player_turn(case=case, size=self.size):
               if self.game.player == "b":
                   self.update_remaining_pawns()
                   self.game.state = "ia"
                   self.page.controls[1].controls[0].content.controls[0].content.value = "L'IA réfléchit..."
                   self.page.controls[1].controls[0].content.controls[0].content.update()
                   for i in range(3):
                       self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.disabled = True
                       self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.update()
                   if self.game.check_winner() == None:
                       sleep(2)
                       self.game.ia_turn()
                       self.update_remaining_pawns()
                       if self.game.check_winner() == None:
                           self.page.controls[1].controls[0].content.controls[0].content.value = "Tour du joueur"
                           self.page.controls[1].controls[0].content.controls[0].content.update()
                           for i in range(3):
                               self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.disabled = False
                           self.page.controls[1].controls[0].content.controls[self.size+1].controls[3].content.disabled = True
                           for i in range(3):
                               self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.update()
                           self.actualise_page()
                           self.game.state = "playing"
                       else: self.on_winner()
                   else:
                       self.on_winner()

    def create_button(self, case: int):
        def oc(e):
            self.on_click(e, case)

        def oh(e):
            if(self.game.state == "playing"):
                self.on_hover_button(e, case)

        return ft.ElevatedButton(
            content=ft.Text(
                value=" ",
                size=60,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
            on_click=oc,
            on_hover=oh,
            bgcolor=ft.colors.GREY_700,
            width=150,
            height=150
        )

    def size_button(self, size: int):

        def change_size(e):
            self.size = size
            for i in range(3):
                self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.disabled = False
                self.page.controls[1].controls[0].content.controls[i+1].controls[3].content.update()
            e.control.disabled = True
            e.control.update()

        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(
                    value="Petit" if size == 0 else ("Moyen" if size == 1 else "Gros"),
                    size=40,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.WHITE
                ),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10)
                ),
                bgcolor=ft.colors.GREY_700,
                width=300,
                height=150,
                on_click=change_size,
                disabled=True if size == 0 else False
            ),
            margin=ft.margin.only(left=50)
        )

    def on_hover_button(self, event: ft.ControlEvent, case: int):
        button = event.control
        if event.data == "true" and self.game.can_pose(case=case, size=self.size):
            button.content.value = "◽" if self.size == 0 else ("◻️" if self.size == 1 else "⬜")
        else:
            button.content.value = self.game.get_visual(case)
        button.update()


        #   ◽◾◻️◼️⬜⬛