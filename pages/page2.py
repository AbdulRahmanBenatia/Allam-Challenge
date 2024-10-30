from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown


BUHOOR = [ #These are only 14
    "السريع",
    "الكامل",
    "المتقارب",
    "المتدارك",
    "المنسرح",
    "المديد",
    "المجتث",
    "الرمل",
    "البسيط",
    "الخفيف",
    "الطويل",
    "الوافر",
    "الهزج",
    "الرجز",
    
    # Adding the rest 2 meters, Note: Not in Metrec Dataset
    "المقتضب",
    "الخبب",
]

class Page2(Screen):
    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        dropdown = DropDown()

        # Arabic options for the dropdown
        options = BUHOOR

        # Add options to dropdown
        for option in options:
            btn = Button(text=reshape_text(option), size_hint_y=None, height=44,font_name="Amiri-Regular.ttf")
            btn.bind(on_release=lambda btn: self.select_option(btn.text, dropdown))
            dropdown.add_widget(btn)


        main_button = Button(text=reshape_text('اختر بحرا'), size_hint=(1, 0.1), font_name="Amiri-Regular.ttf")
        main_button.bind(on_release=dropdown.open)
        layout.add_widget(main_button)
        layout.add_widget(dropdown)

        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_option(self, option, dropdown):
        # Update main button text to show selected option
        dropdown.parent.children[1].text = reshape_text(option)
        dropdown.dismiss()
