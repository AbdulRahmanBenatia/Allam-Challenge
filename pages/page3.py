from components.arabic_text_input import ArabicTextInput
from utils import reshape_text
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from ibm_API import get_response

class Page3(Screen):
    def __init__(self, **kwargs):
        super(Page3, self).__init__(**kwargs)
        layout = FloatLayout()  # Use FloatLayout to place the back button freely

        # Title label
        self.label = Label(
            text=reshape_text("أدخل البيت المراد شرحه"),
            font_size='24sp',
            halign='center',
            valign='middle',
            font_name="Amiri-Regular.ttf",
            size_hint=(0.8, None),  # Set width, height will be auto
            pos_hint={'center_x': 0.5, 'top': 0.9}  # Centered at the top
        )
        layout.add_widget(self.label)

        # Create a TextInput for Arabic text (reverted changes)
        self.text_input = ArabicTextInput(
            hint_text=reshape_text('أدخل البيت هنا'),
            font_size='24sp',
            size_hint=(1, 0.2),  # Reverted back to original size
            font_name="Amiri-Regular.ttf",
            pos_hint={'center_x': 0.5, 'top': 0.75}  # Centered just below the label
        )
        layout.add_widget(self.text_input)

        # Create a Label to display reshaped text
        self.output_label = Label(
            text='',
            font_size='24sp',
            size_hint=(1, 0.2),
            font_name="Amiri-Regular.ttf",
            pos_hint={'top': 0.5}  # Position just below the text input
        )
        layout.add_widget(self.output_label)

        # Bind the on_text event to update the output label and input text
        self.text_input.bind(text=self.update_output)

        # Submit button (تأكيد)
        submit_button = Button(
            text=reshape_text("تأكيد"),
            size_hint=(None, None),  # Set to None to manually control size
            size=(150, 50),  # Smaller size for the button
            font_name="Amiri-Regular.ttf",
            pos_hint={'center_x': 0.5, 'top': 0.4}  # Centered just below the output label
        )
        submit_button.bind(on_press=self.on_submit)
        layout.add_widget(submit_button)

        # Circular back button setup
        back_button = Button(
            size_hint=(None, None),
            size=(50, 50),
            background_normal='/home/ozeiri/repos/Allam-Challenge/icons/back.png',  # Use icon as background
            background_down='/home/ozeiri/repos/Allam-Challenge/icons/back.png',  # Use same icon when pressed
            pos_hint={'x': 0.02, 'top': 0.98}  # Position top left
        )

        # Bind button press to navigate back
        back_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)

        # Add layout to the screen
        self.add_widget(layout)

        self.input_list = []
        self.last_value = ''
        self.full_verse = ''

    def update_output(self, instance, value):
        print("Val : ", value)
        print("Reshaped: ", reshape_text(value))

        if self.text_input.BACK:
            self.input_list = self.input_list[:-1]
            value = value[:-1]

        else:
            self.input_list.append(value[-1])
            # Unbind to prevent recursion error when updating text
            instance.unbind(text=self.update_output)
            till_now = reshape_text(''.join(self.input_list))
            if self.input_list[-1] != ' ':
                instance.text = till_now
        # Rebind after updating the text
        instance.bind(text=self.update_output)
        self.full_verse = value

    def on_submit(self, interface):
        print(self.full_verse)
        prompt = f"""
        اشرح هذا البيت شرحا موجزا جدا: 
        {self.full_verse}
        """
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        self.label.text = reshape_text(response)
