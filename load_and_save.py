import os.path

#items=['Zachary','Inna','Liza','Feodor','Alena','Isaak','Alena','Fiodar']

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
    #loads the list from the file

    print('Load the list from:',file_path)
    input_file = open(file_path, 'r')
    for line in input_file:  
        line = line.strip()  
        print(line)
    input_file.close()



file_path='C:/Projects/Python/Test projects/test7.txt'
#save_list(file_path, items)
load_list(file_path)