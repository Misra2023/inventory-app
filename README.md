# inventory-app
Inventory Management Application
Welcome to our Inventory Management Application! This user-friendly tool is designed to streamline your inventory management process, making it easier and more efficient to keep track of your products. Whether you're a small business owner, a warehouse manager, or anyone dealing with inventory, our application is here to help.

Table of Contents
Getting Started
Key Benefits
How to Use
Examples
Support
Getting Started
To get started with our Inventory Management Application, follow these simple steps:

Installation:

Ensure you have Python 3.x installed on your computer.

Install the required libraries by running the following command in your terminal:

bash
Copy code
pip install click sqlalchemy
Download and Set Up:



Place the script in a directory of your choice.

Create an empty SQLite database file named inventory.db in the same directory. You can do this by running:

bash
Copy code
touch inventory.db
Initialize the Database:

Run the following command to set up the database schema and seed it with initial data:

bash
Copy code
python script_name.py
Replace script_name.py with the actual name of the script.

 # Key Benefits
Our Inventory Management Application offers numerous benefits to help you manage your inventory effectively:

1. User-Friendly CLI
Our application provides a user-friendly command-line interface (CLI) that is easy to use and accessible for users with varying technical expertise.
2. Efficient Product Management
Easily add, delete, and update product records in your inventory with simple commands.
Keep track of product names and quantities effortlessly.
3. Data Integrity
Prevent duplicate product entries with the built-in unique name constraint.
Maintain data integrity by ensuring that each product has a unique name.
4. Time Savings
Save time by quickly adding new products or updating existing ones without the need for complex interfaces or manual data entry.
5. Seamless Integration
Seamlessly integrate the application into your existing workflow or database systems.
 # How to Use
Our Inventory Management Application offers three primary commands for managing your inventory:

 # Adding /Deleteing / updating products
you can use this command
python3 app.py
python3 app.py add-product
python3 app.py delete-product
python3 app.py update-product



#AUTHOR 
MISRA ABDI

#LICENCE 
MIT

