import pglet

from pglet import Page, Icon, Text, Stack, SearchBox

class IconBrowserApp:

    def __init__(self, page):
        self.page = page
        self.main()

    def main(self):
        global icon_names
        self.page.update(Page(title="Icon browser"))
        self.page.clean()
        
        def search_icons(search_name):
            found_icon_names = []
            if search_name==None:
                found_icon_names = icon_names
            else:
                for icon_name in icon_names:
                    if search_name.lower() in icon_name.lower():
                        found_icon_names.append(icon_name)
            return found_icon_names

        def searchbox_changed(e):
            search_name = self.page.get_value('searchbox')
            stack_controls = get_stack_controls(search_name)
            self.page.replace(stack_controls, to=result_stack)
            #print('Seachbox changed to ' + search_name)

        def enter_clicked(e):
            search_name = self.page.get_value('searchbox')
            stack_controls = get_stack_controls(search_name)
            self.page.replace(stack_controls, to=result_stack)
            #print('Seachbox changed to ' + search_name)
            
        #add stack controls each with Icon and Text
        def get_stack_controls(search_name):
            stack_controls = []
            found_icon_names = search_icons(search_name)
            for icon_name in found_icon_names:
                s = Stack(controls=[
                    Icon(name = icon_name),
                    Text(value = icon_name)
                ])
                stack_controls.append(s)
            return stack_controls
        
        stack_controls = get_stack_controls(None)
        
        result_stack = Stack(controls=stack_controls)
        self.page.add(SearchBox(id='searchbox', onchange=searchbox_changed, onsearch=enter_clicked, on_change=True), result_stack)

        self.page.wait_close()

# read list of icon names from file
file_path = 'C:/Projects/Python/pglet_samples/fluent-icons-clean.txt'
input_file = open(file_path, 'r')   
icon_names = []
for line in input_file:
    line=line.strip()
    icon_names.append(line)
input_file.close()

pglet.app("icon-browser-app", target = IconBrowserApp)