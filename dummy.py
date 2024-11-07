import flet as ft

def main(page: ft.Page):
    # Set the background color for the page
    page.bgcolor = "lightblue"

    # Pattern overlay container
    pattern_overlay = ft.Container(
        width=page.width,
        height=page.height,
        image_src="pattern2.png",  # Path to your pattern image
        image_repeat=ft.ImageRepeat.REPEAT,
        opacity=1  # Adjust opacity to allow background color to show through
    )

    # Button in the center
    button = ft.ElevatedButton("Click Me", width=200)

    # Stack to overlay pattern and button
    page.add(
        ft.Stack(
            [
                pattern_overlay,
                ft.Container(content=button, alignment=ft.alignment.center)
            ],
            width=page.width,
            height=page.height
        )
    )

# Make sure "pattern_image.png" is in your project directory
ft.app(target=main)
