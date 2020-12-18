import pglet
from pglet import Page, Text, Dropdown, Button, Stack, Textbox

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()

#initiation
operand1 = '0'
operand2 = '0'
previous_button = None
operator = None

def format_number(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

def calculate(x,y,action):
    if action == '+':
        return x + y
    elif action == '-':
        return x - y
    elif action == '*':
        return x*y
    elif action == '/':
        return format_number(x/y)


def on_click(e):
    #selected_value = page.get_value('list2')
    
    #page.add(Text(value=f'Selected value: {e.data}!'))
    
    global operand1
    global operand2
    global previous_button
    global operator
    
    #operand1 = page.get_value('result')

    
    if e.data in ('1','2','3','4','5','6','7','8','9','0'):
        if operator == None:
            if operand1 == '0':
                page.set_value('result', e.data)
                operand1 = e.data    
            else:
                page.set_value('result', operand1 + e.data)
                operand1 = operand1 + e.data
        else:
            if operand2 == '0':
                page.set_value('result', e.data)
                operand2 = e.data    
            else:
                page.set_value('result', operand2 + e.data)
                operand2 = operand2 + e.data


    elif e.data == 'C':
        page.set_value('result', '0')
        operand1 = '0'
        operand2 = '0'
        operator = None

    elif e.data in ('+','-','*','/'):
        if operator == None:
            operator = e.data
            operand1 = page.get_value('result')
            page.append_value('history',operand1)
        else:
            page.set_value('result', calculate(int(operand1), int(operand2), operator)) 
            operand1 = page.get_value('result')
            operand2 = '0'
            operator = e.data    

    elif e.data == '=':

        page.set_value('result', calculate(int(operand1), int(operand2), operator))   
        operator == None
        operand1 = page.get_value('result')
        operand2 = '0'


    #elif e.data in ('+','-','*','/'):
    #page.add(Text(value=f'Operand1: {operand1}'))
    #page.add(Text(value=f'Previous button: {previous_button}'))    
    #page.add(Text(value=f'Operand2: {operand2}'))   
    #page.add(Text(value=f'Operator: {operator}'))   
    
    previous_button = e.data

    

#page.add(Text(value='Hello, world!'))
#products = [('1','Flour'),('2','Sugar')]
#dd=Dropdown(id="list2", label="Select your product:", options=products)
#page.add(dd)


page.add(
    Stack(horizontal=True,controls=[
        Textbox(id='result', value='0')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='7', onclick=on_click, data='7'),
        Button(text='8', onclick=on_click, data='8'),
        Button(text='9', onclick=on_click, data='9'),
        Button(text='/', onclick=on_click, data='/')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='4', onclick=on_click, data='4'),
        Button(text='5', onclick=on_click, data='5'),
        Button(text='6', onclick=on_click, data='6'),
        Button(text='*', onclick=on_click, data='*')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='1', onclick=on_click, data='1'),
        Button(text='2', onclick=on_click, data='2'),
        Button(text='3', onclick=on_click, data='3'),
        Button(text='-', onclick=on_click, data='-')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='0', onclick=on_click, data='0'),
        Button(text='.', onclick=on_click, data='.'),
        Button(text='=', onclick=on_click, data='='),
        Button(text='+', onclick=on_click, data='+')
    ]),
    Stack(horizontal=True,controls=[
        Button(text='C', onclick=on_click, data='C')
    ]),
    Stack(horizontal=True,controls=[
        Text(id='history', value='History: ')
    ]))

#operand1 = '0'
#operand2 = None
#previous_button = None
#page.add(Text(value=f'Operand1: {operand1}'))
#page.add(Text(value=f'Operand1: {operand2}'))
#page.add(Text(value=f'Operator: {operator}'))
#page.add(Text(value=f'Previous button: {previous_button}'))
page.wait_close()