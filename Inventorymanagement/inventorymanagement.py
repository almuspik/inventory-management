import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the inventory from the Excel file
def load_inventory(filename):
    try:
        inventory = pd.read_excel(filename)
        print(f"Inventory loaded successfully from {filename}")
    except FileNotFoundError:
        # Create an empty DataFrame if the file does not exist
        inventory = pd.DataFrame(columns=["ItemID", "ItemName", "Quantity", "Price"])
        print(f"File {filename} not found. Created an empty inventory.")
    except Exception as e:
        print(f"Error loading inventory: {e}")
        inventory = pd.DataFrame(columns=["ItemID", "ItemName", "Quantity", "Price"])
    return inventory

# Save the inventory to the Excel file
def save_inventory(filename, inventory):
    try:
        inventory.to_excel(filename, index=False)
        print(f"Inventory saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Add a new item to the inventory
def add_item(inventory, item_id, item_name, quantity, price):
    new_item = pd.DataFrame({"ItemID": [item_id], "ItemName": [item_name], "Quantity": [quantity], "Price": [price]})
    inventory = pd.concat([inventory, new_item], ignore_index=True)
    return inventory

# Update the quantity of an item
def update_quantity(inventory, item_id, quantity):
    inventory.loc[inventory['ItemID'] == item_id, 'Quantity'] = quantity
    return inventory

# Remove an item from the inventory
def remove_item(inventory, item_id):
    inventory = inventory[inventory['ItemID'] != item_id]
    return inventory

# Display the inventory
def display_inventory(inventory):
    return inventory.to_string(index=False)

# GUI Functions
def show_inventory():
    try:
        inventory_str = display_inventory(inventory)
        messagebox.showinfo("Inventory", inventory_str)
    except Exception as e:
        print(f"Error displaying inventory: {e}")
        messagebox.showerror("Error", f"Error displaying inventory: {e}")

def add_item_gui():
    try:
        item_id = item_id_entry.get()
        item_name = item_name_entry.get()
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
        global inventory
        inventory = add_item(inventory, item_id, item_name, quantity, price)
        save_inventory(filename, inventory)
        messagebox.showinfo("Success", "Item added successfully")
    except ValueError:
        print("Invalid input for quantity or price.")
        messagebox.showerror("Error", "Invalid input for quantity or price. Please enter numbers.")
    except Exception as e:
        print(f"Error adding item: {e}")
        messagebox.showerror("Error", f"Error adding item: {e}")

def update_quantity_gui():
    try:
        item_id = item_id_entry.get()
        quantity = int(quantity_entry.get())
        global inventory
        inventory = update_quantity(inventory, item_id, quantity)
        save_inventory(filename, inventory)
        messagebox.showinfo("Success", "Quantity updated successfully")
    except ValueError:
        print("Invalid input for quantity.")
        messagebox.showerror("Error", "Invalid input for quantity. Please enter a number.")
    except Exception as e:
        print(f"Error updating quantity: {e}")
        messagebox.showerror("Error", f"Error updating quantity: {e}")

def remove_item_gui():
    try:
        item_id = item_id_entry.get()
        global inventory
        inventory = remove_item(inventory, item_id)
        save_inventory(filename, inventory)
        messagebox.showinfo("Success", "Item removed successfully")
    except Exception as e:
        print(f"Error removing item: {e}")
        messagebox.showerror("Error", f"Error removing item: {e}")

filename = 'inventory.xlsx'
inventory = load_inventory(filename)

# Create the GUI window
root = tk.Tk()
root.title("Inventory Management System")

tk.Label(root, text="Item ID").grid(row=0)
tk.Label(root, text="Item Name").grid(row=1)
tk.Label(root, text="Quantity").grid(row=2)
tk.Label(root, text="Price").grid(row=3)

item_id_entry = tk.Entry(root)
item_name_entry = tk.Entry(root)
quantity_entry = tk.Entry(root)
price_entry = tk.Entry(root)

item_id_entry.grid(row=0, column=1)
item_name_entry.grid(row=1, column=1)
quantity_entry.grid(row=2, column=1)
price_entry.grid(row=3, column=1)

tk.Button(root, text='Display Inventory', command=show_inventory).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Add Item', command=add_item_gui).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(root, text='Update Quantity', command=update_quantity_gui).grid(row=5, column=0, sticky=tk.W, pady=4)
