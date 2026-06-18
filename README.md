# 🍽️ Food Booking System

A desktop-based restaurant food ordering and management application built with Python, Tkinter, and MySQL.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Menu & Pricing](#menu--pricing)
- [Known Bugs](#known-bugs)
- [Project Structure](#project-structure)

---

## Overview

The Food Booking System is a GUI application for managing restaurant orders. Staff can register customers, select food and beverage items, specify sizes and quantities, set spice levels, and generate itemised receipts. All order data is stored in a local MySQL database and can be retrieved at any time using a customer ID.

---

## Features

- **Customer Registration** — Enter name, phone number, and address with input validation
- **Interactive Menu Meters** — Visual dials to select quantities for food, beverages, and desserts
- **Detailed Order Entry** — Specify sizes (Small/Medium/Large) for pizza, burger, milkshake, and watermelon juice
- **Spice Level Selection** — Set spice levels (1–5) for Butter Chicken and Grilled Wrap
- **Tea & Coffee Customisation** — Choose type and sugar preference
- **Receipt Generation** — Itemised receipt with quantities, sizes, and total cost
- **Database Tab** — Retrieve past orders by entering a customer ID
- **Toast Notifications** — Visual feedback on successful customer registration
- **Input Validation** — Prevents letters in phone number fields and digits in name/address fields

---

## Requirements

### Python Version
Python **3.8 or higher**

### Python Libraries

| Library | Purpose |
|---|---|
| `mysql-connector-python` | MySQL database connection |
| `ttkbootstrap` | Themed Tkinter widgets and components |
| `Pillow` | Image compatibility fix for ttkbootstrap |
| `tkinter` | GUI framework (built-in) |
| `winsound` | Error sound alerts (built-in, Windows only) |
| `datetime` | Date and time stamping orders (built-in) |

> ⚠️ **This application is Windows-only** due to the use of `winsound`.

---

## Installation

**1. Clone or download the project files.**

**2. Install the required Python libraries:**

```bash
pip install mysql-connector-python ttkbootstrap Pillow
```

**3. Ensure MySQL Server is installed and running.**
Download from: https://dev.mysql.com/downloads/mysql/

---

## Database Setup

**1. Open MySQL and create the project database:**

```sql
CREATE DATABASE project;
```

**2. Update the database password in the source code** if needed:

```python
con = mycon.connect(host='localhost', user='root', passwd='YOUR_PASSWORD', database='project')
```

**3. The application will automatically create all required tables on first run**, including:

- `customers` — main customer and order summary table
- `pizza`, `burger` — size breakdown tables
- `tikka`, `wrap` — spice level tables
- `tea`, `coffee` — beverage type tables
- `choco`, `watermelon` — milkshake and juice size tables
- `icecream`, `gulabjamun`, `cheesecake`, `kunafa` — dessert tables

---

## Running the Application

```bash
python food_booking.py
```

---

## How to Use

### Placing a New Order

1. **Customer Tab** — Enter the customer's name, phone number, and address, then click **CONFIRM**
2. **Menu Meters Window** — Use the interactive dials to select how many of each item the customer wants, then click **CONFIRM ORDER**
3. **Order Details Window** — Use the tabs to break down quantities by size (e.g. 2 small + 1 large pizza), set spice levels, and choose tea/coffee types
4. **Place Order** — Click **Place Order** to finalise and save to the database
5. **Receipt** — Click **Generate Receipt** to view the itemised bill
6. Click **Next Customer** to reset and start a new order

### Retrieving a Past Order

1. Go to the **Database Tab**
2. Enter the customer's ID number
3. Click **GET RECEIPT** to view their order and total cost

---

## Menu & Pricing

### 🍕 Food

| Item | Size | Price |
|---|---|---|
| Pizza | Small | $10.00 |
| Pizza | Medium | $15.00 |
| Pizza | Large | $20.00 |
| Burger | Small | $4.00 |
| Burger | Medium | $8.00 |
| Burger | Large | $12.00 |
| Butter Chicken | — | $14.00 |
| Grilled Chicken Wrap | — | $5.00 |

### ☕ Beverages

| Item | Price |
|---|---|
| Karak Tea | $1.50 |
| Green Tea | $1.00 |
| Black Tea | $0.50 |
| Latte | $2.00 |
| Cappuccino | $2.50 |
| Americano | $3.00 |
| Chocolate Milkshake (Small) | $7.50 |
| Chocolate Milkshake (Medium) | $9.00 |
| Chocolate Milkshake (Large) | $12.00 |
| Watermelon Juice (Small) | $6.00 |
| Watermelon Juice (Medium) | $7.50 |
| Watermelon Juice (Large) | $8.00 |

### 🍨 Desserts

| Item | Price |
|---|---|
| Ice Cream | $1.00 |
| Gulab Jamun | $4.00 |
| Cheese Cake | $6.00 |
| Kunafa | $7.00 |

---

## Known Bugs

1. **Size mismatch not shown in GUI** — If the sizes entered don't add up to the total ordered on the meter (e.g. ordered 2 pizzas but entered 3 small), the error is only printed to the console and not displayed to the user.

2. **Zero-quantity items not validated** — If an item was set to 0 on the meter but quantities are still entered in the detail window (e.g. 0 tea ordered but 1 karak entered), the data is silently inserted into the database with no warning. This affects pizza, burger, tea, coffee, milkshake, and watermelon juice.

3. **Address validation too strict** — `address.isalpha()` rejects addresses with spaces, numbers, or punctuation (e.g. "123 Main St" would fail).

---

## Project Structure

```
food_booking.py       # Main application file (all code)
README.md             # This file
```

All database tables are created automatically at runtime. No separate SQL schema file is required.
