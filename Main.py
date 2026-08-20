from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import mysql.connector
import random
import os

Builder.load_file("niran.kv")


class Intro(Screen):
    pass


class Modes(Screen):
    pass


class Recipies(Screen):
    pass


class Create(Screen):
    pass


class final_screen(Screen):
    pass


class Pulao(Screen):
    def on_enter(self):
        self.layout = Builder.load_string(a)
        self.add_widget(self.layout)

    def back(self):
        self.root.current = 'ChefAdil3'


class MyApp(App):
    global_restaurant_list = []
    global_price_list = []
    global_cuisine_list = []
    global_multiple_cond_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = False

    def back(self):
        self.root.current = 'ChefAdil3'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Intro(name="ChefAdil1"))
        sm.add_widget(Modes(name="ChefAdil2"))
        sm.add_widget(Recipies(name="ChefAdil3"))
        sm.add_widget(Create(name="Creators"))
        sm.add_widget(final_screen(name="ChefAdil4"))
        sm.add_widget(Pulao(name="Pulao"))
        return sm

    def start_connection(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                database="chefadil1",
                # Never commit real credentials. Load from an environment
                # variable instead, e.g. os.environ["DB_PASSWORD"]
                password=os.environ.get("DB_PASSWORD", "")
            )
            self.cursor = self.db.cursor()
            print("connected")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def find_res(self, cuisine_res, price_range, ambience):
        conditions = []
        values = []

        if cuisine_res and cuisine_res != "None":
            conditions.append("Cuisine = %s")
            values.append(cuisine_res)

        if price_range and price_range != "None":
            conditions.append("Price = %s")
            values.append(price_range)

        if ambience and ambience != "None":
            conditions.append("AmbienceDescription = %s")
            values.append(ambience)

        query = "SELECT * FROM Restaurants"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(query, values)
        results = self.cursor.fetchall()

        if not results:
            print("No exact matches found.")
            like_conditions = []
            like_values = []
            for condition, value in zip(conditions, values):
                like_conditions.append(condition.replace("=", "LIKE"))
                like_values.append(f"%{value}%")

            like_query = "SELECT * FROM Restaurants"
            if like_conditions:
                like_query += " WHERE " + " AND ".join(like_conditions)

            self.cursor.execute(like_query, like_values)
            results = self.cursor.fetchall()

        self.global_multiple_cond_list = []
        for i in results:
            restaurant = {
                "RestaurantName": i[0],
                "AmbienceDescription": i[1],
                "SpecialtyCuisine": i[2],
                "Price": i[3],
                "Delivery": i[4],
                "Location": i[5],
                "Rating": str(i[6]),
                "VegOptions": i[7],
                "Reservations": i[8],
                "GlutenFree": i[9],
                "DriveThru": i[10],
                "KidsMenu": i[11],
                "PetFriendly": i[12],
                "ProvidesOffer": i[13]
            }
            self.global_multiple_cond_list.append(restaurant)
        self.update_final_screen()

    def update_final_screen(self):
        final_screen = self.root.get_screen('ChefAdil4')
        final_screen.clear_widgets()

        background = Image(source='testing123.jpg', allow_stretch=True, keep_ratio=False)
        final_screen.add_widget(background)

        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        self.content_layout = BoxLayout(orientation='vertical', padding=(40, 20, 20, 20), spacing=10)
        self.content_layout.size_hint = (None, None)
        self.content_layout.width = final_screen.width * 0.8
        self.content_layout.height = self.content_layout.width * 9 / 16

        if self.global_multiple_cond_list:
            restaurant = random.choice(self.global_multiple_cond_list)
            self.global_multiple_cond_list.remove(restaurant)
            restaurant_name = Label(text=f"Restaurant Name: {restaurant['RestaurantName']}", font_size='30sp',
                                     halign='left', valign='middle')
            restaurant_name.bind(size=restaurant_name.setter('text_size'))
            specialty_cuisine = Label(text=f"Specialty Cuisine: {restaurant['SpecialtyCuisine']}", font_size='30sp',
                                       halign='left', valign='middle')
            specialty_cuisine.bind(size=specialty_cuisine.setter('text_size'))
            rating = Label(text=f"Rating: {restaurant['Rating']}", font_size='30sp', halign='left', valign='middle')
            rating.bind(size=rating.setter('text_size'))
            location = Label(text=f"Location: {restaurant['Location']}", font_size='30sp', halign='left', valign='middle')
            location.bind(size=location.setter('text_size'))

            self.content_layout.add_widget(restaurant_name)
            self.content_layout.add_widget(specialty_cuisine)
            self.content_layout.add_widget(rating)
            self.content_layout.add_widget(location)
            self.c = True
        elif self.c:
            no_match = Label(text="Out of sugestions", font_size='30sp', halign='left', valign='middle')
            no_match.bind(size=no_match.setter('text_size'))
            self.content_layout.add_widget(no_match)
        else:
            no_match = Label(text="No matches found", font_size='30sp', halign='left', valign='middle')
            no_match.bind(size=no_match.setter('text_size'))
            self.content_layout.add_widget(no_match)

        anchor_layout.add_widget(self.content_layout)

        go_back_button = Button(text='Go Back', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.2})
        go_back_button.bind(on_press=self.Back)

        do_nothing_button = Button(text='Next', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.8})
        do_nothing_button.bind(on_press=self.Next)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_layout.add_widget(go_back_button)
        button_layout.add_widget(do_nothing_button)

        final_screen.add_widget(anchor_layout)
        final_screen.add_widget(button_layout)

    def _update_rect(self, *args):
        self.rect.pos = self.content_layout.pos
        self.rect.size = self.content_layout.size

    def Back(self, instance):
        self.root.current = 'ChefAdil2'
        self.c = False

    def Next(self, instance):
        self.update_final_screen()

    def update_final_screen1(self):
        final_screen1 = self.root.get_screen('ChefAdil3')
        final_screen1.clear_widgets()

        background = Image(source='testing123.jpg', allow_stretch=True, keep_ratio=False)
        final_screen1.add_widget(background)

        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        self.content_layout = BoxLayout(orientation='vertical', padding=(40, 20, 20, 20), spacing=10)
        self.content_layout.size_hint = (None, None)
        self.content_layout.width = final_screen1.width * 0.8
        self.content_layout.height = self.content_layout.width * 9 / 16

        with self.content_layout.canvas.before:
            Color(0.9, 0.9, 0.9, 0.5)
            self.rect = Rectangle(size=self.content_layout.size, pos=self.content_layout.pos)

        self.content_layout.bind(size=self._update_rect, pos=self._update_rect)

        if self.global_multiple_cond_list:
            recipes = random.choice(self.global_multiple_cond_list)
            print(recipes)
            self.global_multiple_cond_list.remove(recipes)
            global a
            a = recipes['Code']
            Recipe_name = Label(text=f"Dish Name: {recipes['NAME']}", font_size='30sp',
                                 halign='left', valign='middle')
            Recipe_name.bind(size=Recipe_name.setter('text_size'))
            Specialty_cuisine = Label(text=f"Type Of Cuisine: {recipes['TYPE_OF_CUISINE']}", font_size='30sp',
                                       halign='left', valign='middle')
            Specialty_cuisine.bind(size=Specialty_cuisine.setter('text_size'))
            Difficulty_level = Label(text=f"Difficulty level: {recipes['DIFFICULTY_LEVEL']}", font_size='30sp',
                                      halign='left', valign='middle')
            Difficulty_level.bind(size=Difficulty_level.setter('text_size'))
            NUTRITIONAL_VALUE = Label(text=f"Nutritional Value: {recipes['NUTRITIONAL_VALUE']}", font_size='30sp',
                                       halign='left', valign='middle')
            NUTRITIONAL_VALUE.bind(size=NUTRITIONAL_VALUE.setter('text_size'))

            self.content_layout.add_widget(Recipe_name)
            self.content_layout.add_widget(Specialty_cuisine)
            self.content_layout.add_widget(Difficulty_level)
            self.content_layout.add_widget(NUTRITIONAL_VALUE)
            self.c = True
        elif self.c:
            no_match = Label(text="Out of sugestions", font_size='30sp', halign='left', valign='middle')
            no_match.bind(size=no_match.setter('text_size'))
            self.content_layout.add_widget(no_match)
        else:
            no_match = Label(text="No matches found", font_size='30sp', halign='left', valign='middle')
            no_match.bind(size=no_match.setter('text_size'))
            self.content_layout.add_widget(no_match)

        anchor_layout.add_widget(self.content_layout)

        go_back_button = Button(text='Go Back', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.2})
        go_back_button.bind(on_press=self.Back1)

        go_next_button = Button(text='Next', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.8})
        go_next_button.bind(on_press=self.Next1)

        go_steps_button = Button(text='Steps', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.2})
        go_steps_button.bind(on_press=self.pulao)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_layout.add_widget(go_back_button)
        button_layout.add_widget(go_steps_button)
        button_layout.add_widget(go_next_button)

        final_screen1.add_widget(anchor_layout)
        final_screen1.add_widget(button_layout)

    def _update_rect1(self, *args):
        self.rect.pos = self.content_layout.pos
        self.rect.size = self.content_layout.size

    def Back1(self, instance):
        self.root.current = 'ChefAdil2'
        self.c = False

    def pulao(self, instance):
        self.root.current = 'Pulao'

    def Next1(self, instance):
        self.update_final_screen1()

    def find_cuis(self, cuisine_rec, Diff_lev, nutr_val):
        print(cuisine_rec, Diff_lev, nutr_val)
        cuis_conditions = []
        cuis_values = []

        if cuisine_rec and cuisine_rec != "None":
            cuis_conditions.append("TYPE_OF_CUISINE = %s")
            cuis_values.append(cuisine_rec)

        if Diff_lev and Diff_lev != "None":
            cuis_conditions.append("DIFFICULTY_LEVEL = %s")
            cuis_values.append(Diff_lev)

        if nutr_val and nutr_val != "None":
            cuis_conditions.append("NUTRITIONAL_VALUE = %s")
            cuis_values.append(nutr_val)

        query = "SELECT * FROM recipes"
        if cuis_conditions:
            query += " WHERE " + " AND ".join(cuis_conditions)

        self.cursor.execute(query, cuis_values)
        results1 = self.cursor.fetchall()

        if not results1:
            print("No exact matches found.")
            cuis_like_conditions = []
            cuis_like_values = []
            for condition, value in zip(cuis_conditions, cuis_values):
                cuis_like_conditions.append(condition.replace("=", "LIKE"))
                cuis_like_values.append(f"%{value}%")

            like_query = "SELECT * FROM recipes"
            if cuis_like_conditions:
                like_query += " WHERE " + " AND ".join(cuis_like_conditions)

            print("Executing like query:", like_query)
            print("With like values:", cuis_like_values)

            self.cursor.execute(like_query, cuis_like_values)
            results1 = self.cursor.fetchall()

        self.global_multiple_cond_list = []
        for i in results1:
            restaurant = {
                "NAME": i[1],
                "SPICINESS_LEVEL": i[2],
                "SWEETNESS_LEVEL": i[3],
                "SALTINESS_LEVEL": i[4],
                "TYPE_OF_CUISINE": i[5],
                "TEXTURE": i[6],
                "AROMACITY": str(i[7]),
                "NUTRITIONAL_VALUE": i[8],
                "PREP_TIME": i[9],
                "DIFFICULTY_LEVEL": i[10],
                "COURSE_TYPE": i[11],
                "SERVING_SIZE": i[12],
                "ALLERGENS": i[13],
                "Code": i[14]
            }
            self.global_multiple_cond_list.append(restaurant)
        self.update_final_screen1()

    def stop_app(self):
        if hasattr(self, 'db') and self.db.is_connected():
            self.db.close()
            print("Database connection closed.")
        App.get_running_app().stop()
        Window.close()


if __name__ == '__main__':
    MyApp().run()
