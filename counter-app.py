import pglet
from pglet import Page, Text, Button, Stack, Textbox

class CounterApp:

    def __init__(self, page):
            self.page = page
            self.main()

    def main(self):
        self.page.update(Page(title="Counter"))
        self.page.clean()

        def on_click(e):
            try:
                count = int(self.page.get_value('number'))
                #if we get here the number is int
                self.page.send('set number errorMessage=""')

                if e.data == '+':
                    self.page.set_value('number', count + 1)

                elif e.data =='-':
                    self.page.set_value('number', count - 1)

            except ValueError:
                self.page.send('set number errorMessage="Please enter a number"')  

        self.page.add(
            Stack(horizontal = True, controls=[
                Button(text='-', onclick=on_click, data='-'),
                Textbox(id='number', value = '0', align = 'right'),
                Button(text='+', onclick=on_click, data='+'),
            ])
        )

pglet.app("inesa-counter-app", target = CounterApp, web = True)