from kivy.uix.textinput import TextInput

class ArabicTextInput(TextInput):
    def __init__(self, **kwargs):
        super(ArabicTextInput, self).__init__(**kwargs)
        self.BACK = False  # Variable to check if external action is triggered

    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'backspace':
            print("Backspace pressed!")
            # Add a letter (e.g., 'X') when backspace is pressed
            self.BACK = True
            
            # You can also control cursor positioning if needed, e.g.,
            # self.cursor = (self.cursor[0] + 1, self.cursor[1])
            # return "BACK"  # Return True to override default backspace behavior
        # Call the parent method to retain other key functionalities
        return super(ArabicTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)