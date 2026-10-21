# Final Project Miriam Rose

For the Pete's Fish and Chips ordering application, customers
will be able to choose items from the menu, choose if they 
would like pickup or delivery, and choose the restaurant 
location for their order.

## Install required libraries
Ensure that you are in the main directory and 
run the following:

_This must be done before you can run the application
if you are not using the included venv._

```shell
$ pip install -r requirements.txt
```
or 
```shell
$ pip install PILLOW
$ pip install pytest
```

## To run the program
Click the green triangle run icon in the 
top-right corner of the PyCharm window.
or
```shell
$ python3 mrose16_projectgui.py
```

## Functionality
### Choose menu items
The menu items are listed as checkboxes, and 
they have the following information:

1. Fish and Chips..........$8.00
2. Shrimp and Chips...$10.00
3. Crab and Chips.......$10.00
4. Chicken Tenders.......$7.00
5. Seafood Combo........$8.00
6. Monster Burger.........$9.00
7. Hot Dog....................$5.00
8. Fish Sandwich..........$4.00

### Choose Pickup or Delivery
The order types of Pickup or Delivery are displayed
as radio buttons for the customers order. The address
entry field will be disabled if Pickup is selected.

### Enter Name:
The name entry field will accept the customers name 
for their order.

### Enter Address:
The address entry field will accept the customers 
address for their order if the Delivery radio button 
was selected. The field is disabled for Pickup.

### Next
The application will change to the location page 
when the next button is clicked.

### Choose restaurant location
The restaurant locations and addresses are listed
as radio buttons. Only one location can be selected.

### Submit
The order will be saved to the orders.csv file
when the submit button is clicked.

### Exit
The application will be closed when the Exit
button is clicked.

## Data files
### orders.csv
The file contains the transaction data in the 
following format:

| Name   | Time                     | Address                             | Order Type | Orders | Cost | Location  | 
|--------|--------------------------|-------------------------------------|------------|--------|------|-----------|
| Miriam | Wed Apr 24 14:17:20 2024 | "123 N. Pine Ln, Phoenix, AZ 85225" | Delivery   | 5 6    | 17.0 | Phoenix 3 |
| Kyle   | Thu Apr 25 12:55:57 2024 |                                     | Pickup     | 1 2    | 18.0 | Tolleson  |


## Class

### Order Class

#### Variables
Each Order instance has the following instance
variables:
1. name: private, string data type
2. time: private, string data type
3. address: private, string data type
4. order_type: private, Pickup or Delivery, integer data type
5. cost: private, float data type
6. location: private, string data type
7. orders: private, list data structure

Each Account instance has the following properties:
- name getter
- name setter
- orders getter
- orders setter

#### Methods
The Order class has the following methods:
* The dunder"__init__" method
* The add_order instance method

## Auto Testing
Run the following command to test the 
Auto_testing.py file. There are 4 test cases.

```shell
$ pytest -v Auto_testing.py
```

