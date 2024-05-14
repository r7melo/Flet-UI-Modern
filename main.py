import flet as ft
from data import ReturnData
from generate_card import CardGenerator

def main(page: ft.Page):

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    
    dic = ReturnData()
    _cards = [
        CardGenerator(
            dic[key]["colors"],
            dic[key]["title"],
            dic[key]["subtitle"],
            dic[key]["price"],
            dic[key]["icon"],
            dic[key]["card_icon"],
            dic[key]["card_type"],
            dic[key]["card_number"]
        )
        for key in dic 
    ]
    
    _main_conteiner = ft.Container(
        expand=True,
        margin=-10,
        gradient=ft.RadialGradient(
            center=ft.Alignment(0, -1.25),
            radius=1.4,
            colors=[
                "#694742",
                "#67413e",
                "#64393b",
                "#613137",
                "#5e2934",
                "#591f32",
                "#541530",
                "#4e0a30",
                "#480130",
                "#410031",
                "#3a0033"
            ],
        ),
        padding=15,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    alignment="center",
                    controls=_cards
                )
            ]
        )
    )

 



    page.add(_main_conteiner)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')
