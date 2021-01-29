#import create_products
import pickle

import pglet
from pglet import Page, Text, Button, Stack, Textbox, Dropdown
from pglet.dropdown import Option

class Product():
    def __init__(self, name, grams_in_cup):
        self.name = name
        self.density = float(grams_in_cup)/240


products = []

def add_product(e):
    '''
    Reads in a new product and stores it
    '''
    print('Create new product')
    #create a new instance
    global products
    new_product = Product(name=page.get_value('product_name'), grams_in_cup=page.get_value('grams_in_a_cup'))
    
    #add the data attributes
    #new_product.name = page.get_value('product_name')
    #new_product.density = float(page.get_value('grams_in_a_cup'))/240
    products.append(new_product)
    print(products)
    save_products('C:/Projects/Python/pglet_samples/products.txt')
    
    #update list of options in product dropdown
    page.clean('product')
    #product_options = create_options(products)
    #page.add(product_options, to='product')

def save_products(file_name):
    '''
    saves the products as a pickled file
    '''
    print('Save contacts in ' +  file_name)
    with open(file_name, 'wb') as out_file:
        pickle.dump(products, out_file)

def load_products(file_name):
    '''
    Loads products from the pickled file
    '''
    global products
    print('Load products from ' + file_name)
    with open(file_name, 'rb') as input_file:
        products = pickle.load(input_file)

def convert(e):
    
    #number of a product in a list of product names
    product_index = names.index(page.get_value('product'))
    try:
        from_value = float(page.get_value('from_value'))
        #if we get here the number is int
        page.send('set from_value errorMessage=""')
    
        from_unit_index = units.index(page.get_value('from_unit'))
        to_unit_index = units.index(page.get_value('to_unit'))

        #set up unit conversion values depending on a product density
        density = densities[product_index]
        
        unit_in_ml = [15, 5, 29.5, 1/float(density), 1, 240]
        page.set_value('to_value', from_value*unit_in_ml[from_unit_index]/unit_in_ml[to_unit_index])
        
        #printing product index to check
        #page.add(Text(value=product_index))
        
    except ValueError:
        page.send('set from_value errorMessage="Please enter a float number"') 


#save_products('C:/Projects/Python/pglet_samples/products.txt')

names = []
densities = []
try:
    load_products('C:/Projects/Python/pglet_samples/products.txt')
    for product in products:
        names.append(product.name)
        densities.append(product.density)
except:
    print('There are no products')

#print(names)

units = ['Tbsp', 'tsp', 'oz', 'g', 'ml', 'cup']

page = pglet.page("index")
page.update(Page(title="Weight Converter"))
page.clean()

page.add(
        Stack(horizontal = True, controls=[
            Text(value='Product name: '),
            Textbox(id='product_name', align = 'right'),
            Text(value='Grams in a cup: '),
            Textbox(id='grams_in_a_cup', align = 'right'),
            Button(text='Add', onclick=add_product, data='Add')
            ])
        )

page.add(Dropdown(id='product', label = 'Select product:', options = names, value = 'Water'))

page.add(
        Stack(horizontal = True, controls=[
            Text(value='Original quantity: '),
            Textbox(id='from_value', value = '0', align = 'right'),
            Dropdown(id='from_unit', options = units, value = 'g'),
            Button(text='Go', onclick=convert, data='Go')
            ]),
        Stack(horizontal = True, controls=[
            Text(value='Converted quantity: '),
            Textbox(id='to_value', value = '0', align = 'right'),
            Dropdown(id='to_unit', options = units, value = 'g'),
            ]),
        )

page.add(Text(value = names + densities))

page.wait_close()
