import pandas as pd
from tkinter import *

root = Tk()
top_frame = Frame(root)
top_frame.pack()
bot_frame = Frame(root)
bot_frame.pack()
button1 = Button(top_frame, text = 'Wczytaj pierwszy BOM', fg='black')
button1.pack(side=LEFT)
button2 = Button(top_frame, text = 'Wczytaj drugi BOM', fg='black')
button2.pack(side=RIGHT)
button3 = Button(bot_frame, text = 'Sprawdz wynik', fg='black')
button3.pack(side=RIGHT)

root.mainloop()

file1 = open('X0402100_V104_1.csv', 'r')
file2 = open('100-05443_V104_1.csv', 'r')

my_csv = pd.read_csv(file1, sep = ';')
refdes1 = my_csv['REFDES']
my_csv = pd.read_csv(file2, sep = ';')
refdes2 = my_csv['REFDES']

list_f1 = []
list_f2 = []
list_comp = []

for line in refdes1:
    list_f1.append(line)
for line in refdes2:
    list_f2.append(line)
for i in list_f1:
    if i not in list_f2:
        list_comp.append(i)
print(list_comp)
list_comp = []
for i in list_f2:
    if i not in list_f1:
        list_comp.append(i)
print(list_comp)
