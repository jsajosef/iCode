from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
import sqlite3 as sql
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_string('''
<ScreenOne>:
    ActionBar:
        pos_hint: {'top':1}
        background_color: [1, 1, 1,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                app_icon: 'prodcat.png'
                title: 'ProdCat'
                with_previous: False
                on_press: root.manager.current = 'screenone'
            ActionOverflow:
            ActionButton:
                important: True
                text: 'Add +'
                on_press: root.manager.current = 'screentwo'
            ActionGroup:
                text: 'More'
                ActionButton:
                    text: 'Open'
                ActionButton:
                    text: 'Settings'
                ActionButton:
                    text: 'Exit'
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 100, 0, 0]
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgb: 0.5, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
            Label:
                text: 'USE PRODCAT™'
                pos_hint: {'center_x':.5, 'center_y':.5}
                font_size: 32
                bold: True
                color: [1, 1, 1, 1]
                padding: [10, 0]
            Label:
                text: 'TO STORE YOUR PRODUCTS'
                pos_hint: {'center_x':.5, 'center_y':.5}
                font_size: 32
                bold: True
                color: [1, 1, 1, 1]
                padding: [10, 0]
            Label:
                text: 'THEIR PRICES AND QUANTITIES'
                pos_hint: {'center_x':.5, 'center_y':.5}
                font_size: 32
                bold: True
                color: [1, 1, 1, 1]
                padding: [10, 0]
        Button:
            text: 'Search for Product'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenfour'
        Button:
            text: 'Open Products List'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenfive'


<ScreenTwo>:
    pn: pn
    pp: pp
    pq: pq
    ActionBar:
        pos_hint: {'top':1}
        background_color: [1, 1, 1,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                app_icon: 'prodcat.png'
                title: 'ProdCat'
                with_previous: False
                on_press: root.manager.current = 'screenone'
            ActionOverflow:
            ActionButton:
                important: True
                text: 'Add +'
            ActionGroup:
                text: 'More'
                ActionButton:
                    text: 'Open'
                ActionButton:
                    text: 'Settings'
                ActionButton:
                    text: 'Exit'
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 100, 0, 0]
        GridLayout:
            cols: 2
            size_hint: (1, 1)
            pos_hint: {'center_x': .5, 'center_y': .5}
            canvas:
                Color:
                    rgb: 0.5, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
            Label:
                text: 'Product Name'
                size_hint: (.2, .1)
                color: [1, 1, 1, 1]
                bold: True
                
            TextInput:
                size_hint: (.5, .5)
                id: pn
                hint_text: 'Enter Product Name'
            Label:
                text: 'Product Price'
                size_hint: (.2, .1)
                color: [1, 1, 1, 1]
                bold: True
                
            TextInput:
                size_hint: (.5, .5)
                id: pp
                hint_text: 'Enter Product Price'
            Label:
                text: 'Quantity'
                size_hint: (.2, .1)
                color: [1, 1, 1, 1]
                bold: True
                
            TextInput:
                size_hint: (.5, .5)
                id: pq
                hint_text: 'Enter Product Quantity'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Save Product'
                padding: [35, 15]
                pos_hint: {'center_x': .5, 'center_y': .5}
                color: [1, 0, 0, 1]
                font_size: 40
                background_color: [1, 1, 1,1]
                on_press:
                    root.saved()
                    
            Button:
                text: 'Search for Product'
                padding: [35, 15]
                pos_hint: {'center_x': .5, 'center_y': .5}
                color: [1, 0, 0, 1]
                font_size: 40
                background_color: [1, 1, 1,1]
                on_press: root.manager.current = 'screenfour'
<ScreenThree>:
    ActionBar:
        pos_hint: {'top':1}
        background_color: [1, 1, 1,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                app_icon: 'prodcat.png'
                title: 'ProdCat'
                with_previous: False
                on_press: root.manager.current = 'screenone'
            ActionOverflow:
            ActionButton:
                important: True
                text: 'Add +'
                on_press: root.manager.current = 'screentwo'
            ActionGroup:
                text: 'More'
                ActionButton:
                    text: 'Open'
                ActionButton:
                    text: 'Settings'
                ActionButton:
                    text: 'Exit'
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 100, 0, 0]
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgb: 0.5, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
            
        Button:
            text: 'Search for Product'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenfour'
        Button:
            text: 'Open Products List'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenfive'
<ScreenFour>:
    ActionBar:
        pos_hint: {'top':1}
        background_color: [1, 1, 1,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                app_icon: 'prodcat.png'
                title: 'ProdCat'
                with_previous: False
                on_press: root.manager.current = 'screenone'
            ActionOverflow:
            ActionButton:
                important: True
                text: 'Add +'
                on_press: root.manager.current = 'screentwo'
            ActionGroup:
                text: 'More'
                ActionButton:
                    text: 'Open'
                ActionButton:
                    text: 'Settings'
                ActionButton:
                    text: 'Exit'
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 100, 0, 0]
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgb: 0.5, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
            BoxLayout:
                orientation: 'vertical'
                size_hint: (.7, .1)
                pos_hint: {'center_x':.5, 'center_y':.5}
                padding: [0, 30, 0, 0]
                
                TextInput:
                    hint_text: 'Enter Product Name'
                    size_hint: (1, .1)
                    pos_hint: {'center_x':.5, 'center_y':.5}
                Button:
                    text: 'Search'
                    size_hint: (.5, .1)
                    pos_hint: {'center_x':.5, 'center_y':.5}
                Carousel:
                    size_hint: (1, .8)
                    pos_hint: {'center_x':.5, 'center_y':.5}
                    
                    Image:
                        source: '1.png'
                    Image:
                        source: '2.png'
                    Image:
                        source: '3.png'
                    Image:
                        source: '4.png'
                    Image:
                        source: '5.png'
                     
        Button:
            text: 'Home'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenone'
        Button:
            text: 'Open Products List'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenfive'

<ScreenFive>:
    ActionBar:
        pos_hint: {'top':1}
        background_color: [1, 1, 1,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                app_icon: 'prodcat.png'
                title: 'ProdCat'
                with_previous: False
                on_press: root.manager.current = 'screenone'
            ActionOverflow:
            ActionButton:
                important: True
                text: 'Add +'
                on_press: root.manager.current = 'screentwo'
            ActionGroup:
                text: 'More'
                ActionButton:
                    text: 'Open'
                ActionButton:
                    text: 'Settings'
                ActionButton:
                    text: 'Exit'
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 100, 0, 0]
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgb: 0.5, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id: tx
        Button:
            text: 'Load Products'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.display()
        Button:
            text: 'Homepage'
            size_hint: (1, .1)
            pos_hint: {'top':1}
            on_press: root.manager.current = 'screenone'
            
''')
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pn = ObjectProperty(None)
    pp = ObjectProperty(None)
    pq = ObjectProperty(None)
    def saved(self):
        db = sql.connect('products.db')
        cur = db.cursor()
        cur.execute('insert into productlist("productname","productprice", "quantity") values("{}", "{}", "{}")'.format(self.pn.text, self.pp.text, self.pq.text))
        db.commit()
        db.close()
        self.pn.text = ''
        self.pp.text = ''
        self.pq.text = ''
class ScreenThree(Screen):
    pass
class ScreenFour(Screen):
    pass
class ScreenFive(Screen):
    #tx = ObjectProperty(None)
    def display(self):
        db = sql.connect('products.db')
        cur = db.cursor()
        results = cur.execute("SELECT * FROM productlist").fetchall()
        self.ids.tx.text = ''
        for i in results:
            self.ids.tx.text += str(i) + '\n'
Sm = ScreenManager()
Sm.add_widget(ScreenOne(name='screenone'))
Sm.add_widget(ScreenTwo(name='screentwo'))
Sm.add_widget(ScreenThree(name='screenthree'))
Sm.add_widget(ScreenFour(name='screenfour'))
Sm.add_widget(ScreenFive(name='screenfive'))
Sm.current = 'screenone'

class ScreenApp(App):
    def build(self):
        return Sm

ScreenApp().run()