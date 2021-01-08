import pglet
from pglet import Page, Text, Button, Stack, Textbox

page = pglet.page("index")
page.update(Page(title="Greeter"))
page.clean()

def on_click(e):
   name = page.get_value('name')
   page.add(Text(value='Hello, '+ name))

page.add(
    Stack(controls=[
        Text(value='Please enter your name:'),
        Textbox(id='name')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='OK', onclick=on_click, data='OK'),
    ])
)

page.wait_close()