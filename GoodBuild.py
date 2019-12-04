from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
import math

class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [70]
        self.spacing = 5

        self.mini_box1 = GridLayout(cols=2)
        self.text1 = Label(text="Leg(a) = ")
        self.input1 = TextInput(text="0",multiline=False)
        self.mini_box1.add_widget(self.text1)
        self.mini_box1.add_widget(self.input1)
        self.add_widget(self.mini_box1)

        self.mini_box2 = GridLayout(cols=2)
        self.text2 = Label(text="Leg(b) = ")
        self.input2 = TextInput(text="0", multiline=False)
        self.mini_box2.add_widget(self.text2)
        self.mini_box2.add_widget(self.input2)
        self.add_widget(self.mini_box2)

        self.mini_box3 = GridLayout(cols=2)
        self.text3 = Label(text="Hypothenuse(c) = ")
        self.input3 = TextInput(text="0", multiline=False)
        self.mini_box3.add_widget(self.text3)
        self.mini_box3.add_widget(self.input3)
        self.add_widget(self.mini_box3)

        self.mini_box4 = GridLayout(cols=2)
        self.text4 = Label(text="Angle(a) = ")
        self.input4 = TextInput(text="0", multiline=False)
        self.mini_box4.add_widget(self.text4)
        self.mini_box4.add_widget(self.input4)
        self.add_widget(self.mini_box4)

        self.mini_box5 = GridLayout(cols=2)
        self.text5 = Label(text="Angle(b) = ")
        self.input5 = TextInput(text="0", multiline=False)
        self.mini_box5.add_widget(self.text5)
        self.mini_box5.add_widget(self.input5)
        self.add_widget(self.mini_box5)

        self.mini_box6 = GridLayout(cols=2)
        self.but = Button(text="Расчёт", on_press=self.press)
        self.mini_box6.add_widget(self.but)
        self.but = Button(text="Сброс", on_press=self.null)
        self.mini_box6.add_widget(self.but)
        self.add_widget(self.mini_box6)


        self.info = Label(text=" ")
        self.add_widget(self.info)

        self.wimg = Image(source='image.png', size_hint = (1, 5))
        self.add_widget(self.wimg)

        self.info = Label(text=" ")
        self.add_widget(self.info)

        self.add_widget(Label(text="For Dima"))


    def press(self, inctance):
        leg_a = float(self.input1.text)
        leg_b = float(self.input2.text)
        hyp_c = float(self.input3.text)
        ang_a = float(self.input4.text)
        ang_b = float(self.input5.text)
        if leg_a > 0 and leg_b > 0:
            hyp_c = math.sqrt((leg_a*leg_a) + (leg_b*leg_b))
            ang_a = math.degrees(math.asin(leg_a/hyp_c))
            ang_b = math.degrees(math.asin(leg_b / hyp_c))
        elif leg_a>0 and hyp_c>0:
            leg_b = sqrt(hyp_c*hyp_c - leg_a*leg_a)
            ang_a = math.degrees(math.asin(leg_a / hyp_c))
            ang_b = math.degrees(math.asin(leg_b / hyp_c))
        elif leg_b>0 and hyp_c>0:
            leg_a = sqrt(hyp_c * hyp_c - leg_b * leg_b)
            ang_a = math.degrees(math.asin(leg_a / hyp_c))
            ang_b = math.degrees(math.asin(leg_b / hyp_c))
        elif ang_a > 0 and leg_a>0:
            hyp_c = leg_a / (math.sin(math.radians(ang_a)))
            leg_b = math.sqrt(hyp_c * hyp_c - leg_a * leg_a)
            ang_b = math.degrees(math.asin(leg_b / hyp_c))
        elif ang_b > 0 and leg_a>0:
            hyp_c = leg_a / (math.cos(math.radians(ang_b)))
            leg_b = math.sqrt(hyp_c * hyp_c - leg_a * leg_a)
            ang_a = 90-ang_b
        elif ang_a > 0 and leg_b>0:
            hyp_c = leg_b / (math.cos(math.radians(ang_a)))
            leg_a = sqrt(hyp_c * hyp_c - leg_b * leg_b)
            ang_b = 90-ang_a
        elif ang_b > 0 and leg_b>0:
            hyp_c = leg_b / (math.sin(math.radians(ang_b)))
            leg_a = math.sqrt(hyp_c * hyp_c - leg_b * leg_b)
            ang_a = 90 - ang_b
        elif hyp_c > 0 and ang_a > 0:
            leg_b = hyp_c * (math.cos(math.radians(ang_a)))
            leg_a = math.sqrt(hyp_c * hyp_c - leg_b * leg_b)
            ang_b = 90-ang_a
        elif hyp_c > 0 and ang_b > 0:
            leg_a = hyp_c * (math.cos(math.radians(ang_b)))
            leg_b = math.sqrt(hyp_c * hyp_c - leg_a * leg_a)
            ang_a = 90-ang_b


        self.input1.text = str(round(leg_a, 2))
        self.input2.text = str(round(leg_b, 2))
        self.input3.text = str(round(hyp_c, 2))
        self.input4.text = str(round(ang_a, 2))
        self.input5.text = str(round(ang_b, 2))



    def null(self, instance):
        self.input1.text = "0"
        self.input2.text = "0"
        self.input3.text = "0"
        self.input4.text = "0"
        self.input5.text = "0"


class TestApp(App):
    def build(self):
        return Test()
if __name__ == "__main__":
    TestApp().run()