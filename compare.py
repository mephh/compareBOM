import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog



class CompareFrame(Frame):
    file1_path = ''
    file2_path = ''

    parameter = 'REFDES'

    def __init__(self):
        Frame.__init__(self)
        self.master.title('BOM Compare')
        self.master.rowconfigure(3, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.grid(sticky=W+E+N+S)
        self.button1 = Button(self, text = 'Wczytaj pliki', command=self.load_file, width=25)
        self.button1.grid(row=0, column=0, sticky=W)
        self.button2 = Button(self, text = 'Szukaj po', command=self.search_for, width=25)
        self.button2.grid(row=0, column=1, sticky=E)
        self.button3 = Button(self, text = 'Porownaj', command=self.compare_files, width=10)
        self.button3.grid(row=1, column=0)
        #do dodania grid z wartosciami, zapis do pliku i przycisk do otwarcia pliku
    def load_file(self):
        file1_path = filedialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                           ,("All files", "*.*") ))
        if file1_path != '':
            file2_path = filedialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                               ,("All files", "*.*") ))

        global path1
        path1 = file1_path
        global path2
        path2 = file2_path

    def search_for(self):
        answer = simpledialog.askstring('Porownaj', 'Która kolumnę chcesz porównać?')
        global parameter
        parameter = answer

    def compare_files(self):
        print(parameter)
        path_l1 = []
        path_l2 = []
        path_l1 = path1.split('/')   #find just filename
        path_l2 = path2.split('/')   #find just filename
        file1 = open(path1, 'r')
        file2 = open(path2, 'r')
        my_csv = pd.read_csv(file1, sep = ';')
        refdes1 = my_csv[parameter]
        my_csv = pd.read_csv(file2, sep = ';')
        refdes2 = my_csv[parameter]
# do dodania sprawdzenie wartosci komponentu
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
        with open('differences.txt', 'w') as output:
            output.write('not in ' + path_l2[-1] + ': ' + '\n')
            for each in list_comp:
                output.write(each + ', ')

        list_comp = []
        for i in list_f2:
            if i not in list_f1:
                list_comp.append(i)
        with open('differences.txt', 'a') as output:
            output.write('\n' + 'not in ' + path_l1[-1] + ': ' + '\n')
            for each in list_comp:
                output.write(each + ', ')

if __name__ == "__main__":
    CompareFrame().mainloop()
