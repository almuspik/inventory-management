# Inventory Management System

This is an Inventory Management System built with Python, using `pandas` for managing inventory data and `tkinter` for the graphical user interface (GUI). The system allows users to add, update, display, and remove items in the inventory, and it saves the data to an Excel file (`inventory.xlsx`).



## Tools Used

- **Python**: The programming language used to build the application.
- **Tkinter**: A built-in Python library used for creating the graphical user interface (GUI).
- **Pandas**: A powerful Python library for data manipulation and analysis, used here to manage and store the inventory data.
- **Openpyxl**: A Python library for reading and writing Excel files, used for storing the inventory data in `.xlsx` format.



## Features

- **Load Inventory**: Load inventory from an existing Excel file or create a new empty inventory.
- **Add Item**: Add new items to the inventory with details such as item ID, name, quantity, and price.
- **Update Quantity**: Update the quantity of an existing item in the inventory.
- **Remove Item**: Remove an item from the inventory by its ID.
- **Display Inventory**: View the full inventory in a dialog box.
- **Data Persistence**: All changes to the inventory are saved to the `inventory.xlsx` file.

## Requirements

- Python 3.x
- `pandas` library
- `tkinter` library (typically comes with Python, but can be installed if missing)
- `openpyxl` (for reading and writing Excel files)

You can install the necessary Python packages using pip:

pip install pandas 
