import pglet
from pglet import Page, Text, Button, Stack, Textbox, Dropdown

page = pglet.page("index")
page.update(Page(title="Weight Converter"))
page.clean()

def on_click(e):
    page.add(Text(value='number'))

products = ['Flour', 'Butter', 'Sugar']
density = [120/240, 227/240, 200/240]
units = ['g', 'ml', 'oz', 'Tbsp', 'tsp', 'cup']


page.add(Dropdown(id='product', label = 'Select product:', options = products))

page.add(
        Stack(horizontal = True, controls=[
            Text(value='Original quantity: '),
            Textbox(id='from_value', value = '0', align = 'right'),
            Dropdown(id='from_unit', options = units),
            Button(text='Go', onclick=on_click, data='Go')
            ]),
        Stack(horizontal = True, controls=[
            Text(value='Converted quantity: '),
            Textbox(id='to_value', value = '0', align = 'right'),
            Dropdown(id='to_unit', options = units),
            ]),
        )
                
#page.add()

page.wait_close()