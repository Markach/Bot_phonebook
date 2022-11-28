import csv
import os.path
import logger as lg

id = 0  
file_BD = ''
BD = []
 
def init_book(file ='phonebook.csv'):
    global id
    global BD
    global file_BD
    file_BD = file 
    BD.clear()
    if os.path.exists(file_BD):
        with open(file_BD, 'r', newline='') as fh:
            reader = csv.reader(fh)
            for row in reader:
                if(row[0] != 'ID'):
                    BD.append(row)
                    if(int(row[0]) > id):
                        id = int(row[0])
    else:
        open(file_BD, 'w', newline='').close()

def create_contact(surname='', name='', number='', comment=''):
    global id
    global BD
    global file_BD
    id += 1
    new_row = [str(id), surname.title(), name.title(), number, comment.lower()]
    BD.append(new_row)
    with open(file_BD, 'a', newline='') as fh:
        writer = csv.writer(fh, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)

def delete_contact(id=''):
    global BD
    global file_BD
    for row in BD:
        if (row[0] == id):
            BD.remove(row)
            break

    with open(file_BD, 'w', newline='') as fh:
        writer = csv.writer(fh, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in BD:
            writer.writerow(row)        

def extract_data(id='', name='', surname='',):
    global BD
    global file_BD
    result = []
    for row in BD:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result