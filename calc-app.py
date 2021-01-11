import pglet
from pglet import Page, Text, Button, Stack, Textbox

class CalcApp:
    #initiation
    operand1 = '0' #previous value
    operator = '+'
    start_new = True #will start new sequence in the 'result' textbox
    history_id = None

    def __init__(self, page):
        self.page = page
        self.main()
    
    def main(self):
        self.page.update(Page(title="Calculator"))
        self.page.clean()

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
                return format_number(x * y)
            elif action == '/':
                return format_number(x / y)

        def on_click(e):
            
            if e.data in ('1','2','3','4','5','6','7','8','9','0','.'):
                #start a new sequence in the 'result' textbox
                if self.start_new == True:
                    self.page.set_value('result', e.data)
                    self.start_new = False
                
                #continue exising sequence in the 'result' textbox
                else:
                    self.page.set_value('result', self.page.get_value('result') + e.data)

                self.page.append_value(self.history_id ,e.data)

            elif e.data == 'C':
                self.page.set_value('result', '0')
                self.operand1 = '0'
                self.operator = '+'
                self.start_new = True
                self.history_id = self.page.add(Text(value='History: ')).id

            elif e.data in ('+','-','*','/'):
                
                self.page.set_value('result', calculate(float(self.operand1), float(self.page.get_value('result')), self.operator)) 
                self.operand1 = self.page.get_value('result')
                self.operator = e.data
                self.start_new = True
                self.page.append_value(self.history_id ,'='+ self.operand1 + self.operator)    

            elif e.data == '=':

                self.page.set_value('result', calculate(float(self.operand1), float(self.page.get_value('result')), self.operator))
                self.operator = '+'
                self.operand1 = '0'
                self.start_new = True
                self.page.append_value(self.history_id ,' = ' + self.page.get_value('result'))
                self.history_id = self.page.add(Text(value='History: ')).id


            #self.page.add(Text(value=f'self.operand1: {self.operand1}'))   
            #self.page.add(Text(value=f"Operand2: {self.page.get_value('result')}"))   
            #self.page.add(Text(value=f'self.operator: {self.operator}'))   


        history = Text(value='History: ')

        self.page.add(
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

        self.history_id = history.id

pglet.app("inesa-calc-app", target = CalcApp, web = True)