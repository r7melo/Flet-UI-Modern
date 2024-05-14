import flet as ft

class CardGenerator(ft.UserControl):
    def __init__(
        self,
        colors:list,
        title: str,
        subtitle: str,
        price: str,
        icon: str,
        card_icon: str,
        card_type: str,
        card_number:str
    ):
        
        self.colors = colors
        self.title = title
        self.subtitle = subtitle
        self.price = price
        self.icon = icon
        self.card_icon = card_icon
        self.card_type = card_type
        self.card_number = card_number

        super().__init__()

    def show_price(self, e):
        if e.data == "true":
            self.animated_text.offset = ft.transform.Offset(0, 0)
            self.animated_text.opacity = 1
            self.animated_text.update()
        else:
            self.animated_text.offset = ft.transform.Offset(0.25, 0)
            self.animated_text.opacity = 0
            self.animated_text.update()

    def build(self):

        # animation card
        self.animated_card = ft.Container(
            offset=ft.transform.Offset(0,0),
            animate_offset=ft.animation.Animation(900),
            content=ft.Card(
                width=64,
                height=64,
                elevation=20,
                content=ft.Container(
                    width=56,
                    height=56,
                    border_radius=20,
                    image_src= self.icon
                )
            )
        )

        # animation text
        self.animated_text = ft.Text(
            self.price,
            size=18,
            weight="bold",
            offset=ft.transform.Offset(0.35, 0),
            animate_offset=ft.animation.Animation(duration=900, curve="decelerate"),
            animate_opacity=300,
            opacity=0
        )

        # animation conteiner

        self.main_card = ft.Container(
            gradient=ft.RadialGradient(
                center=ft.Alignment(0.8, 0.8),
                radius=1.4,
                colors=self.colors
            ),
            width=210,
            height=260,
            border_radius=35,
            alignment=ft.alignment.bottom_center,
            content=ft.Column(
                alignment="end",
                horizontal_alignment="end",
                controls=[
                    ft.Column(
                        expand=True,
                        alignment="start",
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=210, 
                                        height=100,
                                        content=ft.Row(
                                            spacing=5,
                                            controls=[
                                                ft.Column(
                                                    alignment="center",
                                                    controls=[
                                                        ft.Container(
                                                            width=80,
                                                            height=64,
                                                            padding=ft.padding.only(left=10),
                                                            alignment=ft.alignment.center,
                                                            content=self.animated_card
                                                        )
                                                    ]
                                                ),
                                                ft.Column(
                                                    horizontal_alignment="start",
                                                    alignment="start",
                                                    controls=[
                                                        ft.Container(
                                                            width=120,
                                                            height=100,
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text(
                                                                        self.title,
                                                                        size=16
                                                                    ),
                                                                    ft.Text(
                                                                        self.subtitle,
                                                                        size=12,
                                                                        color="white54"
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Row(
                                vertical_alignment="end",
                                alignment="end",
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        width=100,
                                        height=150,
                                        content=ft.Column(
                                            alignment="end",
                                            controls=[
                                                ft.Container(
                                                    padding=ft.padding.only(bottom=35, left=10),
                                                    content=self.animated_text
                                                )
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        on_hover=lambda e: self.show_price(e),
                                        width=100,
                                        height=120,
                                        bgcolor="white10",
                                        border_radius=ft.border_radius.only(top_left=25, bottom_right=35),
                                        content=ft.Column(
                                            spacing=1,
                                            controls=[
                                                ft.Row(
                                                    alignment="start",
                                                    controls=[
                                                        ft.Container(
                                                            width=100,
                                                            height=40,
                                                            padding=15,
                                                            content=ft.Column(
                                                                spacing=5,
                                                                controls=[
                                                                    ft.Container(
                                                                        width=21,
                                                                        height=21,
                                                                        image_src=self.card_icon
                                                                    ),
                                                                    ft.Text(
                                                                        self.card_type,
                                                                        size=12,
                                                                        color="white70"                                                                                
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                ),
                                                ft.Container(
                                                    padding=ft.padding.only(bottom=35)
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            padding=15,
                                                            width=100,
                                                            height=60,
                                                            content=ft.Text(
                                                                self.card_number,
                                                                size=12,
                                                                color="white70"
                                                            )
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ],
                    )
                ]
            )
        )

        return self.main_card