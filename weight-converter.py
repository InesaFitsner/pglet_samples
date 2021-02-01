#import create_products
import pickle

import pglet
from pglet import Page, Text, Button, Stack, Textbox, Dropdown
from pglet.dropdown import Option

class Product():
    def __init__(self, name, density):
        self.name = name
        self.density = density

def add_product(e):
    '''
    Reads in a new product and stores it
    '''
    #check if product exists
    if find_product(page.get_value('product_name'))!=None:
        page.set_value('product_prompt', 'Product with this name already exists')
    else:
        #create a new instance
        global products
        new_product = Product(name=page.get_value('product_name'), density=float(page.get_value('grams_in_a_cup'))/240)
    
        products.append(new_product)
        names.append(Option(new_product.name))
        page.set_value('product_prompt', new_product.name + ' ' + str(new_product.density))
    
        #update list of products in pickled file
        save_products('C:/Projects/Python/pglet_samples/products.txt')
    
        #update list of options in product dropdown
        page.clean('product')
        page.add(names, to='product')

def edit_product(e):
    print('Edit')

def delete_product(e):
    product = find_product(page.get_value('product_name'))
    #check if product exists
    if product==None:
        page.set_value('product_prompt', 'Product with this name does not exist')
    else:
        del(product)
        #update list of products in pickled file
        save_products('C:/Projects/Python/pglet_samples/products.txt')
        load_products('C:/Projects/Python/pglet_samples/products.txt')
    
        #update list of options in product dropdown
        page.clean('product')
        page.add(names, to='product')

def find_product(product_name):
    for product in products:
        if product_name == product.name:
            return product
    return None

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
    try:
        with open(file_name, 'rb') as input_file:
            products = pickle.load(input_file)
    except:
        products = []
        print('There is no file')

    global names
    names = []
    
    for product in products:
            names.append(Option(product.name))

def convert(e):
    product = find_product(page.get_value('product'))
    
    try:
        from_value = float(page.get_value('from_value'))
        #if we get here the number is float
        page.send('set from_value errorMessage=""')
    
        from_unit_index = units.index(page.get_value('from_unit'))
        to_unit_index = units.index(page.get_value('to_unit'))

        #set up unit conversion values depending on a product density
        
        unit_in_ml = [15, 5, 29.5, 1/product.density, 1, 240]
        page.set_value('to_value', from_value*unit_in_ml[from_unit_index]/unit_in_ml[to_unit_index])
        
    except ValueError:
        page.send('set from_value errorMessage="Please enter a float number"') 
    


load_products('C:/Projects/Python/pglet_samples/products.txt')

units = ['Tbsp', 'tsp', 'oz', 'g', 'ml', 'cup']

page = pglet.page("index")
page.update(Page(title="Weight Converter"))
page.clean()

page.add(
        Stack(controls=[
            Stack(horizontal = True, controls=[
                Text(value='Product name: '),
                Textbox(id='product_name', align = 'right'),
                Text(value='Grams in a cup: '),
                Textbox(id='grams_in_a_cup', align = 'right'),
                Button(text='Add', onclick=add_product, data='Add'),
                Button(text='Edit', onclick=edit_product, data='Edit'),
                Button(text='Delete', onclick=delete_product, data='Delete')
                ]),
            Text(id='product_prompt', value='Product prompt')
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

page.wait_close()
