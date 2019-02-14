from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog

class CompareFrame(Frame):
    global path1
    global path2
    global parameter

    def __init__(self):
        parameter = ";"
        Frame.__init__(self)
        self.master.title('BOM Compare')
        self.master.rowconfigure(3, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.grid(sticky=W+E+N+S)
        self.button1 = Button(self, text = 'Wczytaj pliki', command=self.load_file, width=25)
        self.button1.grid(row=0, column=0, sticky=W)
        self.button2 = Button(self, text = 'Formatowanie', command=self.search_for, width=25)
        self.button2.grid(row=0, column=1, sticky=E)
        self.button3 = Button(self, text = 'Porownaj', command=self.compare_files, width=10)
        self.button3.grid(row=1, column=0)

    def load_file(self):
        self.path1 = filedialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                           ,("All files", "*.*") ))
        if self.path1 != '':
            self.path2 = filedialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                               ,("All files", "*.*") ))
    def search_for(self):
        self.parameter = simpledialog.askstring('Formatowanie', 'Jaki znak oddziela wartości?')

    def compare_files(self):
        with open (self.path1, encoding='utf8') as file1:           #doesnt work as unicode
            file1 = [line.rstrip('\n').split(self.parameter).pop(2) for line in file1]
        with open(self.path2, encoding='utf8') as file2:
            file2 = [line.rstrip('\n').split(self.parameter).pop(2) for line in file2]
        list_f1 = []
        list_f2 = []
        list_comp = []
        for line in file1:
            list_f1.append(line)
        for line in file2:
            list_f2.append(line)
        for i in list_f1:
            if i not in list_f2:
                list_comp.append(i)
        with open('differences.txt', 'w') as output:
            output.write('not in ' + self.path2 + ': ' + '\n')
            for each in list_comp:
                output.write(each + ', ')
        list_comp = []
        for i in list_f2:
            if i not in list_f1:
                list_comp.append(i)
        with open('differences.txt', 'a') as output:
            output.write('\n' + 'not in ' + self.path1 + ': ' + '\n')
            for each in list_comp:
                output.write(each + ', ')

if __name__ == "__main__":
    CompareFrame().mainloop()
