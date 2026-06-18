import tkinter as tk


def set_default_values(a):
    a.delete(0, tk.END)
    a.insert(0, '0')


def int_check(a):
    if a == '' or a == ' ':
        return 0
    return int(a)
