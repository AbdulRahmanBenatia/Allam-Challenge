from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from utils import reshape_text
from pages.page1 import Page1
from pages.page2 import Page2
from pages.page3 import Page3
from pages.page4 import Page4
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

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

class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        # self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.layout = FloatLayout()
        font_path = "Amiri-Regular.ttf"  

        background = Image(source='icons/Arabic_Letters.jpg', allow_stretch=True, keep_ratio=False, opacity = 0.1,
                           size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(background, index = 0)
        
        # # Title Label
        # self.title_label = Label(text='', font_size='32sp', size_hint=(1, 0.2), pos_hint={'center_x': 0.5 , 'center_y': 0.95},
        #                          halign='center', valign='middle', font_name=font_path)
        # self.title_label.bind(size=self.title_label.setter('text_size'))
        # self.layout.add_widget(self.title_label)

        # # Define buttons with reshaped text and initially set opacity to 0
        # self.buttons = [
        #     Button(text=reshape_text("تحديد البحر الشعري"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.8},),
        #     Button(text=reshape_text("إنشاء أبيات جديدة"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path, opacity=0,  pos_hint={'center_x': 0.5 , 'center_y': 0.55},),
        #     Button(text=reshape_text("شرح الأبيات"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.3},),
        #     Button(text=reshape_text("دراسة البحور"), font_size='24sp', size_hint=(1, 0.2), font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.05},),
        # ]
        
        # Title Label
        self.title_label = Label(text='', font_size='32sp', size_hint=(1, 0.15), 
                                pos_hint={'center_x': 0.5 , 'center_y': 0.92},
                                halign='center', valign='middle', font_name=font_path)
        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.layout.add_widget(self.title_label)

        # Define buttons with reshaped text and initially set opacity to 0
        self.buttons = [
            Button(text=reshape_text("تحديد البحر الشعري"), font_size='24sp', size_hint=(0.8, 0.15),
                font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.75}),
            Button(text=reshape_text("إنشاء أبيات جديدة"), font_size='24sp', size_hint=(0.8, 0.15),
                font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.55}),
            Button(text=reshape_text("شرح الأبيات"), font_size='24sp', size_hint=(0.8, 0.15),
                font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.35}),
            Button(text=reshape_text("دراسة البحور"), font_size='24sp', size_hint=(0.8, 0.15),
                font_name=font_path, opacity=0, pos_hint={'center_x': 0.5 , 'center_y': 0.15}),
        ]

        
        # Bind each button to its corresponding function
        self.buttons[0].bind(on_press=self.go_to_page1)
        self.buttons[1].bind(on_press=self.go_to_page2)
        self.buttons[2].bind(on_press=self.go_to_page3)
        self.buttons[3].bind(on_press=self.go_to_page4)

        # Add all buttons to the layout at once in their places
        for button in self.buttons:
            self.layout.add_widget(button)

        # Add the layout to the screen
        self.add_widget(self.layout)

        # Animate the title and then the buttons
        self.animate_text(reshape_text("علام الشعر"))  # Start the text animation
        Clock.schedule_once(self.animate_buttons, 1)  # Delay the button animation slightly
        


    def animate_text(self, full_text):
        self.title_label.text = ''  # Start with an empty label
        self.index = 0

        def update_text(dt):
            if self.index < len(full_text):
                self.title_label.text += full_text[self.index]
                self.index += 1
            else:
                return False  # Stop the scheduled event once text is complete

        # Schedule the text update every 0.1 seconds
        Clock.schedule_interval(update_text, 0.1)

    def animate_buttons(self, *args):
        # Gradually increase the opacity of each button
        for i, button in enumerate(self.buttons):
            Clock.schedule_once(lambda dt, btn=button: setattr(btn, 'opacity', 1), i * 0.5)

    def go_to_page1(self, instance):
        self.manager.current = 'page1'
    
    def go_to_page2(self, instance):
        self.manager.current = 'page2'
    
    def go_to_page3(self, instance):
        self.manager.current = 'page3'
    
    def go_to_page4(self, instance):
        self.manager.current = 'page4'


class ArabicApp(App):
    def build(self):
        Window.title = "Al Farahidi"

        sm = ScreenManager()
        sm.add_widget(MainPage(name='main'))
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        sm.add_widget(Page3(name='page3'))
        sm.add_widget(Page4(name='page4'))

        return sm

if __name__ == '__main__':
    ArabicApp().run()
