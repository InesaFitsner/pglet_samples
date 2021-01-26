#import load_and_save

import pglet
from pglet import Page, Text, Button, Stack, Textbox, Dropdown

page = pglet.page("index")
page.update(Page(title="Weight Converter"))
page.clean()
#global products

def on_click(e):
    
    product_index = products.index(page.get_value('product'))
    try:
        from_value = float(page.get_value('from_value'))
        #if we get here the number is int
        page.send('set from_value errorMessage=""')
    
        from_unit_index = units.index(page.get_value('from_unit'))
        to_unit_index = units.index(page.get_value('to_unit'))

        #set up unit conversion values depending on a product density
        density = densities[product_index]
        unit_in_ml = [15, 5, 29.5, 1/density, 1, 240]
        page.set_value('to_value', from_value*unit_in_ml[from_unit_index]/unit_in_ml[to_unit_index])
        
    except ValueError:
        page.send('set from_value errorMessage="Please enter a float number"') 

products = ['Flour', 'Butter', 'Sugar', 'Water', 'Honey', 'Icing sugar', 'Brown sugar']
#products = load_and_save.load_list
densities = [120/240, 227/240, 200/240, 240/240, 320/240, 125/240, 220/240]
units = ['Tbsp', 'tsp', 'oz', 'g', 'ml', 'cup']



page.add(Dropdown(id='product', label = 'Select product:', options = products, value = 'Water'))

page.add(
        Stack(horizontal = True, controls=[
            Text(value='Original quantity: '),
            Textbox(id='from_value', value = '0', align = 'right'),
            Dropdown(id='from_unit', options = units, value = 'g'),
            Button(text='Go', onclick=on_click, data='Go')
            ]),
        Stack(horizontal = True, controls=[
            Text(value='Converted quantity: '),
            Textbox(id='to_value', value = '0', align = 'right'),
            Dropdown(id='to_unit', options = units, value = 'g'),
            ]),
        )

page.wait_close()