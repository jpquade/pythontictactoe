import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        #container = gui.VBox(width=400, height=400)
        grid = gui.GridBox(width = 200, height = 200)
        
        self.lbl = gui.Label('Python Tic-Tac-Toe')
        self.bt = gui.Button('1',width = 200, height = 200)
        self.bt2 = gui.Button('2',width = 200, height = 200)
        
        self.bt3 = gui.Button('3',width = 200, height = 200)

        # setting the listener for the onclick event of the buttons
        self.bt.onclick.do(self.on_button_pressed, "Name")
        self.bt2.onclick.do(self.on_button_pressed, "Name", "Surname")

        # appending a widget to another
        #container.append(self.lbl)
        #container.append(self.bt)
        #container.append(self.bt2)
        grid.append(self.bt)
        grid.append(self.bt2)
        grid.append(self.bt3)

        # returning the root widget
        return grid

    # listener function
    def on_button_pressed(self, widget, name='', surname=''):
        self.lbl.set_text('Button pressed!')
        widget.set_text('Hello ' + name + ' ' + surname)

# starts the web server
start(MyApp)