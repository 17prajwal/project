#!/usr/bin/env python
# coding: utf-8

# In[2]:


admin_keys = {"Prajwal": "praj@1234"}

menu = {1: {'Food Name': 'panner tikka masala', 'Food ID': 1, 'Price': 150, 'Discount': 10,  'Stock': 24},
        2: {'Food Name': 'Aloo masala',         'Food ID': 2, 'Price': 60,  'Discount': 0,   'Stock': 100},
        3: {'Food Name': 'veg.Manchuriya',      'Food ID': 3, 'Price': 70,  'Discount': 5,   'Stock': 50},
        4: {'Food Name': 'Tandoori Parata',     'Food ID': 4, 'Price': 10,  'Discount': 0,   'Stock': 60},
        5: {'Food Name': 'meals-plate',         'Food ID': 5, 'Price': 50,  'Discount': 2,   'Stock': 50}}
def add_new_item():
    foodname = input("Enter the foood name: ")
    foodid = int(input("Enter the food id: "))
    price = int(input("Enter the price of the food: "))
    discount = int(input("Enter the discount of food: "))
    stock = int(input("Enter te stock value of food: "))
    menu[foodid] = {
        "Food Name": foodname,
        "Food ID": foodid,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    print(f"The {foodname} is successfully added")
    return menu


def edit_from_item():
    food = int(input("Enter the foodid which you want to edit: "))
    a = input("Enter the food name")
    b = int(input("Enter the price of food"))
    c = int(input("Enter the discount of food"))
    d = int(input("Enter the stock of the food"))
    menu[food]["Food Name"] = a
    menu[food]["Price"] = b
    menu[food]["Discount"] = c
    menu[food]["Stock"] = d
    print("*****Edit food item successfully*****")
    return menu

def show_menu():
    print("***** THE MENU OF PRS HOTEL*****")
    for i in menu:
        print("Food Name: ",menu[i]["Food Name"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Food ID: ",menu[i]["Food ID"])

def remove_food_item():
    d = int(input("Enter the food id which you want to exit"))
    menu.pop(d)
    print("Remove food item successfully ")
    return menu


# In[ ]:




