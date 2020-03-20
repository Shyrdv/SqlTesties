import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.sql import select

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name: ", name, "Last Name: ", last, "Email: ", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

engine = create_engine('mysql+mysqlconnector://daviid:Ubuntob0I!@172.104.148.212/Tfw')

connection = engine.raw_connection()

mycursor = connection.cursor()

cur = engine.connect()
res = cur.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", ("testies1", "testies1", True))
cur.close()

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()