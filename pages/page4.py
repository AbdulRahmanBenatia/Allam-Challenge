import json
from components.arabic_text_input import ArabicTextInput
from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import  Screen
from ibm_API import get_reponse
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


class Page4(Screen):
    def __init__(self, **kwargs):
        super(Page4, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        dropdown = DropDown()

        # Load the responses from the JSON file
        with open('buhur_responses_reshaped.json', 'r', encoding='utf-8') as json_file:
            self.buhur_responses = json.load(json_file)

        # Arabic options for the dropdown
        options = BUHOOR
        # Add options to dropdown
        for option in options:
            btn = Button(text=reshape_text(option), size_hint_y=None, height=44, font_name="Amiri-Regular.ttf")
            btn.bind(on_release=lambda btn: self.select_option(btn.text, dropdown))
            dropdown.add_widget(btn)

        self.main_button = Button(text=reshape_text('اختر بحرا'), size_hint=(1, 0.1), font_name="Amiri-Regular.ttf")
        self.main_button.bind(on_release=dropdown.open)
        layout.add_widget(self.main_button)
        layout.add_widget(dropdown)

        self.response_label = Label(text="", size_hint=(1, 0.6), font_name="Amiri-Regular.ttf")
        layout.add_widget(self.response_label)

        back_button = Button(text=reshape_text('رجوع'), size_hint=(1, 0.2), font_name="Amiri-Regular.ttf")
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_option(self, option, dropdown):
        # Update main button text to show selected option
        self.main_button.text = option
        dropdown.dismiss()

        # Fetch the corresponding response from the loaded JSON file
        option_key = option.strip()  # Strip any extra spaces or formatting if needed
        print(len(reshape_text(option_key)))
        print(len(list(self.buhur_responses.keys())[0]))
        print(option_key)
        print(list(self.buhur_responses.keys())[0])
        if option_key in self.buhur_responses:
            response = self.buhur_responses[option_key]
        else:
            response = "No explanation available."

        # Update the label with the response
        self.response_label.text = reshape_text(response)