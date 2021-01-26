import os.path

#items = ['Flour', 'Butter', 'Sugar', 'Water', 'Honey']
#densities = [120/240, 227/240, 200/240, 240/240, 320/240]

def save_list(file_path, items):
    #Saves the list to the file

    print('Save the list in:',file_path)
    #check if the file exists
    #if os.path.isfile(file_path):
        #print('This file exists')
    
    #open the output file
    output_file=open(file_path,'w')
    
    #work through the sales values in the list
    for item in items:
        output_file.write(str(item)+'\n')

    #close output file
    output_file.close()

   

def load_list(file_path):
    #loads the list of names from the file

    print('Load the list from:',file_path)
    #items.clear
    items = []
    #open file for input
    input_file = open(file_path, 'r')
    i=0
    for line in input_file:  
        line = line.strip()  
        items.append(line)
        print(items[i])
        print[i]
        i=i+1

    input_file.close()
    return items

file_path='C:/Projects/Python/pglet_samples/products.txt'
#save_list(file_path, items)
items = load_list(file_path)
#i=0
#for line in items:
#    print(line)
#    print(i)
#    i=i+1