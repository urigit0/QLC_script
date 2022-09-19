from tkinter import *
from tkinter import ttk

import random
root = Tk()
root.title('sequence script')
field = []

maxN_fixtures = 14
maxN_steps = 20
count = 1

curr_value = 0
curr_bg = 'black'
sequence_list = ["seq 1", "seq 2", "seq 3"]
curr_sequence = ''

# очистка всех шагов
def clear():
    for row in range(maxN_steps):
        for col in range(maxN_fixtures):
            field[row][col]['text'] = ''
            field[row][col]['background'] = curr_bg
# смена секвенции
def select_seq():
    # print(seq_current_btn.current(), '--', seq_current_btn.get())
    global curr_sequence
    curr_sequence = seq_current_btn.current()

def updSeqList():
    # print(seq_current_btn.current(),'--', seq_current_btn.get())
    pass
# установка текущих значений
def set_1():
    global curr_value
    curr_value = 0
    currVal_button['text'] = curr_value
    global curr_bg
    curr_bg = 'black'
    currVal_button['background'] = curr_bg
def set_2():
    global curr_value
    curr_value = 100
    currVal_button['text'] = curr_value
    global curr_bg
    curr_bg = 'grey'
    currVal_button['background'] = curr_bg
def set_3():
    global curr_value
    curr_value = 188
    currVal_button['text'] = curr_value
    global curr_bg
    curr_bg = 'white'
    currVal_button['background'] = curr_bg
def set_4():
    global curr_value
    curr_value = 230
    currVal_button['text'] = curr_value
    global curr_bg
    curr_bg = 'yellow'
    currVal_button['background'] = curr_bg

# обработка нажатия кнопки
def click(row, col):
    # field[row][col]['text'] = curr_value
    field[row][col]['background'] = curr_bg

# создание массива кнопок
for row in range(maxN_steps):
    line = []
    for col in range(maxN_fixtures):
        button = Button(root, text=' ', width=2, height=1,
                        font=('Verdana', 10, 'bold'),
                        fg='green',
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)


# создаём список секвенций
seq_current_btn = ttk.Combobox(root, values=sequence_list, postcommand=updSeqList)
seq_current_btn.grid(row=maxN_steps + 1, column=1, columnspan=5, sticky='nsew')

# кнопка выбора секвенции
sel_button = Button(root, text='sel', command=select_seq)
sel_button.grid(row=maxN_steps+1, column=6, columnspan=1, sticky='nsew')

# кнопка установки всех значений
clear_button = Button(root, text='clr', command=clear)
clear_button.grid(row=maxN_steps+1, column=7, columnspan=1, sticky='nsew')

# кнопка сохранения секвенции
save_button = Button(root, text='sav', command=clear)
save_button.grid(row=maxN_steps+1, column=0, columnspan=1, sticky='nsew')

# кнопка отображения текущего значения
currVal_button = Button(root, text=curr_value, fg='green', bg='black')
currVal_button.grid(row=maxN_steps+1, column=8, columnspan=2, sticky='nsew')

# кнопка установки текущих значений
l1_button = Button(root, text='0',background='black',fg='green', command=set_1)
l1_button.grid(row=maxN_steps+1, column=10, columnspan=1, sticky='nsew')
l2_button = Button(root, text='100',background='gray',fg='green', command=set_2)
l2_button.grid(row=maxN_steps+1, column=11, columnspan=1, sticky='nsew')
l3_button = Button(root, text='188',background='white',fg='green', command=set_3)
l3_button.grid(row=maxN_steps+1, column=12, columnspan=1, sticky='nsew')
l4_button = Button(root, text='230',background='yellow',fg='green', command=set_4)
l4_button.grid(row=maxN_steps+1, column=13, columnspan=1, sticky='nsew')

root.mainloop()