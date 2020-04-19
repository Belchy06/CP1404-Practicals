"""
CP1404/CP5632 Practical
Kivy GUI program to create dynamic labels
William Belcher, Engineering @ JCU
Started 19/04/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'William Belcher'

from kivy.uix.button import Button

LABEL_LIST = ["Bill", "Jeff", "Elon", "Gina"]


class DynamicLabels(App):
    """ DynamicLabels is a Kivy App for creating dynamic labels """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 600)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_widgets.kv')
        for name in LABEL_LIST:
            temp_button = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_button)
            temp_button.bind(on_release=self.press_entry)
        return self.root

    def press_entry(self, on_release):
        print(on_release.text)


DynamicLabels().run()
