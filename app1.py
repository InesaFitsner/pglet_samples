import pglet
from pglet import Page, Text, Dropdown, Button, Stack, Textbox

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()

#initiation
operand1 = '0'
operand2 = '0'
operator = None
history_id = None

def format_number(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

def calculate(x,y,action):
    if action == '+':
        return format_number(x + y)
    elif action == '-':
        return format_number(x - y)
    elif action == '*':
        return format_number(x*y)
    elif action == '/':
        return format_number(x/y)


def on_click(e):
    
    global operand1
    global operand2
    global operator
    global history_id

    
    if e.data in ('1','2','3','4','5','6','7','8','9','0','.'):
        if operator == None:
            page.set_value('result', format_number(float(operand1 + e.data)))
            operand1 = page.get_value('result')     
        else:
            page.set_value('result', format_number(float(operand2 + e.data)))
            operand2 = page.get_value('result')         
        page.append_value(history_id ,e.data)

    elif e.data == 'C':
        page.set_value('result', '0')
        operand1 = '0'
        operand2 = '0'
        operator = None
        history_id = page.add(Text(value='History: ')).id

    elif e.data in ('+','-','*','/'):
        if operator == None:
            operator = e.data
            operand1 = page.get_value('result')
            page.append_value(history_id , operator)
        else:
            page.set_value('result', calculate(float(operand1), float(operand2), operator)) 
            operand1 = page.get_value('result')
            operand2 = '0'
            operator = e.data
            page.append_value(history_id ,'='+ operand1 + operator)    

    elif e.data == '=':

        page.set_value('result', calculate(float(operand1), float(operand2), operator))   
        operator = None
        operand1 = '0'
        operand2 = '0'
        page.append_value(history_id ,' = ' + page.get_value('result'))
        history_id = page.add(Text(value='History: ')).id


    #page.add(Text(value=f'Operand1: {operand1}'))   
    #page.add(Text(value=f'Operand2: {operand2}'))   
    #page.add(Text(value=f'Operator: {operator}'))   


history = Text(value='History: ')

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
        history
    ]))

history_id = history.id

#page.add(Text(value=f'Operand1: {operand1}'))
#page.add(Text(value=f'Operand1: {operand2}'))
#page.add(Text(value=f'Operator: {operator}'))
page.wait_close()