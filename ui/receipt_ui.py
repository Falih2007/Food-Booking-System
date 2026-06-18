import tkinter as tk
from tkinter import ttk


class ReceiptFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tree = None
        self.total_frame = None
        self.create_widgets()

    def create_widgets(self):
        self.grid(row=0, column=0, sticky="nsew")
        receipt_frame = ttk.Frame(self)
        receipt_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.tree = ttk.Treeview(receipt_frame, columns=('Item', 'Quantity', 'Size', 'Total Cost'), show='headings')
        self.tree.heading('Item', text='Item')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Size', text='Size')
        self.tree.heading('Total Cost', text='Total Cost')
        self.tree.grid(row=0, column=0, sticky='nsew')
        self.total_frame = ttk.Label(self, text=" Total Cost: $0.00 ", relief='sunken', padding=(10, 5), font=('Arial', 12, 'bold'))
        self.total_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')
