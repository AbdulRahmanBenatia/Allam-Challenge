import arabic_reshaper
from bidi.algorithm import get_display
import flet as ft

SMALL_BTN_SIZE = 20
LARGE_BTN_SIZE = 28

HOME_BTN_STYLE = ft.ButtonStyle(   bgcolor={
                "": "#282753",   
                "hovered": "#645483",     
                
            },
            )
SEND_BTN_STYLE = ft.ButtonStyle(   bgcolor={
                "": "#3E4651",   
                "hovered": "#5B6370",     
                
            },
            )

BACK_BTN_STYLE = ft.ButtonStyle(   bgcolor={
                "": "#8B0000",         # Default color (dark red)
                "hovered": "#B22222"   # Lighter red on hover
                
            },
            )


TEXT_INPUT_STYLE = ft.ButtonStyle(   bgcolor={
                "": "#3E4651",   
                
            },
            )


# Handling Arabic Text
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text




def Text(text, size=26, font_family="Amiri"):
    return ft.Text(text, size=size, font_family=font_family,color="#EF79C2")