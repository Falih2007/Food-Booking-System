import tkinter as tk
from tkinter import ttk


def build_customer_widgets(customer_frame):
    customername_label = tk.Label(customer_frame, text="NAME")
    customername_label.grid(row=0, column=0, padx=10, pady=10)
    c_name = ttk.Entry(customer_frame)
    c_name.grid(row=0, column=1, padx=10, pady=10)

    customerphoneno_label = tk.Label(customer_frame, text="PHONE")
    customerphoneno_label.grid(row=1, column=0, padx=10, pady=10)
    c_phone_no = ttk.Entry(customer_frame)
    c_phone_no.grid(row=1, column=1, padx=10, pady=10)

    customeraddress_label = tk.Label(customer_frame, text="ADDRESS")
    customeraddress_label.grid(row=2, column=0, padx=10, pady=10)
    c_address = ttk.Entry(customer_frame)
    c_address.grid(row=2, column=1, padx=10, pady=10)

    return {
        'customername_label': customername_label,
        'c_name': c_name,
        'customerphoneno_label': customerphoneno_label,
        'c_phone_no': c_phone_no,
        'customeraddress_label': customeraddress_label,
        'c_address': c_address,
    }
