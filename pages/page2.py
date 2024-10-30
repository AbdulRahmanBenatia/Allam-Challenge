from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from utils import reshape_text

BUHOOR = [
    "السريع", "الكامل", "المتقارب", "المتدارك", "المنسرح", "المديد",
    "المجتث", "الرمل", "البسيط", "الخفيف", "الطويل", "الوافر",
    "الهزج", "الرجز", "المقتضب", "الخبب",
]

class Page2(Screen):
    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        main_layout = FloatLayout()
        font_path = "Amiri-Regular.ttf"  # Arabic font path

        # Back button with custom icon
        back_button = Button(
            size_hint=(None, None),
            size=(50, 50),
            background_normal='/home/ozeiri/repos/Allam-Challenge/icons/back.png',  # Use custom icon
            background_down='/home/ozeiri/repos/Allam-Challenge/icons/back.png',    # Same for pressed state
            pos_hint={'x': 0.02, 'top': 0.98}  # Position top left
        )
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        main_layout.add_widget(back_button)

        # Title label for displaying selected option with animation
        self.output_label = Label(
            text='',
            font_size='28sp',
            opacity=1,
            font_name=font_path,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        main_layout.add_widget(self.output_label)

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
            pos_hint={'center_x': 0.5, 'y': 0.05},
            font_name=font_path
        )
        self.main_button.bind(on_release=dropdown.open)
        main_layout.add_widget(self.main_button)

        self.add_widget(main_layout)

    def select_option(self, option, dropdown):
        # Update main button text and reset output label for animation
        self.main_button.text = option
        dropdown.dismiss()

        # Start text animation for output_label
        self.animate_text(option)

    def animate_text(self, full_text):
        self.output_label.text = ''  # Start with an empty label
        self.index = 0

        def update_text(dt):
            if self.index < len(full_text):
                self.output_label.text += full_text[self.index]
                self.index += 1
            else:
                return False  # Stop the scheduled event once text is complete

        # Schedule the text update every 0.1 seconds
        Clock.schedule_interval(update_text, 0.1)
