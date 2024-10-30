import json
from components.arabic_text_input import ArabicTextInput
from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from ibm_API import get_response
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView  # Import ScrollView
from kivy.clock import Clock

BUHOOR = [
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
    "المقتضب",
    "الخبب",
]

class Page4(Screen):
    def __init__(self, **kwargs):
        super(Page4, self).__init__(**kwargs)
        main_layout = FloatLayout()
        font_path = "Amiri-Regular.ttf"  # Arabic font path

        # Back button with custom icon
        back_button = Button(
            size_hint=(None, None),
            size=(50, 50),
            background_normal='/home/ozeiri/repos/Allam-Challenge/icons/back.png',
            background_down='/home/ozeiri/repos/Allam-Challenge/icons/back.png',
            pos_hint={'x': 0.02, 'top': 0.98}
        )
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        main_layout.add_widget(back_button)

        # Load the responses from the JSON file
        with open('buhur_responses_reshaped.json', 'r', encoding='utf-8') as json_file:
            self.buhur_responses = json.load(json_file)

        # Dropdown setup
        dropdown = DropDown()
        for option in BUHOOR:
            option_layout = BoxLayout(size_hint_y=None, height=50, padding=(10, 0))
            btn = Button(
                text=reshape_text(option),
                size_hint=(None, 1),
                width=150,
                font_name=font_path
            )
            btn.bind(on_release=lambda btn: self.select_option(btn.text, dropdown))
            option_layout.add_widget(btn)
            dropdown.add_widget(option_layout)

        # Main button to open dropdown at the bottom
        self.main_button = Button(
            text=reshape_text('اختر بحرا'),
            font_size='24sp',
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            font_name=font_path
        )
        self.main_button.bind(on_release=dropdown.open)
        main_layout.add_widget(self.main_button)

        # Create a ScrollView to hold the response label
        scroll_view = ScrollView(
            size_hint=(0.8, 0.6),  # Define height relative to the parent layout
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Response label with animation and constrained text
        self.response_label = Label(
            text="",
            font_size='24sp',
            size_hint_y=None,  # Allow height to adjust based on content
            halign='center',
            valign='top',
            font_name=font_path,
            text_size=(self.width * 0.75, None)  # Adjusted width for 4-5 words per line
        )
        self.response_label.bind(texture_size=self.response_label.setter('size'))  # Auto-size the label

        scroll_view.add_widget(self.response_label)  # Add label to ScrollView
        main_layout.add_widget(scroll_view)  # Add ScrollView to main layout

        self.add_widget(main_layout)

    def select_option(self, option, dropdown):
        # Update main button text and display the corresponding response
        self.main_button.text = option
        dropdown.dismiss()

        # Fetch the response from the loaded JSON file
        option_key = option.strip()
        if option_key in self.buhur_responses:
            response = self.buhur_responses[option_key]
        else:
            response = "No explanation available."

        # Start the text animation
        self.animate_text(reshape_text(response))

    def animate_text(self, full_text):
        self.response_label.text = ''  # Start with an empty label
        self.index = 0

        def update_text(dt):
            if self.index < len(full_text):
                self.response_label.text += full_text[self.index]
                self.index += 1
            else:
                return False  # Stop the scheduled event once text is complete

        # Schedule the text update every 0.1 seconds
        Clock.schedule_interval(update_text, 0.1)
