import pglet
from pglet import Page, Text, Button, Stack, Textbox, Dropdown

page = pglet.page("index")
page.update(Page(title="Weight Converter"))
page.clean()

def on_click(e):
    
    product_index = products.index(page.get_value('product'))
    from_value=int(page.get_value('from_value'))
    from_unit=page.get_value('from_unit')
    to_unit=page.get_value('to_unit')

    #set up conversion table depending on a product density
    density = densities[product_index]
    Tbsp = [1, 3, 0.5, 15*density, 15, 0.0625]
    tsp = [1/3, 1, 0.16, 5*density, 5, 0.0208333]

    page.set_value('to_value', from_value*Tbsp[unit_names.index(to_unit)])

products = ['Flour', 'Butter', 'Sugar', 'Water']
densities = [120/240, 227/240, 200/240, 240/240]
unit_names = ['Tbsp', 'tsp', 'oz', 'g', 'ml', 'cup']
x=1
Tbsp = [1, 3, 0.5, 15*x, 15, 0.0625]
tsp = [1/3, 1, 0.16, 5*x, 5, 0.0208333]



page.add(Dropdown(id='product', label = 'Select product:', options = products))

page.add(
        Stack(horizontal = True, controls=[
            Text(value='Original quantity: '),
            Textbox(id='from_value', value = '0', align = 'right'),
            Dropdown(id='from_unit', options = unit_names),
            Button(text='Go', onclick=on_click, data='Go')
            ]),
        Stack(horizontal = True, controls=[
            Text(value='Converted quantity: '),
            Textbox(id='to_value', value = '0', align = 'right'),
            Dropdown(id='to_unit', options = unit_names),
            ]),
        )
                
#page.add()

page.wait_close()