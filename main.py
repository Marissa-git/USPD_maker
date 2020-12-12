# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:22:27 2020

@author: Masha
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import pandas as pd


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.init_main(root)

    def open_file_tkinter(self):
        filename = filedialog.askopenfilename(defaultextension='.csv',
                                              filetypes=[
                                                  ("csv files", "*.csv"),
                                              ]
                                              )
        self.entry_0_string.set(filename)

    def open_file_tkinter_write(self):
        finish_filename = filedialog.askopenfilename(defaultextension='.csv',
                                                     filetypes=[
                                                         ("csv files", "*.csv"),
                                                     ]
                                                     )
        self.entry_2_string.set(finish_filename)

    def show_warning(self, msg):
        messagebox.showwarning("Предупреждение", msg)

    def clear_line(self):
        self.text_1.delete('1.0', tk.END)

    def calculation(self):
        self.clear_line()
        filename = self.entry_0_string.get()
        USPD = self.entry_1_string.get()
        finish_filename = self.entry_2_string.get()
        if finish_filename[len(finish_filename) - 4:len(finish_filename)] != ".csv":
            self.show_warning("Введите корректное имя файла записи, на конце должно быть .csv")
            return 1

        if USPD.isdigit():
            USPD = int(USPD)
        else:
            self.show_warning("Введите целое число в поле для USPD")
            return 1

        if os.path.isfile(filename):
            file = pd.read_csv(filename, delimiter=';')
        else:
            self.show_warning("Введите корректное имя считываемого файла")
            return 1
        finish_file = pd.DataFrame(file.loc[file['USPD'] == USPD])
        finish_file.to_csv(finish_filename, sep=";", index=False)
        self.text_1.insert(1.0, 'Файл готов!')

        return filename

    def init_main(self, root):

        open_file_label = tk.Label(root, text='Выберите путь к файлу с базой данных(csv):').grid(row=1,
                                                                                                 column=0, sticky='W')
        button_open_file = tk.Button(text="Открыть файл", bg='#FFFFE0', command=lambda:
        self.open_file_tkinter()).grid(row=5, column=0, sticky='W')
        button_calculation = tk.Button(text="Создать csv", bg='#FFFFE0', command=lambda:
        self.calculation()).grid(row=5, column=0, padx=260, sticky='W')
        write_to__file_label = tk.Label(root, text='Выберете/вбейте путь к новому csv файлу:').grid(row=3,
                                                                                                    column=0,
                                                                                                    sticky='W')
        button_open_file_to_write = tk.Button(text="Выбрать файл записи", bg='#FFFFE0', command=lambda:
        self.open_file_tkinter_write()).grid(row=5, column=0, padx=110, sticky='W')

        self.entry_0_string = tk.StringVar()
        self.entry_1_string = tk.StringVar()
        self.entry_2_string = tk.StringVar()

        USDP_info = tk.Label(root, text='Введите нужное USPD:').grid(row=2, column=0, sticky='W')
        res = tk.Label(root, text='Результат:').grid(row=4, column=0, sticky='W')

        entry_0 = tk.Entry(textvariable=self.entry_0_string, justify="left", width=70).grid(row=1, column=0,
                                                                                            padx=400, sticky='W',
                                                                                            columnspan=11)
        entry_1 = tk.Entry(textvariable=self.entry_1_string, justify="left", width=70).grid(row=2, column=0,
                                                                                            padx=400, sticky='W',
                                                                                            columnspan=11)
        entry_2 = tk.Entry(textvariable=self.entry_2_string, justify="left", width=70).grid(row=3, column=0,
                                                                                            padx=400, sticky='W',
                                                                                            columnspan=11)

        self.text_1 = tk.Text(height=1, width=20, font=("Times New Roman", 12), wrap="word")
        self.text_1.grid(row=4, column=0, padx=400, sticky='W', columnspan=11)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.grid()
    root.title("USPD")
    root.geometry("850x150+300+150")
    root.resizable(False, False)
    root.mainloop()
