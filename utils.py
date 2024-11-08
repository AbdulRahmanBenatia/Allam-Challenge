import arabic_reshaper
from bidi.algorithm import get_display
import flet as ft

SMALL_BTN_SIZE = 20
LARGE_BTN_SIZE = 28

# Handling Arabic Text
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text




def Text(text, size=28, font_family="Amiri"):
    return ft.Text(text, size=size, font_family=font_family)