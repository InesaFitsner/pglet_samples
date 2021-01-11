import pglet
from pglet import Page, Text, Dropdown, Button, Stack, Textbox

page = pglet.page("inesa-calc")
page.update(Page(title="Calculator"))
page.clean()

#initiation
operand1 = '0' #previous value
operator = '+'
start_new = True #will start new sequence in the 'result' textbox
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
    global operator
    global history_id
    global start_new

    
    if e.data in ('1','2','3','4','5','6','7','8','9','0','.'):
        #start a new sequence in the 'result' textbox
        if start_new == True:
            page.set_value('result', e.data)
            start_new = False
        
        #continue exising sequence in the 'result' textbox
        else:
            page.set_value('result', page.get_value('result') + e.data)

        page.append_value(history_id ,e.data)

    elif e.data == 'C':
        page.set_value('result', '0')
        operand1 = '0'
        operator = '+'
        start_new = True
        history_id = page.add(Text(value='History: ')).id

    elif e.data in ('+','-','*','/'):
        
        page.set_value('result', calculate(float(operand1), float(page.get_value('result')), operator)) 
        operand1 = page.get_value('result')
        operator = e.data
        start_new = True
        page.append_value(history_id ,'='+ operand1 + operator)    

    elif e.data == '=':

        page.set_value('result', calculate(float(operand1), float(page.get_value('result')), operator))
        operator = '+'
        operand1 = '0'
        start_new = True
        page.append_value(history_id ,' = ' + page.get_value('result'))
        history_id = page.add(Text(value='History: ')).id


    #page.add(Text(value=f'Operand1: {operand1}'))   
    #page.add(Text(value='Operand2: '+ page.get_value('result')))   
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

page.wait_close()